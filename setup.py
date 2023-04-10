from setuptools import setup, find_packages

setup(
    name="auto-researcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "openai",
        "python-dotenv",
        "termcolor",
    ],
    author="Eimen Hamedat",
    author_email="eimen.hamedat@gmail.com",
    description="An auto-researcher tool to create literature reviews using the OpenAI API",
    keywords="aiapi science literature review",
    url="https://github.com/eimenhmdt/autoresearcher",  # Replace with the URL of your GitHub repository or project homepage
)