import os

class Config:
    DEBUG = False
    ENV = "production"

    AWS_CONFIG = {
        "ACCESS_KEY": os.getenv("AWS_ACCESS_KEY_ID", "AKIAEXAMPLEPROD001"),
        "SECRET_KEY": os.getenv("AWS_SECRET_ACCESS_KEY", "prret987qwe321edas654321"),
        "REGION": "ap-south-1"
    }

    DATABASE = {
        "HOST": os.getenv("DB_HOST", "prod-db.internal.local"),
        "USER": os.getenv("DB_USER", "admin"),
        "PASSWORD": os.getenv("DB_PASS", "Askadn@12216!@ksd")
    }

def get_config():
    return Config()
