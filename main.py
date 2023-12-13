# Importing modules
import requests
from bs4 import BeautifulSoup
import pandas as ps

# Base function
def main(suburl : str):
    # Format user input 
    suburl = suburl.split()
    suburl = [word.capitalize() for word in suburl]
    suburl = "_".join(suburl)

    # Setting the search
    base_url = "https://fr.wikipedia.org/wiki/"
    url = base_url + suburl

    # Verifying errors > the url + response
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur : {response.status_code}")

    # Getting the data 
    soup = BeautifulSoup(response.text, "html.parser")

    h3 = list()
    for title in soup.find_all("p"):
        h3.append(title.text)
    

    return h3

# Execute function
if __name__ == "__main__":
    user_input = input("Votre recherche : ")
    print(f"{main(user_input)} \n")
