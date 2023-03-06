from dotenv import load_dotenv
load_dotenv()

import os 

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY =  os.environ['SECRET_KEY']