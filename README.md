🎵 Leitor de Músicas em CSV (Python)

Projeto desenvolvido durante o Bootcamp de Análise de Dados da Generation Brasil, com o objetivo de praticar a leitura e manipulação de arquivos CSV utilizando Python.

📌 Objetivo do Projeto

Ler um arquivo musicas.csv contendo informações de músicas — como título, artista, ano, gênero e duração — e exibir cada registro de forma organizada no terminal.

🛠 Tecnologias Utilizadas

Python 3

Módulo padrão csv

Visual Studio Code

📁 Estrutura do Projeto
📦 leitor-musicas-csv
├── funcoes.py
├── main.py
└── musicas.csv

🔹 funcoes.py

Contém a função ler_musicas(), responsável por:

Abrir o arquivo CSV

Ignorar o cabeçalho utilizando next()

Ler os dados linha a linha com csv.reader

Exibir as informações das músicas de forma estruturada no terminal

🔹 main.py

Arquivo principal do projeto, responsável por:

Importar a função ler_musicas

Executar a leitura do arquivo ao rodar o script

🔹 musicas.csv

Arquivo de dados contendo as informações das músicas utilizadas no exercício.

▶️ Como Executar

Certifique-se de ter o Python 3 instalado

Clone este repositório

Execute o arquivo principal:

python main.py
