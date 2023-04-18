from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="autoresearcher",
    version="0.0.6",
    author="Eimen Hamedat",
    author_email="eimen.hamedat@gmail.com",
    description="Automating scientic workflows with AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eimenhmdt/autoresearcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=[
        "openai==0.27.0",
        "python-dotenv==1.0.0",
        "requests==2.26.0",
        "termcolor==1.1.0",
        "jellyfish==0.11.2",
        "tiktoken==0.3.3",
        "faiss-cpu==1.7.3",
        "PyMuPDF==1.22.0",
        "langchain>=0.0.141",
        "setuptools>=42",
        "wheel"
    ],
)
