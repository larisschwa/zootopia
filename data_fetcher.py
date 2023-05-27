import json
import requests

API_KEY = 'FarKzLiOWsIRRYVTCpmIUQ==ftVMNYUNZ5AzuNFv'


def fetch_data(animal):
    """
      Fetches the animals data for the animal 'animal_name'.
      Returns: a list of animals, each animal is a dictionary:
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
      },
      """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None