# AutoResearcher

[![Discord](https://img.shields.io/discord/123456789012345678?label=AutoResearcher&logo=discord&style=flat-square)](https://discord.gg/PnQDR5h9)

AutoResearcher is an open-source project that uses GPT-based AI models to automatically generate academic literature reviews based on a given research question. The script fetches top papers from the Semantic Scholar API, extracts relevant information, and combines the findings into a concise literature review.

The project is a very early prototype and is still under development. The vision is to create a tool that can conduct actual scientific discovery on autopilot.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/eimenhmdt/autoresearcher.git
```

2. Create a virtual environment and activate it:

```bash
cd autoresearcher
python3 -m venv venv
source venv/bin/activate
```

On Windows, use `venv\Scripts\activate` instead of `source venv/bin/activate`.

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project directory and add your OpenAI API key and an email of your choice (used to identify your API requests for getting citations):

```bash
OPENAI_API_KEY=<your_openai_api_key>
EMAIL=<your_email>
```

Replace <your_openai_api_key> with your actual API key from OpenAI.

## Usage

1. Open the main.py file and set your research question at the bottom of the script:

```python
research_question = "<your_research_question>"
```

Replace <your_research_question> with your desired research question.

2. Run the script with your research question as a command-line argument:

```bash
python auto_researcher.py "<your_research_question>"
```
Replace <your_research_question> with your desired research question. If no argument is provided, the script will use the default research question.

The script will fetch the top papers, extract answers, and generate a literature review.

## Contributing

Contributions are welcome! Please feel free to submit issues or create pull requests. Let's take upgrade science together! 🚀

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Made with coffee by [@eimenhamedat](https://twitter.com/eimenhmdt)
