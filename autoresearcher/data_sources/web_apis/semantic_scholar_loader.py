from autoresearcher.data_sources.web_apis.base_web_api_data_loader import (
    BaseWebAPIDataLoader,
)
import jellyfish


class SemanticScholarLoader(BaseWebAPIDataLoader):
    def __init__(self):
        """
        Initializes the SemanticScholarLoader class.
        Args:
          None
        Returns:
          None
        Notes:
          Calls the superclass constructor with the SemanticScholar API URL.
        """
        super().__init__("https://api.semanticscholar.org/graph/v1/paper/search")

    def fetch_data(self, search_query, limit=100, year_range=None):
        """
        Fetches data from the SemanticScholar API.
        Args:
          search_query (str): The query to search for.
          limit (int, optional): The maximum number of results to return. Defaults to 100.
          year_range (tuple, optional): A tuple of two integers representing the start and end year of the search. Defaults to None.
        Returns:
          list: A list of paper objects.
        Examples:
          >>> fetch_data("machine learning", limit=50, year_range=(2010, 2020))
          [{...}, {...}, ...]
        """
        params = {
            "query": search_query,
            "limit": limit,
            "fields": "title,url,abstract,authors,citationStyles,journal,citationCount,year,externalIds",
        }

        if year_range is not None:
            params["year"] = year_range

        data = self.make_request("", params=params)
        return data.get("data", [])

    def fetch_and_sort_papers(
        self,
        search_query,
        limit=100,
        top_n=20,
        year_range=None,
        keyword_combinations=None,
        weight_similarity=0.5,
    ):
        """
        Fetches and sorts papers from the SemanticScholar API.
        Args:
          search_query (str): The query to search for.
          limit (int, optional): The maximum number of results to return. Defaults to 100.
          top_n (int, optional): The maximum number of results to return after sorting. Defaults to 20.
          year_range (tuple, optional): A tuple of two integers representing the start and end year of the search. Defaults to None.
          keyword_combinations (list, optional): A list of keyword combinations to search for. Defaults to None.
          weight_similarity (float, optional): The weight to give to the similarity score when sorting. Defaults to 0.5.
        Returns:
          list: A list of the top `top_n` paper objects sorted by combined score.
        Examples:
          >>> fetch_and_sort_papers("machine learning", limit=50, top_n=10, year_range=(2010, 2020))
          [{...}, {...}, ...]
        """
        papers = []
        if keyword_combinations is None:
            keyword_combinations = [search_query]

        for combination in keyword_combinations:
            papers.extend(self.fetch_data(combination, limit, year_range))

        max_citations = max(papers, key=lambda x: x["citationCount"])["citationCount"]

        for paper in papers:
            similarity = jellyfish.jaro_similarity(search_query, paper["title"])
            normalized_citation_count = paper["citationCount"] / max_citations
            paper["combined_score"] = (weight_similarity * similarity) + (
                (1 - weight_similarity) * normalized_citation_count
            )

        sorted_papers = sorted(papers, key=lambda x: x["combined_score"], reverse=True)

        # deduplicate paper entries prior to taking top n results
        sorted_dedup_papers = list(
            {each_paper["paperId"]: each_paper for each_paper in sorted_papers}.values()
        )

        return sorted_dedup_papers[:top_n]
