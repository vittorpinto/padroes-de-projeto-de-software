class TV:
    def __init__(self, nome):
        self.nome = nome
        self.ligada = False
        self.volume = 10
        self.entrada = "TV"

    def ligar(self):
        self.ligada = True
        print(f"{self.nome} ligada")

    def desligar(self):
        self.ligada = False
        print(f"{self.nome} desligada")

    def ajustar_volume(self, valor):
        self.volume += valor
        print(f"Volume da {self.nome} ajustado para {self.volume}")

    def escolher_entrada(self, entrada):
        self.entrada = entrada
        print(f"Entrada da {self.nome} escolhida para {self.entrada}")

class SomSurround:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False
        self.volume = 10
        self.entrada = "TV"
        self.modo = "Estereo"

    def ligar(self):
        self.ligado = True
        print(f"{self.nome} ligado")

    def desligar(self):
        self.ligado = False
        print(f"{self.nome} desligado")

    def ajustar_volume(self, valor):
        self.volume += valor
        print(f"Volume do {self.nome} ajustado para {self.volume}")

    def escolher_entrada(self, entrada):
        self.entrada = entrada
        print(f"Entrada do {self.nome} escolhida para {self.entrada}")

    def ligar_modo(self, modo):
        self.modo = modo
        print(f"Modo do {self.nome} ligado para {self.modo}")

class DVD:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False
        self.reproduzindo = False

    def ligar(self):
        self.ligado = True
        print(f"{self.nome} ligado")

    def desligar(self):
        self.ligado = False
        print(f"{self.nome} desligado")

    def reproduzir(self):
        self.reproduzindo = True
        print(f"{self.nome} reproduzindo")

    def parar(self):
        self.reproduzindo = False
        print(f"{self.nome} parado")

class SintonizadorTV:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False
        self.canal = "AR"

    def ligar(self):
        self.ligado = True
        print(f"{self.nome} ligado")

    def desligar(self):
        self.ligado = False
        print(f"{self.nome} desligado")

    def escolher_canal(self, canal):
        self.canal = canal
        print(f"Canal do {self.nome} escolhido para {self.canal}")

class HomeTheater:
    def __init__(self, tv, som, dvd, sintonizador):
        self.tv = tv
        self.som = som
        self.dvd = dvd
        self.sintonizador = sintonizador

    def ligar_home_theater(self):
        print("Ligando o home theater...")
        self.tv.ligar()
        self.som.ligar()
        self.dvd.ligar()
        self.sintonizador.ligar()
        self.tv.escolher_entrada("DVD")
        self.som.escolher_entrada("DVD")
        self.som.ligar_modo("Estereo")
        print("Home theater ligado")

    def desligar_home_theater(self):
        print("Desligando o home theater...")
        self.tv.desligar()
        self.som.desligar()
        self.dvd.desligar()
        self.sintonizador.desligar()
        print("Home theater desligado")

    def assistir_dvd(self):
        print("Assistindo DVD...")
        self.dvd.reproduzir()
        self.tv.ajustar_volume(5)
        self.som.ajustar_volume(5)

    def parar_dvd(self):
        print("Parando DVD...")
        self.dvd.parar()

    def assistir_tv(self):
        print("Assistindo TV...")
        self.tv.escolher_entrada("TV")
        self.som.escolher_entrada("TV")
        self.sintonizador.escolher_canal("Cabo")
        self.tv.ajustar_volume(10)
        self.som.ajustar_volume(10)

if __name__ == "__main__":
    tv = TV("Samsung")
    som = SomSurround("LG")
    dvd = DVD("Sony")
    sintonizador = SintonizadorTV("Philips")

    home_theater = HomeTheater(tv, som, dvd, sintonizador)

    home_theater.ligar_home_theater()
    home_theater.assistir_dvd()
    home_theater.parar_dvd()
    home_theater.assistir_tv()
    home_theater.desligar_home_theater()
