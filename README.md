# 🤖🧪 AutoResearcher

---

⚡ Automating scientic workflows with AI ⚡

[![Discord](https://img.shields.io/discord/1094636825647267910?label=AutoResearcher&logo=discord&style=flat-square)](https://discord.gg/PnQDR5h9)

---

## What is AutoResearcher?

AutoResearcher is an open-source Python package that combines AI models and external knowledge sources to automate scientific workflows. It is designed to help researchers and scientists to speed up their research process and to make it more efficient.

The project is a very early prototype and is still under development. Currently, it is limited to conducting literature reviews. The vision, however, is to create a tool that can conduct actual scientific discovery on autopilot.

If this vision excites you, please consider contributing to the project. You can start by joining the [Discord server](https://discord.gg/PnQDR5h9) and discussing your ideas with the community.

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
