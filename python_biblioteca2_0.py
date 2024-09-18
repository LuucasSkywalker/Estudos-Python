class Livro:
    def __init__(self, titulo, autor, genero, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, '
        f' Gênero: {self.genero}, Ano de Publicação: {self.ano_publicacao}'

'''
Criando uma classe filha para adicionar mais alguns atributos   '''
class LivroDetalhado(Livro):
    def __init__(self, titulo, autor, genero, ano_publicacao,
                 quantidade, disponibilidade, nacionalidade):
        super().__init__(titulo, autor, genero, ano_publicacao)
        self.quantidade = quantidade
        self.disponibilidade = disponibilidade
        self.nacionalidade = nacionalidade

    def verificar_disponibilidade(self):
        return self.disponibilidade

    def obter_nacionalidade(self):
        return self.nacionalidade
#------------------------------------------------------ 
    
    livros = []

def cadastrar_livro(titulo, autor, genero, ano_publicacao,
                    quantidade, nacionalidade):
    disponibilidade = 'Disponível' if quantidade > 0 else 'Indisponível'
    novo_livro = LivroDetalhado(titulo, autor, genero, ano_publicacao,
                                quantidade, disponibilidade, nacionalidade)
    livros.append(novo_livro)

#--------------------------------------------------------
cadastrar_livro('Dom Quixote', 'Miguel de Cervantes',
                'Ficção', 1605, 0, 'Espanha')

cadastrar_livro('Orgulho e Preconceito', 'Jane Austen', 'Romance',
                1813, 8, 'Inglaterra')

cadastrar_livro('1984', 'George Orwell', 'Distopia',
                1949, 12, 'Inglaterra')

cadastrar_livro('Cem Anos de Solidão', 'Gabriel Garcia Marquez', 'Realismo Mágico',
                1967, 7, 'Colômbia')

cadastrar_livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', 'Ficção',
                1951, 9, 'Estados Unidos')

#------------------------------------------------------

autor_pesquisa = input('Digite o nome do autor para buscar seus livros: ')
resultados_autor = buscar_livro ('autor', autor_pesquisa)
for livro in resultados_autor:
         print(f'Disponibilidade: {livro.disponibilidade}')
         print(f'Livro encontrado: {livro.titulo}, Autor: {livro.autor}')
         print(f'Quantidade: {livro.quantidade}')
         print(f'Gênero: {livro.genero}, Ano de Publicação: {livro.ano_publicacao}')
         print(f'Nacionalidade: {livro.nacionalidade}')


import matplotlib.pyplot as plt

def grafico():
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

grafico()