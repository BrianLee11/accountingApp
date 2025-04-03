import requests

headers = {
    'User-Agent': 'Jane Doe CompanyX (jane.doe@example.com)'
}
url = 'https://data.sec.gov/submissions/CIK0000320193.json'  # Example for Apple Inc.
response = requests.get(url, headers=headers)
print(response.json())

print("Hello World Out there!")