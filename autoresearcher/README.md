# AutoResearcher

[![Discord](https://img.shields.io/discord/1094636825647267910?label=AutoResearcher&logo=discord&style=flat-square)](https://discord.gg/PnQDR5h9)

AutoResearcher is an open-source Python package that uses GPT-based AI models to automatically generate academic literature reviews based on a given research question. The package fetches top papers from the Semantic Scholar API, extracts relevant information, and combines the findings into a concise literature review.

The project is a very early prototype and is still under development. The vision is to create a tool that can conduct actual scientific discovery on autopilot.

## Installation

Install the package using pip:

pip install autoresearcher

## Setting Environment Variables

Before using the package, you need to set the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for accessing the GPT-based AI models.
- `EMAIL`: An email address of your choice (used to identify your API requests for getting citations).

You can set the environment variables in your operating system or in your Python script using the `os` module:

```python
import os

os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"
os.environ["EMAIL"] = "<your_email>"
```

Replace <your_openai_api_key> and <your_email> with your actual API key and email address.

## Usage

1. Import the literature_review function from the package:

```python
from autoresearcher import literature_review
```

2. Set your research question as a string:

```python
research_question = "What is the best way to train a neural network?"
```

3. Create a literature_review instance with your research question:

```python
researcher = literature_review(research_question)
```

4. Execute the researcher instance to fetch and analyze relevant papers:

```python
researcher()
```

This will generate a literature review based on the research question.

## Contributing

Contributions are welcome! Please feel free to submit issues or create pull requests. Let's take upgrade science together! 🚀

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Made with ☕ by [@eimenhamedat](https://twitter.com/eimenhmdt)
