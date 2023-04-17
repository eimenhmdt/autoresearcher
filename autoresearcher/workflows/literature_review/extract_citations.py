# Extract bibliographical citations from answers
def extract_citations(answers):
    """
    Extracts bibliographical citations from a list of answers.
    Args:
      answers (list): A list of strings containing answers.
    Returns:
      list: A list of strings containing bibliographical citations.
    Examples:
      >>> answers = ["This is an answer. SOURCE: Smith, J. (2020).",
      ...            "This is another answer. SOURCE: Jones, A. (2021)."]
      >>> extract_citations(answers)
      ["Smith, J. (2020)", "Jones, A. (2021)"]
    """
    citations = []
    for answer in answers:
        citation_start = answer.rfind("SOURCE: ")
        if citation_start != -1:
            citation = answer[citation_start + len("SOURCE: ") :]
            citations.append(citation)
    return citations
