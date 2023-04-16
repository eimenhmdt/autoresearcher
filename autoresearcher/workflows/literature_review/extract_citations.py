# Extract bibliographical citations from answers
def extract_citations(answers):
    citations = []
    for answer in answers:
        citation_start = answer.rfind("SOURCE: ")
        if citation_start != -1:
            citation = answer[citation_start + len("SOURCE: "):]
            citations.append(citation)
    return citations