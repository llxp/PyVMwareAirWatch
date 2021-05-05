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
# system_info = a.info.get_environment_info()
# pprint.pprint(system_info)

#users = a.users.search(username="mfuchs")
#pprint.pprint(users)
sample_group = a.groups.search_group_id(name="Local Home")
pprint.pprint(sample_group)

sample_app = a.apps.get_id(applicationname="Notepad++ (x64)", locationgroupid=sample_group)
pprint.pprint(sample_app)

# sample_app_detail = a.apps.search_details(sample_app)
# pprint.pprint(sample_app_detail)
app_installed_on_devices = a.apps.check_app_installed(sample_app)
pprint.pprint(app_installed_on_devices)

# for device in app_installed_on_devices:
#     device_info = a.devices.get_details_by_device_id(device)
#     if device_info['Udid'] == "E90E043BC46F6B42B16586DA1D9C5168":
#         print("Found a match!")
#         print(f"Hostname: {device_info['DeviceReportedName']} & DeviceUDID: {device_info['Udid']}")
#         break
#     else:
#         print("Match not found")
#         pass

