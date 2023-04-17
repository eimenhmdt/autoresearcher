import os
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL", "")
assert EMAIL, "EMAIL environment variable is missing from .env"


def get_citation_by_doi(doi):
    """
    Retrieves a citation for a given DOI.
    Args:
      doi (str): The DOI of the citation to retrieve.
    Returns:
      str: The citation for the given DOI.
    Raises:
      ValueError: If the response is not valid JSON.
    Notes:
      Requires an email address to be set in the EMAIL environment variable.
    Examples:
      >>> get_citation_by_doi("10.1038/s41586-020-2003-7")
      "Liu, Y., Chen, X., Han, M., Li, Y., Li, L., Zhang, J., ... & Zhang, Y. (2020). A SARS-CoV-2 protein interaction map reveals targets for drug repurposing. Nature, 581(7809), 561-570."
    """
    url = f"https://api.citeas.org/product/{doi}?email={EMAIL}"
    response = requests.get(url)
    try:
        data = response.json()
        return data["citations"][0]["citation"]
    except ValueError:
        return response.text
