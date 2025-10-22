import requests
from datetime import datetime

# Haal de huidige tijd op
now = datetime.now()
print(f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 40)

# Maak de request naar de API
response = requests.get('https://api.myip.com')

# Print de response
print(response.text)

# Of als je de data als JSON wilt verwerken:
data = response.json()
print(f"\nIP: {data['ip']}")
print(f"Country: {data['country']}")
print(f"CC: {data['cc']}")
print(f"\nRequest uitgevoerd op: {now.strftime('%Y-%m-%d om %H:%M:%S')}")