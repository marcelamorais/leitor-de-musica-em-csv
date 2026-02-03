#para eu ler uma base de dados, preciso importar o módulo que lê.
import csv 

# agora devo dizer onde esta o arquivo. (path)

caminho_arquivo = "leitor-csv-musicas-python/assets/musicas.csv"

#sempre que eu quero criar uma função eu coloco, a instrução "def" + nome da função():
def ler_musicas():
    print("-----LISTA DE MUSICAS-----")
    try: #o comando try serve para o sistema tentar executar uma ou mais instruções, se nao der certo ele exibe uma msg de erro.
         with open(caminho_arquivo,"r",encoding="utf-8") as arquivo_musica:
             # o comando with open() permite que eu abra algo, mas para isso devo informar, onde está, o modo abertura (ler - r; adicionar - a; reescrever -w)
             # NÃO OBRIGATORIO MAS IMPORTANTE - colocar como quer ler (utf-8), e depois "declarar uma variavel" para essa instrução
            leitor = csv.reader(arquivo_musica)
            # chamei um leitor para o sistema, que lê csv e adicionei o metodo reader para ler o arquivo.
            next(leitor)
            # o comando next é para pular a primeira linha do arquivo
            
            # agora quero exibir linha por linha do que o leitor viu
            for cada_linha in leitor:
                if cada_linha:
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    # sempre tenho que falar todos os cabeçalhos do meu arquivo
                    print("Titulo",titulo,"Artista",artista,"Ano",ano,"Genêro",genero,"Duração",duracao_segundos)
    except FileNotFoundError:
        print("Erro")
            
            