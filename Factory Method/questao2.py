from abc import ABC, abstractmethod

class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

class Soldier(Enemy):
    def attack(self):
        print("Atacando com uma arma")

class Monster(Enemy):
    def attack(self):
        print("Atacando com garras e dentes")

class Boss(Enemy):
    def attack(self):
        print("Atacando com poderes especiais")

class EnemyFactory(ABC):
    @abstractmethod
    def create_enemy(self, enemy_type):
        pass

class ConcreteEnemyFactory(EnemyFactory):
    def create_enemy(self, enemy_type):
        if enemy_type == "soldier":
            return Soldier()
        elif enemy_type == "monster":
            return Monster()
        elif enemy_type == "boss":
            return Boss()
        else:
            raise ValueError("Tipo de inimigo inválido")

def test_game(factory, enemy_type):
    enemy = factory.create_enemy(enemy_type)
    enemy.attack()

print("Testando o jogo com diferentes tipos de inimigos")
factory = ConcreteEnemyFactory()
enemy_types = ["soldier", "monster", "boss"]
for enemy_type in enemy_types:
    test_game(factory, enemy_type)
