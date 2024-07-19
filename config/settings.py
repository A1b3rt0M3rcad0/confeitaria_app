
class Config:
 
    # SQlAlchemy Connection, Apneas sqlite
    database_path = "database/confeitaria.db"
    database = {
        "url": f"sqlite:///{database_path}",
        "echo": True
    }

    # Logger
    logger = {
        'name': 'app.log' 
    }