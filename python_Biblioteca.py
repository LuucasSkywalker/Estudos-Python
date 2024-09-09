class Livro:
    def __init__(self, titulo, autor, genero, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, '
        f' Gênero: {self.genero}, Ano de Publicação: {self.ano_publicacao}'


class LivroDetalhado(Livro):
    def __init__(self, titulo, autor, genero, ano_publicacao,
                 quantidade, disponibilidade, nacionalidade):
        super().__init__(titulo, autor, genero, ano_publicacao)
        self.ano_publicacao = ano_publicacao
        self.quantidade = quantidade
        self.disponibilidade = disponibilidade
        self.nacionalidade = nacionalidade

    def verificar_disponibilidade(self):
        return self.disponibilidade

    def obter_nacionalidade(self):
        return self.nacionalidade

# Inicialize uma lista vazia para armazenar os livros
livros = []

def cadastrar_livro(titulo, autor, genero, ano_publicacao,
                    quantidade, disponibilidade, nacionalidade):
    novo_livro = LivroDetalhado(titulo, autor, genero, ano_publicacao,
                                quantidade, disponibilidade, nacionalidade)
    livros.append(novo_livro)

 # Cadastrar alguns livros específicos
cadastrar_livro('Dom Quixote', 'Miguel de Cervantes',
                'Ficção', 1605, 5, 'Disponível', 'Espanha')

cadastrar_livro('Orgulho e Preconceito', 'Jane Austen', 'Romance',
                1813, 8, 'Disponível', 'Inglaterra')

cadastrar_livro('1984', 'George Orwell', 'Distopia',
                1949, 12, 'Disponível', 'Inglaterra')

cadastrar_livro('Cem Anos de Solidão', 'Gabriel Garcia Marquez', 'Realismo Mágico',
                1967, 7, 'Disponível', 'Colômbia')

cadastrar_livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', 'Ficção',
                1951, 9, 'Disponível', 'Estados Unidos')


'''
def listar_livros():
    for livro in livros:
        print(
    f'Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}, '
    f'Ano de Publicação: {livro.ano_publicacao}, Quantidade: {livro.quantidade}, '
    f'Disponibilidade: {livro.disponibilidade}, Nacionalidade: {livro.nacionalidade}'
)
'''
def buscar_livro(criterio, valor):
    resultados = []
    for livro in livros:
        if (criterio == 'titulo' and livro.titulo.lower() == valor.lower()) or \
           (criterio == 'autor' and livro.autor.lower() == valor.lower()) or \
           (criterio == 'genero' and livro.genero.lower() == valor.lower()) or \
           (criterio == 'ano_publicacao' and livro.ano_publicacao == int(valor)) or \
           (criterio == 'quantidade' and livro.quantidade == int(valor)) or \
           (criterio == 'nacionalidade' and livro.nacionalidade.lower() == valor.lower()):
            resultados.append(livro)
    return resultados

def verificar_disponibilidade(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            return livro.verificar_disponibilidade()
    return 'Livro não encontrado'

# Adicionar input para pesquisar livro por autor
autor_pesquisa = input('Digite o nome do autor para buscar seus livros: ')
resultados_autor = buscar_livro('autor', autor_pesquisa)
for livro in resultados_autor:
         print(f'Livro encontrado: {livro.titulo}, Autor: {livro.autor}')
         print(f'Gênero: {livro.genero}, Ano de Publicação: {livro.ano_publicacao}')
         print(f'Quantidade: {livro.quantidade}, Disponibilidade: {livro.disponibilidade}')
         print(f'Nacionalidade: {livro.nacionalidade}')


import matplotlib.pyplot as plt

def gerar_grafico():
    generos = {}
    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    genero_lista = list(generos.keys())
    quantidades = list(generos.values())

    plt.bar(genero_lista, quantidades)
    plt.xlabel('Ano de Publicação')
    plt.ylabel('Quantidade')
    plt.title('Quantidade de Livros por generos')
    plt.show()

# Listar todos os livros
#listar_livros()


# Verificar a disponibilidade de um livro
disponibilidade = verificar_disponibilidade('')
print(f' {disponibilidade}')

'''
# Buscar livros por título, autor, gênero, quantidade ou nacionalidade
resultados = buscar_livro('autor', 'Miguel de Cervantes')
for livro in resultados:
    print(f'Livro encontrado: {livro.titulo}, Autor: {livro.autor},
     Gênero: {livro.genero}, Ano de Publicação: {livro.ano_publicacao},
      Quantidade: {livro.quantidade}, Disponibilidade: {livro.disponibilidade}, 
      Nacionalidade: {livro.nacionalidade}')
'''
# Gerar o gráfico
gerar_grafico()
