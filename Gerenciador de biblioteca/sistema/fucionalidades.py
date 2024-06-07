from dados import *


class Livros():

    '''
    Essa classe, consistem em adicionar livros, retirar, devolver e emprestar.
    '''

    def __init__(self , titulo = None , autor = None , isbn = None, editora = None , ano_publicação = None): # Informaçôes do livro
        self.titulo  = titulo # Titulo do livro
        self.autor = autor # Autor do livro
        self.isbn = isbn # isbn do livro
        self.editora = editora
        self.ano_pu = ano_publicação # ano de publicação do livros

    
    def add_livros(self):
        try:
            add_banco(titulo=self.titulo , autor=self.autor , isbn=self.isbn , editora=self.editora  ,ano_publicação=self.ano_pu)
        except Exception as error:
            print(f'fudeu: {error}')
        
        else:
            print('\033[1;32mprocesso de add dados foi um sucesso\033[m')


    def Del_livros(self):
        try:
            Del_dados(isbn= self.isbn)
        except Exception as error:
            print(f'Fudeu: {error}')
        else:
            print('\033[1;31mGG pae\033[m')


    def emprestar_livros(self):
        try:
            empretismoEdevolução_livros(isbn = self.isbn , ocasião=True ) # aqui ele vai retorna False para a coluna 'Disponivel', ensinuado que o livro foi emeprestado

        except sqlite3.Error as error:
            print(f'algo de errado: {error}')

        else:
            print(f'\033[1;32mGG pae\033[m')


    def devolução_livro(self):
        try:
            empretismoEdevolução_livros(isbn = self.isbn , ocasião=False) # aqui ele vai retorna True para a coluna 'Disponivel', ensinuado que foi devolvido
        
        except sqlite3.Error as error:
            print(f'Algo deu errado: {error}')

        print('\033[1;32mGG pae\033[m')


class Biblioteca():
    def __init__(self):
        pass


if __name__ == '__main__':
    from gui import Gui
    livro = Livros(titulo= 'teste' , autor = 'teste' , isbn= 2133  , editora = 'apolo da foda', ano_publicação = 2009212)
    Gui()