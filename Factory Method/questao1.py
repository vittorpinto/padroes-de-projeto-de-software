from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def load(self):
        pass

class PDFDocument(Document):
    def load(self):
        print("Carregando um documento PDF")

class WordDocument(Document):
    def load(self):
        print("Carregando um documento Word")

class HTMLDocument(Document):
    def load(self):
        print("Carregando um documento HTML")

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, file_type):
        pass

class ConcreteDocumentFactory(DocumentFactory):
    def create_document(self, file_type):
        if file_type == "pdf":
            return PDFDocument()
        elif file_type == "word":
            return WordDocument()
        elif file_type == "html":
            return HTMLDocument()
        else:
            raise ValueError("Tipo de arquivo inválido")

def test_document_loading(factory, file_type):
    document = factory.create_document(file_type)
    document.load()

print("Testando o sistema de carregamento de documentos")
factory = ConcreteDocumentFactory()
file_types = ["pdf", "word", "html"]
for file_type in file_types:
    test_document_loading(factory, file_type)
