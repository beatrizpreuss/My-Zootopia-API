import requests

API_KEY = 'tX+p7IesWxHN16/NqL2HRg==GrkHAE4JXFrM96K8'
ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals?name='
ANIMAL = 'chameleon'

res = requests.get(f'{ANIMAL_URL}{ANIMAL}', headers={'X-Api-Key': API_KEY})
resp = res.json()
print(resp)
