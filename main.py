# Importing modules
import requests
from bs4 import BeautifulSoup
import pandas as ps

# Base function
def main(surburl : str):
    # Testing the user inputs
    
    # Setting the search
    base_url = "https://fr.wikipedia.org/wiki/"
    url = base_url + surburl

    # Verifying the url
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur : {response.status_code}")

    return ""

# Execute function
if __name__ == "__main__":
    user_input = input("Votre recherche : ")
    print(f"{main(user_input)} \n")
