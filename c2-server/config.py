"""
C2 Server Configuration
"""

import os
import base64
from typing import Optional

class Config:
    """Base configuration"""
    
    # Server settings
    HOST = os.getenv('C2_HOST', '0.0.0.0')
    PORT = int(os.getenv('C2_PORT', '8443'))
    WORKERS = int(os.getenv('C2_WORKERS', '4'))
    
    # Security
    MASTER_KEY = os.getenv('C2_MASTER_KEY')
    if not MASTER_KEY:
        from cryptography.fernet import Fernet
        MASTER_KEY = base64.b64encode(Fernet.generate_key()).decode()
        print(f"[!] Generated new master key: {MASTER_KEY}")
    MASTER_KEY_B64 = MASTER_KEY
    
    # Database
    DB_PATH = os.getenv('C2_DB_PATH', 'c2.db')
    
  
    JWT_SECRET = os.getenv('JWT_SECRET', 'change-me-in-production')
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION = int(os.getenv('JWT_EXPIRATION', '3600'))
    
   
    RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'true').lower() == 'true'
    RATE_LIMIT_REQUESTS = int(os.getenv('RATE_LIMIT_REQUESTS', '100'))
    RATE_LIMIT_PERIOD = int(os.getenv('RATE_LIMIT_PERIOD', '60'))
    

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'c2.log')
    
    # Pperators
    ALLOWED_TOKENS = os.getenv('ALLOWED_TOKENS', 'dev-token-123,testtoken').split(',')
    
    @classmethod
    def validate(cls):
        """Validate critical configuration"""
        if cls.JWT_SECRET == 'change-me-in-production':
            print("[!] WARNING: Using default JWT secret - change in production")
        
        if not cls.MASTER_KEY:
            raise ValueError("MASTER_KEY must be set")


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'INFO'
    
    @classmethod
    def validate(cls):
        super().validate()
        if cls.JWT_SECRET == 'change-me-in-production':
            raise ValueError("JWT_SECRET must be changed in production")
