import requests

url = "http://localhost:5051/v1/account/urn:uuid:aeb6da93-1410-a954-6836-b147cd14904f"

payload={}
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
