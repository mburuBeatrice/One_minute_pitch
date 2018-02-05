class Config:
    '''
    General configuration parent class
    '''
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beatrice shiro:ciru6254#@localhost/pitch'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True