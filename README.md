# 🤖🧪 AutoResearcher

---

⚡ Automating scientific workflows with AI ⚡

<a href="https://github.com/eimenhmdt/autoresearcher/">![GitHub Repo stars](https://img.shields.io/github/stars/eimenhmdt/autoresearcher?style=social)</a>
[![Discord](https://img.shields.io/discord/1094636825647267910?label=AutoResearcher&logo=discord&style=flat-square)](https://discord.gg/PnQDR5h9)

---

## What is AutoResearcher?

AutoResearcher is an open-source Python package that leverages AI models and external knowledge sources to automate scientific workflows. Designed to help researchers and scientists accelerate their research process and increase efficiency, AutoResearcher is a powerful tool for the modern scientific community.

Please note that the project is currently in its early prototype stage and under active development. Its present functionality is limited to conducting literature reviews, but the ultimate goal is to create a tool capable of driving scientific discovery on autopilot.

If this vision excites you, we invite you to contribute to the project. Start by joining our [Discord server](https://discord.gg/jUMfu4D4je) and discussing your ideas with our community.

## Documentation

Documentation for the package is available [here](https://eimenhmdt.github.io/autoresearcher/).

## Installation

Install the package using pip:

```bash
pip install autoresearcher
```

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

3. Create a literature_review instance with your research question and execute it:

```python
researcher = literature_review(research_question)
```

You can also pass an output file name as a .txt file:

```python
researcher = literature_review(research_question, output_file="my_literature_review.txt")
```

This will generate a literature review based on the research question.

Also, you can run it in one command:
```python
python run_autorsearcher.py --research_question "<your_research_question>" --output_file "<your_output_file>"
```

## Contributing

We welcome contributions! Feel free to submit issues or create pull requests. Together, let's revolutionize science! 🚀

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Made with ☕ by [@eimenhamedat](https://twitter.com/eimenhmdt)
