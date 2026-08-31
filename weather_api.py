import requests
url="https://api.open-meteo.com/v1/forecast?latitude=33.4&longitude=-111.9&current=temperature_2m"
response=requests.get(url)
data=response.json()
print(data)
