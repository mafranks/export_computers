import csv
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
# Setup up authentication object
AUTH = (CLIENT_ID, API_KEY)
# Set the URL - CHANGE THIS IF YOU'RE NOT IN THE NAM REGION
BASE_URL = 'https://api.amp.cisco.com/v1/computers'
# Max limit is 500
LIMIT = 500

def fetch_computers(offset=0):
    """Pulls a dictionary of computers from the API"""

    params = {
        'limit': LIMIT,
        'offset': offset
    }
    response = requests.get(BASE_URL, params=params, auth=AUTH)
    response.raise_for_status()
    return response.json()

def main():
    """Main function to fetch all computers and save to CSV"""
    all_computers = []
    offset = 0

    while True:
        data = fetch_computers(offset)
        computers = data.get('data', [])
        if not computers:
            break
        all_computers.extend(computers)
        offset += len(computers)

    # Define the row headers (If you get a ValueError for a field that is added in the future, add it here)
    headers = [
        'connector_guid', 'hostname', 'windows_processor_id', 'active', 'links', 'operating_system',
        'os_version', 'internal_ips', 'external_ip', 'flag', 'id', 'install_date', 'is_compromised',
        'demo', 'windows_machine_guid', 'os_type', 'supports', 'network_addresses', 'connector_version',
        'group_guid', 'policy', 'groups', 'last_seen', 'av_update_definitions', 'faults', 'isolation',
        'orbital', 'risk_score', 'csc_id', 'bp_signature', 'serial_number'
    ]

    # Save the information to a CSV
    with open('computers.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_computers)

if __name__ == '__main__':
    main()
