from langchain.document_loaders import PyMuPDFLoader

def load_pdf(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()
    return pages