"""
Konfigurasi aplikasi Input Penjualan
"""

import os

class Config:
    """Konfigurasi dasar aplikasi"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///penjualan.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Konfigurasi server
    HOST = os.environ.get('HOST') or '0.0.0.0'
    PORT = int(os.environ.get('PORT') or 8080)
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

class DevelopmentConfig(Config):
    """Konfigurasi untuk development"""
    DEBUG = True

class ProductionConfig(Config):
    """Konfigurasi untuk production"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-in-production'

# Mapping konfigurasi
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}