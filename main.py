#!/usr/bin/env python3
from autoresearcher.workflows.literature_review import literature_review

research_question = "How will AI impact science?"
researcher = literature_review.literature_review(research_question)
researcher()
