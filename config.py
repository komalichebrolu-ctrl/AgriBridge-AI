import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'agribridge_default_secret_key_2026')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2MB MAX
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
    SUPPORTED_LANGUAGES = ['en', 'hi', 'te']
    DEFAULT_LANGUAGE = 'en'
