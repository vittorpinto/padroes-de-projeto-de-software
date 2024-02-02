from abc import ABC, abstractmethod

class Relatorio(ABC):
    @abstractmethod
    def gerar(self):
        pass

class RelatorioHTML(Relatorio):
    def gerar(self):
        return "<html><head><title>Relatório Financeiro</title></head><body><h1>Relatório Financeiro</h1><p>Este é um relatório financeiro em HTML.</p></body></html>"

class RelatorioPDF(Relatorio):
    def gerar(self):
        return "%PDF-obj\n<< /Type /Catalog /Pages 2"

class RelatorioSimples(Relatorio):
    def gerar(self):
        return "Relatório Financeiro\nEste é um relatório financeiro simples."

class RelatorioCompleto(Relatorio):
    def gerar(self):
        return "Relatório Financeiro\nEste é um relatório financeiro completo.\nContém os seguintes dados:\n- Receitas\n- Despesas\n- Lucros\n- Perdas\n- Balanço Patrimonial\n- Demonstração de Resultados\n- Fluxo de Caixa"

class FabricaRelatorios(ABC):
    @abstractmethod
    def criar_relatorio(self, tipo):
        pass

class FabricaRelatoriosFinanceiros(FabricaRelatorios):
    def criar_relatorio(self, tipo):
        if tipo == "HTML":
            return RelatorioHTML()
        elif tipo == "PDF":
            return RelatorioPDF()
        elif tipo == "Simples":
            return RelatorioSimples()
        elif tipo == "Completo":
            return RelatorioCompleto()
        else:
            return None

if __name__ == "__main__":
    fabrica = FabricaRelatoriosFinanceiros()

    relatorio_html = fabrica.criar_relatorio("HTML")
    print(relatorio_html.gerar())

    relatorio_pdf = fabrica.criar_relatorio("PDF")
    print(relatorio_pdf.gerar())

    relatorio_simples = fabrica.criar_relatorio("Simples")
    print(relatorio_simples.gerar())

    relatorio_completo = fabrica.criar_relatorio("Completo")
    print(relatorio_completo.gerar())
