
class Config:
 
    # SQlAlchemy Connection
    database = {
        "url": "sqlite:///database/confeitaria.db",
        "echo": True
    }

    # Logger
    logger = {
        'name': 'app.log' 
    }