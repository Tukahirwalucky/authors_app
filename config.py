class Config:
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost/flaskauthors"
    JWT_SECRECT_KEY = 'authors'