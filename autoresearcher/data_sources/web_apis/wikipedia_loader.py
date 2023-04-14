import wikipedia

from autoresearcher.data_sources.web_apis.base_web_api_data_loader import BaseWebAPIDataLoader

class WikipediaLoader(BaseWebAPIDataLoader):
    def __init__(self):
        super().__init__("https://en.wikipedia.org/w/api.php")

    def fetch_data(self, search_query, results=10, language="en"):
        wikipedia.set_lang(language)
        wikipedia.set_rate_limiting(True)
        
        search_results = wikipedia.search(search_query, results=results)
        data = []

        for result in search_results:
            try:
                page = wikipedia.page(result)
                data.append({
                    "title": page.title,
                    "url": page.url,
                    "summary": page.summary,
                    "content": page.content,
                    "categories": page.categories,
                    "references": page.references,
                })
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation pages by selecting the first option
                if e.options:
                    page = wikipedia.page(e.options[0])
                    data.append({
                        "title": page.title,
                        "url": page.url,
                        "summary": page.summary,
                        "content": page.content,
                        "categories": page.categories,
                        "references": page.references,
                    })
            except wikipedia.exceptions.PageError:
                # Skip pages that cannot be found
                continue

        return data

