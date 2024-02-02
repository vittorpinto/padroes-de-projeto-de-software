# Factory Method

O padrão de projeto Factory Method permite que uma classe delegue a criação de objetos para subclasses, em vez de fazê-lo diretamente. Esse padrão usa uma interface ou uma classe abstrata para definir um método fábrica que retorna um objeto de um determinado tipo. As subclasses podem sobrescrever esse método para retornar diferentes tipos de objetos, de acordo com algum critério. Por exemplo, uma classe de criador de documentos pode criar documentos de diferentes formatos, como PDF, DOCX ou TXT. O padrão Factory Method facilita a extensibilidade, a reutilização e o desacoplamento do código.


- **Exercício 1:** Suponha que você esteja desenvolvendo um sistema de geração de relatórios contábeis para uma empresa. Este sistema deve ser capaz de gerar relatórios financeiros com diferentes níveis de detalhes e formatações (HTML, PDF, Relatorio Simples, Relatorio Completo);
- **Exercício 2:** Crie um sistema de carregamento de documentos;
- **Exercício 3:** Desenvolva um jogo com diferentes tipos de inimigos.
- **Exercício 4:** Implemente um sistema de leitura de arquivos de configuração;
- **Exercício 5:** Construa um sistema de registro de eventos;
- **Exercício 6:** Desenvolva um sistema de geração de relatórios.