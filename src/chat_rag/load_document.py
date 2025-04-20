from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, TextLoader


class DocLoader:
    def __init__(self, url = None, path = None):
        self.url = url
        self.path = path
    def load(self):
        if self.url:
            loader_ = WebBaseLoader( web_path = self.url )
        elif self.path:
            loader_ = PyPDFLoader( file_path = self.path, extract_images = False )
        return loader_.load()
