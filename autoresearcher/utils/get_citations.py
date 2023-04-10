import os
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL", "")
assert EMAIL, "EMAIL environment variable is missing from .env"

def get_citation_by_doi(doi):
    url = f"https://api.citeas.org/product/{doi}?email={EMAIL}"
    response = requests.get(url)
    data = response.json()
    return data["citations"][0]["citation"]