import requests
import json

url = "http://localhost:5051/v1/account/password"

payload = json.dumps({
  "login": "irure",
  "email": "nisi in"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
