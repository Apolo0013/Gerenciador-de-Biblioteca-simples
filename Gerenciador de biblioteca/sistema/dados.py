import sqlite3


def livro_lista(dados):
    for livro in dados:
        titulo = livro[0]
        autor = livro[1]
        isbn = livro[2]
        editora = livro[3]
        ano = livro[4]
        add_banco(titulo = titulo , autor = autor , isbn = isbn , ano_publicação=ano , editora = editora)


def add_banco(titulo , autor , isbn , editora , ano_publicação , dados = 'livros_disponivel'):
    try:
        cursor.execute(f'INSERT INTO {dados} VALUES ("{titulo}" , "{autor}" , {isbn} , "{editora}" , {ano_publicação} , {True})')

    except sqlite3.Error as error:
        print(f'Desculpe mais nao foi possivel em add os dados: {error}')

    else:
        banco.commit()


def empretismoEdevolução_livros(isbn , ocasião):
    '''
    aqui voce votar o isbn do livro e diz a ocasião:
    true: emprestar
    false: devolver
    '''
    if ocasião:
        try:
            cursor.execute(f'UPDATE livros_disponivel SET Disponivel = {False} WHERE Isbn = "{isbn}"')

        except sqlite3.Error as error:
            print(f'Algo deu errado: {error}')

        else:
            banco.commit()


    else:
        try:
            cursor.execute(f'UPDATE livros_disponivel SET Disponivel = {True} WHERE Isbn = {isbn}')

        except sqlite3.Error as error:
            print(f'Algo de errado: {error}')

        else:
            banco.commit()


def Del_dados(isbn):
    try:
        cursor.execute(f'DELETE FROM livros_disponivel WHERE Isbn == {isbn}')
    except sqlite3.Error as error:
        print(f'Algo de errado ao excluir o isbn: {isbn} ERROR: {error}')
        
    finally:
        banco.commit()


def banco_de_dados():
    try:
        cursor.execute('SELECT * FROM  livros_disponivel')
    except sqlite3.Error as error:
        print(error)
    else:
        banco.commit()
        return  cursor.fetchall()

#banco de dados

banco = sqlite3.connect('Dados_biblioteca.db')

cursor = banco.cursor()

