class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def requisitar(self, comunicacao):
        return comunicacao.enviar()

class Comunicacao:
    def enviar(self):
        raise NotImplementedError

class Adapter(Comunicacao):
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def enviar(self):
        return self.estrategia.executar()

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

    adapter_email = Adapter(email)
    adapter_sms = Adapter(sms)

    resultado1 = cliente.requisitar(adapter_email)
    resultado2 = cliente.requisitar(adapter_sms)

    print(resultado1)
    print(resultado2)
