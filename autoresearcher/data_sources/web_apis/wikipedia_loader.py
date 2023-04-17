import wikipedia

from autoresearcher.data_sources.web_apis.base_web_api_data_loader import (
    BaseWebAPIDataLoader,
)


class WikipediaLoader(BaseWebAPIDataLoader):
    def __init__(self):
        super().__init__("https://en.wikipedia.org/w/api.php")

    def fetch_data(self, search_query, results=10, language="en"):
        """
        Fetches data from the Wikipedia API.
        Args:
          search_query (str): The query to search for.
          results (int, optional): The maximum number of results to return. Defaults to 10.
          language (str, optional): The language to search in. Defaults to "en".
        Returns:
          list: A list of dictionaries containing the data for each result.
        Raises:
          wikipedia.exceptions.DisambiguationError: If the search query returns a disambiguation page.
        Examples:
          >>> loader = WikipediaLoader()
          >>> loader.fetch_data("Python")
          [
            {
              "title": "Python (programming language)",
              "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
              "summary": "Python is an interpreted, high-level, general-purpose programming language.",
              "content": "Python is an interpreted, high-level, general-purpose programming language...",
              "categories": ["Programming languages"],
              "references": ["https://www.python.org/"]
            }
          ]
        """
        wikipedia.set_lang(language)
        wikipedia.set_rate_limiting(True)

        search_results = wikipedia.search(search_query, results=results)
        data = []

        for result in search_results:
            try:
                page = wikipedia.page(result)
                data.append(
                    {
                        "title": page.title,
                        "url": page.url,
                        "summary": page.summary,
                        "content": page.content,
                        "categories": page.categories,
                        "references": page.references,
                    }
                )
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation pages by selecting the first option
                if e.options:
                    page = wikipedia.page(e.options[0])
                    data.append(
                        {
                            "title": page.title,
                            "url": page.url,
                            "summary": page.summary,
                            "content": page.content,
                            "categories": page.categories,
                            "references": page.references,
                        }
                    )
            except wikipedia.exceptions.PageError:
                # Skip pages that cannot be found
                continue

        return data
