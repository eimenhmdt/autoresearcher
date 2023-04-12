# 🤖🧪🌏 AutoResearcher API & Plugin

---

⚡ Using APIs and ChatGPT Plugins to automate scientific workflows with AI ⚡

## What is the AutoResearcher API & Plugin?

This repo turns the AutoResearcher open-source package into both an API and a ChatGPT plugin.


## Running the API locally

To run this on your local machine:
- Create a `.env` file in the root folder of `autorsearcher` with two env variables. Use the `.env.examples` file for hints if you need it:
```
EMAIL=sample@test.com
OPENAI_API_KEY=sk-your-OpenAI-api-key
```
- In your terminal, go to `autoresearcher/api/`
- Install all Autoresearcher requirements: `python -m pip install -e . autoresearcher`
- Install all API server requirements: `python -m pip install -r requirements.txt`
- Start the server: `python main.py`

## Using the Plugin

If you have access to ChatGPT plugins and want to give this a spin, make sure you run it locally first. Once the API is running on a local server (this readme assumes it to be running on `localhost:8000`), go to ChatGPT > Plugins > Plugin Store > Develop your own plugin > Enter your website domain: here enter `localhost:8000` and click "Find manifest file".

It should work! 

To ask something of AutoResearcher, here's an example prompt:

```
Please use Autoresearcher to answer the question "What is the current state of phage biobanking?"
```