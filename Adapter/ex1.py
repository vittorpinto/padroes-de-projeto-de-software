# Usando o padrão de projeto Strategy para separar a lógica de negócio da lógica de apresentação
# Fonte: [Refatorando Python: Dicas e Técnicas para Otimizar Seu Código](https://awari.com.br/refatorando-python-dicas-e-tecnicas-para-otimizar-seu-codigo/)

class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def requisitar(self, estrategia):
        return estrategia.executar()

class Estrategia:
    def __init__(self, descricao):
        self.descricao = descricao

    def executar(self):
        raise NotImplementedError

class EnviarEmail(Estrategia):
    def __init__(self):
        super().__init__("Enviar e-mail")

    def executar(self):
        return f"Executando o serviço: {self.descricao}"

class EnviarSMS(Estrategia):
    def __init__(self):
        super().__init__("Enviar SMS")

    def executar(self):
        return f"Executando o serviço: {self.descricao}"

if __name__ == "__main__":
    cliente = Cliente("Maria")

    email = EnviarEmail()
    sms = EnviarSMS()

    resultado1 = cliente.requisitar(email)
    resultado2 = cliente.requisitar(sms)

    print(resultado1)
    print(resultado2)
