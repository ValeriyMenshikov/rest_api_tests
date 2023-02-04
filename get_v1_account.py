import requests

url = "http://localhost:5051/v1/account"

payload={}
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