if __name__ == '__main__':
    livros = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0618640157", "HarperCollins", 1954),
    ("1984", "George Orwell", "978-0451524935", "Plume", 1949),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", "978-0316769488", "Little, Brown and Company", 1951),
    ("O Grande Gatsby", "F. Scott Fitzgerald", "978-0743273565", "Scribner", 1925),
    ("Moby Dick", "Herman Melville", "978-1503280786", "CreateSpace Independent Publishing Platform", 1851),
    ("Orgulho e Preconceito", "Jane Austen", "978-1503290563", "CreateSpace Independent Publishing Platform", 1813),
    ("Crime e Castigo", "Fyodor Dostoevsky", "978-0143058144", "Penguin Classics", 1866),
    ("Guerra e Paz", "Leo Tolstoy", "978-0199232765", "Oxford University Press", 1869),
    ("O Conde de Monte Cristo", "Alexandre Dumas", "978-0140449266", "Penguin Classics", 1844),
    ("A Revolução dos Bichos", "George Orwell", "978-0451526342", "Signet Classics", 1945),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-0156012195", "Harcourt, Inc.", 1943),
    ("As Aventuras de Huckleberry Finn", "Mark Twain", "978-0486280615", "Dover Publications", 1884),
    ("Cem Anos de Solidão", "Gabriel Garcia Marquez", "978-0060883287", "Harper Perennial", 1967),
    ("Dom Quixote", "Miguel de Cervantes", "978-0060934347", "Harper Perennial", 1605),
    ("O Morro dos Ventos Uivantes", "Emily Brontë", "978-0141439556", "Penguin Classics", 1847),
    ("Jane Eyre", "Charlotte Brontë", "978-0142437209", "Penguin Classics", 1847),
    ("O Processo", "Franz Kafka", "978-0805210408", "Schocken", 1925),
    ("Os Irmãos Karamazov", "Fyodor Dostoevsky", "978-0374528379", "Farrar, Straus and Giroux", 1880),
    ("Ulisses", "James Joyce", "978-0199535675", "Oxford University Press", 1922),
    ("O Retrato de Dorian Gray", "Oscar Wilde", "978-0141439570", "Penguin Classics", 1890),
    ("Drácula", "Bram Stoker", "978-0486411095", "Dover Publications", 1897),
    ("Frankenstein", "Mary Shelley", "978-0486282114", "Dover Publications", 1818),
    ("Os Miseráveis", "Victor Hugo", "978-0451419439", "Signet Classics", 1862),
    ("Anna Karenina", "Leo Tolstoy", "978-0143035008", "Penguin Classics", 1877),
    ("Odisseia", "Homero", "978-0140268867", "Penguin Classics", -800),
    ("A Ilíada", "Homero", "978-0140275360", "Penguin Classics", -750),
    ("A Divina Comédia", "Dante Alighieri", "978-0140448955", "Penguin Classics", 1320),
    ("O Nome da Rosa", "Umberto Eco", "978-0156001311", "Harcourt, Inc.", 1980),
    ("O Apelo da Selva", "Jack London", "978-0486264724", "Dover Publications", 1903),
    ("Admirável Mundo Novo", "Aldous Huxley", "978-0060850524", "Harper Perennial", 1932),
    ("Fahrenheit 451", "Ray Bradbury", "978-1451673319", "Simon & Schuster", 1953),
    ("Senhor das Moscas", "William Golding", "978-0399501487", "Penguin Books", 1954),
    ("O Sol é Para Todos", "Harper Lee", "978-0061120084", "Harper Perennial", 1960),
    ("O Estrangeiro", "Albert Camus", "978-0679720201", "Vintage", 1942),
    ("Lolita", "Vladimir Nabokov", "978-0679723168", "Vintage", 1955),
    ("A Metamorfose", "Franz Kafka", "978-0553213690", "Bantam Classics", 1915),
    ("O Castelo", "Franz Kafka", "978-0805211061", "Schocken", 1926),
    ("A Máquina do Tempo", "H.G. Wells", "978-0553213515", "Bantam Classics", 1895),
    ("A Ilha do Dr. Moreau", "H.G. Wells", "978-0486290273", "Dover Publications", 1896),
    ("20.000 Léguas Submarinas", "Jules Verne", "978-0486448490", "Dover Publications", 1870),
    ("Viagem ao Centro da Terra", "Jules Verne", "978-0486440883", "Dover Publications", 1864),
    ("A Volta ao Mundo em 80 Dias", "Jules Verne", "978-0486411111", "Dover Publications", 1873),
    ("O Médico e o Monstro", "Robert Louis Stevenson", "978-0486266888", "Dover Publications", 1886),
    ("O Jardim Secreto", "Frances Hodgson Burnett", "978-0486280242", "Dover Publications", 1911),
    ("O Mágico de Oz", "L. Frank Baum", "978-0486291163", "Dover Publications", 1900),
    ("Peter Pan", "J.M. Barrie", "978-0486278072", "Dover Publications", 1911),
    ("Alice no País das Maravilhas", "Lewis Carroll", "978-0486275439", "Dover Publications", 1865),
    ("O Silmarillion", "J.R.R. Tolkien", "978-0618391110", "Mariner Books", 1977),
    ("O Hobbit", "J.R.R. Tolkien", "978-0547928227", "Mariner Books", 1937),
    ("Duna", "Frank Herbert", "978-0441013593", "Ace", 1965),
    ("O Guia do Mochileiro das Galáxias", "Douglas Adams", "978-0345391803", "Del Rey", 1979),
    ("O Código Da Vinci", "Dan Brown", "978-0307474278", "Anchor", 2003),
    ("Anjos e Demônios", "Dan Brown", "978-0743493468", "Atria Books", 2000),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "978-0590353427", "Scholastic", 1997),
    ("Harry Potter e a Câmara Secreta", "J.K. Rowling", "978-0439064873", "Scholastic", 1998),
    ("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", "978-0439136365", "Scholastic", 1999),
    ("Harry Potter e o Cálice de Fogo", "J.K. Rowling", "978-0439139601", "Scholastic", 2000),
    ("Harry Potter e a Ordem da Fênix", "J.K. Rowling", "978-0439358071", "Scholastic", 2003),
    ("Harry Potter e o Enigma do Príncipe", "J.K. Rowling", "978-0439784542", "Scholastic", 2005),
    ("Harry Potter e as Relíquias da Morte", "J.K. Rowling", "978-0545010221", "Scholastic", 2007),
    ("Jogos Vorazes", "Suzanne Collins", "978-0439023481", "Scholastic Press", 2008),
    ("Em Chamas", "Suzanne Collins", "978-0439023498", "Scholastic Press", 2009),
    ("A Esperança", "Suzanne Collins", "978-0439023511", "Scholastic Press", 2010)
    ]
    livro_lista(livros)
    banco.close()