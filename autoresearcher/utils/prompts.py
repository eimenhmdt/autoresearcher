literature_review_prompt =  """"
`reset`
`no quotes`
`no explanations`
`no prompt`
`no self-reference`
`no apologies`
`no filler`
`just answer`

I will give you a list of research findings and a research question.

Synthesize the list of research findings to generate a scientific literature review. Also, identify knowledge gaps and future research directions.

Make sure to always reference every research finding you use with in-text citations in APA format using the source provided. 

Only use the research findings I provide you with to create your literature review. Only give me the output and nothing else.

Now, using the concepts above, create a literature review for this research question '{research_question}' using the following research findings:

{answer_list}
"""


extract_answer_prompt = """
`reset`
`no quotes`
`no explanations`
`no prompt`
`no self-reference`
`no apologies`
`no filler`
`just answer`

I will give you the abstract of an academic paper. Extract the answer to this research question: {research_question} from the abstract.

If the answer is not in the abstract, then you are only allowed to respond with 'No answer found'.

This is the abstract: {abstract}
"""

keyword_combination_prompt = """
`reset`
`no quotes`
`no explanations`
`no prompt`
`no self-reference`
`no apologies`
`no filler`
`just answer`

Generate several keyword combinations based on the following research question: {research_question}. 
Don't generate more than 5 keyword combinations.

The output should be structured like this:
Write "KeywordCombination:" and then list the keywords like so "Keyword,Keyword,Keyword"

"""