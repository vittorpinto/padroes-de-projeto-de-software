from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class PDFReport(Report):
    def generate(self, data):
        print(f"Gerando um relatório PDF com os dados: {data}")

class CSVReport(Report):
    def generate(self, data):
        print(f"Gerando um relatório CSV com os dados: {data}")

class HTMLReport(Report):
    def generate(self, data):
        print(f"Gerando um relatório HTML com os dados: {data}")

class ReportFactory(ABC):
    @abstractmethod
    def create_report(self, report_type):
        pass

class ConcreteReportFactory(ReportFactory):
    def create_report(self, report_type):
        if report_type == "pdf":
            return PDFReport()
        elif report_type == "csv":
            return CSVReport()
        elif report_type == "html":
            return HTMLReport()
        else:
            raise ValueError("Tipo de relatório inválido")

def test_system(factory, report_type, data):
    report = factory.create_report(report_type)
    report.generate(data)

print("Testando o sistema com diferentes tipos de relatórios")
factory = ConcreteReportFactory()
report_types = ["pdf", "csv", "html"]
data = ["Nome,Idade,Profissão", "João,25,Engenheiro", "Maria,30,Médica"]
for report_type in report_types:
    test_system(factory, report_type, data)
