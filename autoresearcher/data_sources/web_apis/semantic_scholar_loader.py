from autoresearcher.data_sources.web_apis.base_web_api_data_loader import BaseWebAPIDataLoader
import jellyfish

class SemanticScholarLoader(BaseWebAPIDataLoader):
    def __init__(self):
        super().__init__("https://api.semanticscholar.org/graph/v1/paper/search")

    def fetch_data(self, search_query, limit=100, year_range=None):
        params = {
            "query": search_query,
            "limit": limit,
            "fields": "title,url,abstract,authors,citationStyles,journal,citationCount,year,externalIds"
        }

        if year_range is not None:
            params["year"] = year_range

        data = self.make_request("", params=params)
        return data.get('data', [])

    def fetch_and_sort_papers(self, search_query, limit=100, top_n=20, year_range=None, keyword_combinations=None, weight_similarity=0.5):
        papers = []
        if keyword_combinations is None:
            keyword_combinations = [search_query]

        for combination in keyword_combinations:
            papers.extend(self.fetch_data(combination, limit, year_range))

        max_citations = max(papers, key=lambda x: x['citationCount'])['citationCount']
        
        for paper in papers:
            similarity = jellyfish.jaro_similarity(search_query, paper['title'])
            normalized_citation_count = paper['citationCount'] / max_citations
            paper['combined_score'] = (weight_similarity * similarity) + ((1 - weight_similarity) * normalized_citation_count)

        sorted_papers = sorted(papers, key=lambda x: x['combined_score'], reverse=True)

        print("Top 20 papers:") 
        for paper in sorted_papers[:top_n]:
            print(paper['citationCount'], paper['title'], f"Combined Score: {paper['combined_score']:.2f}")

        return sorted_papers[:top_n]
    
    
