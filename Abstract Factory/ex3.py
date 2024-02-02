from abc import ABC, abstractmethod

class Foundation(ABC):
    @abstractmethod
    def build(self):
        pass

class Wall(ABC):
    @abstractmethod
    def build(self):
        pass

class Roof(ABC):
    @abstractmethod
    def build(self):
        pass

class HousePartFactory(ABC):
    @abstractmethod
    def create_foundation(self):
        pass

    @abstractmethod
    def create_wall(self):
        pass

    @abstractmethod
    def create_roof(self):
        pass

class ContemporaryFoundation(Foundation):
    def build(self):
        print("Construindo uma fundação no estilo contemporâneo")

class ContemporaryWall(Wall):
    def build(self):
        print("Construindo uma parede no estilo contemporâneo")

class ContemporaryRoof(Roof):
    def build(self):
        print("Construindo um telhado no estilo contemporâneo")

class ContemporaryHousePartFactory(HousePartFactory):
    def create_foundation(self):
        return ContemporaryFoundation()

    def create_wall(self):
        return ContemporaryWall()

    def create_roof(self):
        return ContemporaryRoof()

class ColonialFoundation(Foundation):
    def build(self):
        print("Construindo uma fundação no estilo colonial")

class ColonialWall(Wall):
    def build(self):
        print("Construindo uma parede no estilo colonial")

class ColonialRoof(Roof):
    def build(self):
        print("Construindo um telhado no estilo colonial")

class ColonialHousePartFactory(HousePartFactory):
    def create_foundation(self):
        return ColonialFoundation()

    def create_wall(self):
        return ColonialWall()

    def create_roof(self):
        return ColonialRoof()

def test_house_building(factory):
    foundation = factory.create_foundation()
    wall = factory.create_wall()
    roof = factory.create_roof()
    foundation.build()
    wall.build()
    roof.build()

print("Testando a simulação de construção de casas com o estilo contemporâneo")
contemporary_factory = ContemporaryHousePartFactory()
test_house_building(contemporary_factory)

print("Testando a simulação de construção de casas com o estilo colonial")
colonial_factory = ColonialHousePartFactory()
test_house_building(colonial_factory)
