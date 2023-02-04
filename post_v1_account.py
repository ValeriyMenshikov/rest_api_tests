import requests
import json

url = "http://localhost:5051/v1/account"

payload = json.dumps({
  "login": "login_7",
  "email": "login_7@mail.ru",
  "password": "login_77"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
