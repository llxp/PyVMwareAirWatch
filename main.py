from dotenv import load_dotenv
from pyairwatch.client import AirWatchAPI
import os
import pprint

# Load environment variables from .env
load_dotenv()

# Assign environment variables to CONSTANTS
MY_API_KEY = os.getenv('MY_API_KEY')
MY_USER = os.getenv('MY_USER')
MY_PASS = os.getenv('MY_PASS')
AW_API_URL= os.getenv('AW_API_URL')

# Build the AirWatch API Client
a = AirWatchAPI(env=f'{AW_API_URL}',
                apikey=f'{MY_API_KEY}',
                username=f'{MY_USER}',
                password=f'{MY_PASS}')

# Execute a system_info and pprint the output
system_info = a.info.get_environment_info()
pprint.pprint(system_info)