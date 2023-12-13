# Importing modules
import requests
from bs4 import BeautifulSoup
import pandas as ps
from data_clean import regex_clean
from model import bert_summarizer

# Base function
def main(suburl : str):
    # Format user input 
    suburl = suburl.split()
    suburl = [word.capitalize() for word in suburl]
    suburl = "_".join(suburl)

    # Setting the search
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url + suburl

    # Verifying errors > the url + response
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur : {response.status_code}")

    # Getting the data 
    soup = BeautifulSoup(response.text, "html.parser")

    text_content = list()
    for title in soup.find_all("p"):
        text_content.append(title.text)
    
    return bert_summarizer(regex_clean(text_content[:3]))

# Execute function
if __name__ == "__main__":
    user_input = input("Votre recherche : ")
    print(f"{main(user_input)} \n")
