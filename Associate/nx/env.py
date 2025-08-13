from dotenv import load_dotenv
import os

user = os.environ.get('CISCOUSER')
print(user)