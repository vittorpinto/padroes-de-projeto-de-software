from abc import ABC, abstractmethod

# Classe abstrata para leitores de configuração
class ConfigReader(ABC):
    @abstractmethod
    def read_config(self, file_name):
        pass

# Leitor concreto para formato JSON
class JSONConfigReader(ConfigReader):
    def read_config(self, file_name):
        print(f"Lendo arquivo de configuração {file_name} no formato JSON")

# Leitor concreto para formato XML
class XMLConfigReader(ConfigReader):
    def read_config(self, file_name):
        print(f"Lendo arquivo de configuração {file_name} no formato XML")

# Leitor concreto para formato YAML
class YAMLConfigReader(ConfigReader):
    def read_config(self, file_name):
        print(f"Lendo arquivo de configuração {file_name} no formato YAML")

# Classe abstrata para fábrica de leitores de configuração
class ConfigReaderFactory(ABC):
    @abstractmethod
    def create_config_reader(self, file_type):
        pass

# Fábrica concreta que usa o Factory Method para criar o leitor apropriado
class ConcreteConfigReaderFactory(ConfigReaderFactory):
    def create_config_reader(self, file_type):
        if file_type == "json":
            return JSONConfigReader()
        elif file_type == "xml":
            return XMLConfigReader()
        elif file_type == "yaml":
            return YAMLConfigReader()
        else:
            raise ValueError("Tipo de arquivo inválido")

# Função para testar o sistema de leitura de arquivos de configuração
def test_system(factory, file_name, file_type):
    reader = factory.create_config_reader(file_type)
    reader.read_config(file_name)

print("Testando o sistema com diferentes tipos de arquivos de configuração")
factory = ConcreteConfigReaderFactory()
file_names = ["config.json", "config.xml", "config.yaml"]
file_types = ["json", "xml", "yaml"]
for file_name, file_type in zip(file_names, file_types):
    test_system(factory, file_name, file_type)
