from dotenv import load_dotenv
load_dotenv()

import os 

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']