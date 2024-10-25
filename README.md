# Export Computers Script
Used to export computers from the Secure Endpoint API.

Set up a .env file in the same directory as the script with the following two entries:
```
API_KEY = ""
CLIENT_ID = ""
```
Add your Client ID and API Key from Secure Endpoints to the blank fields.

Install python-dotenv if you have not already:
```
pip intall python-dotenv
```
OR 
```
python -m pip install python-dotenv
```

If you're not in the NAM region, you'll need to edit the BASE_URL in main.py.
For EU:
```
BASE_URL = 'https://api.eu.amp.cisco.com/v1/computers'
```
For APJC:
```
BASE_URL = 'https://api.apjce.amp.cisco.com/v1/computers'
```

Then run the script and it should pull all your computers and save them to a computers.csv file in the same directory.

```
python .\main.py
```
