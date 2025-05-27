import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
ANIMAL_URL = 'https://api.api-ninjas.com/v1/animals?name='


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary
    """
    res = requests.get(f'{ANIMAL_URL}{animal_name}',
                     headers={'X-Api-Key': API_KEY})
    animals_resp = res.json()
    return animals_resp