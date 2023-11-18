# importing modules
import requests
from bs4 import BeautifulSoup
import pandas as ps

# Base function
def main(surburl : str):
    # base url 
    base_url = "https://fr.wikipedia.org/wiki/"
    url = base_url + surburl

    return url

# execute function
if __name__ == "__main__":
    user_input = input("Votre recherche : ")
    print(f"{main(user_input)} \n")

