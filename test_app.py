import unittest
import json
import io
import os
from PIL import Image
from app import app

class AgriBridgeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'
        self.client = app.test_client()

    def test_health_check(self):
        """Test GET /health returns status ok."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['app'], 'AgriBridge AI')

    def test_home_page(self):
        """Test GET / renders index template successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        text = response.get_data(as_text=True)
        self.assertIn('AgriBridge AI', text)

    def test_set_language(self):
        """Test POST /set-language updates language in session."""
        # Test setting Telugu
        res_te = self.client.post('/set-language', json={'lang': 'te'})
        self.assertEqual(res_te.status_code, 200)
        data = res_te.get_json()
        self.assertEqual(data['lang'], 'te')

        # Check that page now renders in Telugu
        res_home = self.client.get('/')
        text_home = res_home.get_data(as_text=True)
        self.assertIn('రైతు', text_home) # Telugu word "Farmer"

        # Reset to English
        res_en = self.client.post('/set-language', json={'lang': 'en'})
        self.assertEqual(res_en.status_code, 200)

    def test_weather_module(self):
        """Test GET and POST /weather — works with Open-Meteo live data or demo fallback."""
        res_get = self.client.get('/weather')
        self.assertEqual(res_get.status_code, 200)

        res_post = self.client.post('/weather', data={'city': 'Guntur'})
        self.assertEqual(res_post.status_code, 200)
        text_post = res_post.get_data(as_text=True)
        # City name must always appear (from live data or demo fallback)
        self.assertIn('Guntur', text_post)
        # Page must show either live weather data or a Demo Mode badge
        self.assertTrue('°C' in text_post or 'Demo Mode' in text_post)

    def test_soil_module(self):
        """Test GET and POST /soil advisory logic."""
        res_get = self.client.get('/soil')
        self.assertEqual(res_get.status_code, 200)

        res_post = self.client.post('/soil', data={
            'moisture': 'dry',
            'crop_name': 'Cotton',
            'growth_stage': 'flowering',
            'soil_type': 'black'
        })
        self.assertEqual(res_post.status_code, 200)
        text_post = res_post.get_data(as_text=True)
        self.assertIn('Cotton', text_post)

    def test_crop_disease_upload_validation(self):
        """Test /crop with valid PIL image vs invalid file."""
        # Create a small valid test image in memory
        img = Image.new('RGB', (100, 100), color='green')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)

        res_valid = self.client.post('/crop', data={
            'crop_image': (img_byte_arr, 'test_leaf.jpg')
        }, content_type='multipart/form-data')
        self.assertEqual(res_valid.status_code, 200)
        text_valid = res_valid.get_data(as_text=True)
        self.assertIn('Simulated', text_valid)

        # Test invalid file format (.txt)
        txt_file = io.BytesIO(b"Not an image")
        res_invalid = self.client.post('/crop', data={
            'crop_image': (txt_file, 'test.txt')
        }, content_type='multipart/form-data')
        self.assertEqual(res_invalid.status_code, 200)
        text_invalid = res_invalid.get_data(as_text=True)
        self.assertIn('valid JPG or PNG', text_invalid)

    def test_chat_module(self):
        """Test POST /chat API endpoint for offline queries."""
        # Query about rain
        res_rain = self.client.post('/chat', json={'message': 'Should I irrigate if heavy rain is expected?'})
        self.assertEqual(res_rain.status_code, 200)
        data = res_rain.get_json()
        self.assertTrue('Irrigation' in data['response'] or 'rain' in data['response'].lower())

        # Query about heat
        res_heat = self.client.post('/chat', json={'message': 'How to protect crops from severe heat above 35 C?'})
        self.assertEqual(res_heat.status_code, 200)
        data_heat = res_heat.get_json()
        self.assertTrue('Heat' in data_heat['response'] or 'temperature' in data_heat['response'].lower())

    def test_404_error_page(self):
        """Test custom 404 handler for non-existent route."""
        response = self.client.get('/invalid-route-xyz')
        self.assertEqual(response.status_code, 404)
        text = response.get_data(as_text=True)
        self.assertIn('404', text)

if __name__ == '__main__':
    unittest.main()
