import requests
import json

url = "http://localhost:5051/v1/account/login"

payload = json.dumps({
  "login": "commodo",
  "password": "veniam do dolor",
  "rememberMe": False
})
headers = {
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
