from tkinter import *
from tkinter.ttk import Treeview , Combobox


class Gui():

    def __init__(self):
        self.janela = Tk()
        self.janela.protocol('WM_DELETE_WINDOW' , self.fechar_janela)
        self.atualizar_banco()
        self.Configuração_Gui()
        self.Frames()
        self.Botões()
        #self.Imagems()
        self.Labels()
        self.Entradas()
        self.Tabela()
        self.Combobox()
        self.janela.mainloop()


    def fechar_janela(self):
        from tkinter import messagebox

        janela = messagebox.askquestion('Fechando Programa','Você tem certeza se que fechar o programa?')
        print(janela)
        if janela == 'yes':
            from dados import banco
            self.janela.destroy()
            banco.commit()
            banco.close()


    def atualizar_banco(self):
        from .dados import banco_de_dados
        return banco_de_dados()


    
    def Configuração_Gui(self):
        self.janela.title('Gerenciador de Biblioteca')
        self.janela.geometry('800x600')
        self.janela.iconphoto(False , PhotoImage(file = 'sistema\\imagens\\livro.png'))
        self.janela.config(bg = '#C4C4C4')
        self.janela.resizable(width=False , height = False)


    def Frames(self):
        self.frame_titulo = Frame(self.janela , bg = '#0E85B0' , height=80 , width = 800)
        self.frame_titulo.place(x = 0 , y = 0)

        frame_tabela = Frame(self.janela , width = 780 , height = 300 , bg = '#0096A6')
        frame_tabela.place(x = 10 , y = 300)

        frame_opcao = Frame(self.janela , width = 390 , height = 140 , bg = '#018588')
        frame_opcao.place(x = 440 , y = 147 )

    
    def Imagems(self):
        pass


    def Labels(self):
        # label do titulo
        label_titulo = Label(self.janela , width = 20 , height=1 , text = 'Gerenciador de Biblioteca' , font = 'Arial 35 bold' , relief='flat' , bg = '#0E85B0' , fg = '#E1E1E1')
        label_titulo.place(x = 10 , y = 10)

        #Label de orientação da pesquisa
        label_pesquisa = Label(self.janela , width = 8 , height = 1 , text = 'Pesquisa' , relief = 'flat' , font = self.fonte , bg = '#C4C4C4')
        label_pesquisa.place(x = 10 , y = 155)

        #Orientação as opcoes
        label_oriOP = Label(self.janela, width=25 , height=1 , text = 'Classificar tabela por ondem' ,font = 'Arial 15 bold' , bg = '#018588' , relief = 'flat' , anchor='w')
        label_oriOP.place(x = 470 , y = 150)

        #orietar a opcao bna pesquisa
        label_oripes = Label(self.janela , width = 10 , height = 1  , text = 'Pesquisa por', font = 'Arial 12 bold' , bg = '#C4C4C4')
        label_oripes.place(x = 15 , y = 230)

        #aviso de pesquisa
        self.label_avisoPesquisa = Label(self.janela , width = 51 , height = 1 , font = 'Arial 10 bold' , bg = '#C4C4C4' , fg = '#BB0C00' , relief = 'flat' , anchor = 'w' , text = '')
        self.label_avisoPesquisa.place(x = 13 , y = 205)

    
    def Entradas(self):
        self.pesquisa_tabela = Entry(self.janela , width=30 , relief='solid' , font = 'Arial 10 bold' , validate='none')
        self.pesquisa_tabela.place(x = 10 , y = 180)


    def Botões(self):
        self.fonte = 'Arial 12 bold'
        # botao para add livro ao banco de dados se lokp manjo demais pae kkkkk
        botao_addLivros = Button(self.janela , width = 17 , height = 1 , text = 'Adicionar Livro' , relief='flat' , bg = '#32B10E' , font = self.fonte , command= self.pegarDados_livro)
        botao_addLivros.place(x = 10 , y = 100)

        # Botao para retirar um livro do banco de dados, ou seja retirar um livro fds
        botao_removerLivro = Button(self.janela , width = 17 , height = 1 , text ='Remover Livro' , relief = 'flat' , bg = '#C52100' , font = self.fonte , command = self.remover_livro)
        botao_removerLivro.place(x  = 210 , y = 100)

        # Botao para empresta livro para um usuario
        botao_empresta = Button(self.janela , width = 17 , height = 1 , text = 'Emprestimo Livro' , relief = 'flat' , bg = '#C5BE2B' , font = self.fonte , command = self.EmpretismoLivro)
        botao_empresta.place(x = 410 , y = 100)

        # Botao para devolver o livro
        botao_devolverLivro = Button(self.janela , width = 17 , height = 1 , text = 'Devolução Livro' , relief='flat' , bg = '#006D2C' , font = self.fonte , command = self.devoulucao)
        botao_devolverLivro.place(x = 610 , y = 100)

        #imagem = PhotoImage(file = 'sistema\\imagens\\lupa.png')
        
        # Botao para confirmar a pesquisa
        botao_confirmar = Button(self.janela ,  height = 1 , width = 15 , text = 'Confirmar' , relief = 'flat' , bg = '#1D1DC2' , font = 'Arial 10 bold' , command = self.Pesquisa)
        botao_confirmar.place(x = 230 , y= 175)

        #confirmar e ordenar a tabela
        botao_ondernar = Button(self.janela , width = 15 , height= 1 , text = 'Ondenar' , bg = '#006892' , relief = 'flat' , font = self.fonte , command = self.Ondenar)
        botao_ondernar.place(x = 540 , y = 215)

        botao_reniciarTabela = Button(self.janela , width = 10 , height = 1 , text = 'Reniciar' , bg = '#006892' , relief = 'solid' , font = self.fonte , command = self.atualizar_tabela)
        botao_reniciarTabela.place(x = 445 , y = 250)


    def Combobox(self):
        self.style.configure('TCombobox' , font = ('Arial' , 12 , 'bold'))

        #Pesquisa por
        self.opcao_pesquisa = Combobox(self.janela , width =20 , style='TCombobox')
        self.opcao_pesquisa['values'] = ('Titulo' , 'Autor' , 'Editora' , 'Ano')
        self.opcao_pesquisa.current(0)
        self.opcao_pesquisa.place(x = 15 , y = 255)
        
        #classificar tabelas
        self.opcao_classi = Combobox(self.janela , width = 20)
        self.opcao_classi['values'] = ('A-Z','Z-A')
        self.opcao_classi.current(0)
        self.opcao_classi.place(x = 460 , y = 190)

        #classificar tabela por
        self.opcao_por = Combobox(self.janela , width = 20)
        self.opcao_por['values'] = ('Titulo','Autor','Editora')
        self.opcao_por.current(0)
        self.opcao_por.place(x = 630 , y = 190)



    def Tabela(self):
        from tkinter.ttk import Style

        self.tabela = Treeview(self.janela , columns=('titulo' , 'autor' , 'isbn' , 'editora' , 'ano' , 'disponivel') , show = 'headings')

        self.style = Style()
        self.style.configure('Treeview' ,  font = ('Arial' ,10 , 'bold' , ))
        self.style.configure('Treeview.Heading' , font = ('Arial' , 10 ,'bold'))

        self.tabela.heading('titulo' , text = 'Titulo')
        self.tabela.heading('autor' , text = 'Autor')
        self.tabela.heading('isbn' , text = 'Isbn')
        self.tabela.heading('editora' , text = 'Editora')
        self.tabela.heading('ano' , text = 'Ano')
        self.tabela.heading('disponivel' , text = 'Disponivel')


        self.tabela.column('titulo' ,width = 150)
        self.tabela.column('autor' ,width = 150)
        self.tabela.column('isbn' ,width = 120)
        self.tabela.column('editora' ,width = 150)
        self.tabela.column('ano' ,width = 70)
        self.tabela.column('disponivel' ,width = 100)

        self.tabela.place(x = 20 , y = 320 , height= 270 , width = 760)


        self.atualizar_tabela()


    def Limpar_tabela(self):
        for valor in self.tabela.get_children():
            self.tabela.delete(valor)


    def atualizar_tabela(self):
        self.Limpar_tabela()

        if len(self.atualizar_banco()) != 0:
            for linha in self.atualizar_banco():
                if linha[5] == 1:
                    situação = 'Sim'
            
                else:
                    situação = 'Não'
                self.tabela.insert('' , 'end' ,  values = (linha[0] , linha[1] , linha[2] , linha[3] , linha[4] , situação))
            self.tabela.update()


    # Funcoes que irão da fucionalidade ao mesmo

    def devoulucao(self):
        self.janela.withdraw()

        def validação_isbn(action , valor):
            if action == '1':
                if len(valor) > 13:
                    return False
                
                if not valor.isdigit():
                    return False
            
            return True


        def voltar():
            self.janela.deiconify()
            self.janela_devol.destroy()

        cor = '#C4C4C4'

        self.janela_devol = Toplevel()
        self.janela_devol.title('Emprestar Livro')
        self.janela_devol.iconphoto(False , PhotoImage(file = 'sistema\\imagens\\livro.png'))
        self.janela_devol.config(bg = '#C4C4C4')
        self.janela_devol.geometry('310x240')
        self.janela_devol.resizable(width = False , height = False)


        cmdisbn = (self.janela_devol.register(validação_isbn) , '%d' , '%P')

        #label e frame do titulo
        #frame do titulo
        frame_titulo = Frame(self.janela_devol , width = 350 , height = 60 , bg = '#0E85B0')
        frame_titulo.place(x = 0 , y = 0)

        #label do titulo
        label_titulo = Label(self.janela_devol , width = 15 , height = 1 , font = 'Arial 20 bold' , text = 'Devolução do Livro' , relief = 'flat' , bg = '#0E85B0')
        label_titulo.place(x = 10 , y = 10)

        #botao de voltar
        botao_voltar = Button(self.janela_devol , width = 8 , height = 1 , font = self.fonte , text = 'Voltar' ,relief = 'solid' , bg = cor , command = voltar)
        botao_voltar.place(x = 210 , y = 70)
    

        #label e entrada
        label_orienta = Label(self.janela_devol , width = 25 , height = 1 , font = 'Arial 12 bold' , relief = 'flat' , text = 'Digite o Isbn do livro desejado' , bg= cor)
        label_orienta.place(x = 5 , y =110)

        #entrada e botao de confirmar a devolucao
        self.entrada_isbnD = Entry(self.janela_devol , width = 15 , font = 'Arial 10 bold' , validate='key' , validatecommand=cmdisbn)
        self.entrada_isbnD.place(x = 10 , y = 140)

        #label avisando o campo
        self.aviso_label = Label(self.janela_devol , width = 1 , height =1 , text = '' , font = 'Arial 9 bold' , bg = cor , fg = '#BB0C00' , relief = 'flat')
        self.aviso_label.place(x = 120 , y = 135)

        self.aviso_campoV = Label(self.janela_devol , width = 33 , height = 1 , text = '' , font = 'Arial 9 bold' , fg = '#BB0C00',bg = cor , relief = 'flat' , anchor = 'w')
        self.aviso_campoV.place(x = 10 , y =170)

        #botao de confirmar a devolução
        botao_confirmar = Button(self.janela_devol , width = 15 , height = 1 , text = 'Devolver' , relief = 'solid' , bg = '#1D1DC2' , font = self.fonte , anchor= 'center' , command = self.Devolução)
        botao_confirmar.place(x = 10 , y = 190)


    def EmpretismoLivro(self):
        self.janela.withdraw()

        def validação_isbn(action , valor):
            if action == '1':
                if len(valor) > 13:
                    return False
                
                if not valor.isdigit():
                    return False
            
            return True

        def voltar():
            self.janela_emprestimo.destroy()
            self.janela.deiconify()


        self.janela_emprestimo = Toplevel()
        self.janela_emprestimo.title('Emprestar Livro')
        self.janela_emprestimo.iconphoto(False , PhotoImage(file = 'sistema\\imagens\\livro.png'))
        self.janela_emprestimo.config(bg = '#C4C4C4')
        self.janela_emprestimo.geometry('310x240')
        self.janela_emprestimo.resizable(width = False , height = False)

        cor = '#C4C4C4'
        cmdisbn = (self.janela_emprestimo.register(validação_isbn) , '%d' , '%P')
        
        #label e frame do titulo
        frame_titulo = Frame(self.janela_emprestimo , width=340 , height= 60 , bg = '#0E85B0')
        frame_titulo.place(x = 0 , y = 0)

        label_titulo = Label(self.janela_emprestimo , width = 17 , height = 1 , text = 'Empretismo de Livro' , relief = 'flat' , font = 'Arial 20  bold' , bg = '#0E85B0')
        label_titulo.place(x = 5 , y = 10)

        #botao de voltar
        botao_voltar = Button(self.janela_emprestimo , width = 8 , height = 1 ,text = 'Voltar' ,  font = self.fonte , relief = 'solid' , bg = cor , command = voltar)
        botao_voltar.place(x = 210 , y = 70)

        #entrada e botao
        #LABEl para orienta o usuario
        label_orientando = Label(self.janela_emprestimo , width = 30 , height = 1 , font = 'Arial 12 bold' ,text = 'Digite o Isbn do livro que você deseja.' , bg = cor , relief='flat')
        label_orientando.place(x = 5 , y = 110)

        #entrada do isbn para intentificar o livro para emprestar o mesmo>:)
        self.entrada_isbnEmprestimo = Entry(self.janela_emprestimo , width = 15 , font = 'Arial 10 bold' , validate='key', validatecommand=cmdisbn)
        self.entrada_isbnEmprestimo.place(x = 15 , y = 145)

        #endicando que o bagulho ta vazio
        self.label_errorCarac = Label(self.janela_emprestimo , width = 1 , height = 1 , text = '' , bg = cor, fg = '#BB0C00' , relief = 'flat' , font = 'Arial 10  bold')
        self.label_errorCarac.place(x = 125 , y = 140)

        #avisando oq ah de errado.
        self.label_avisoCampo = Label(self.janela_emprestimo , width =20 , height = 1 , text = '' , relief='flat' , font = 'Arial 9 bold' , bg = cor , fg = '#BB0C00')
        self.label_avisoCampo.place(x = 5 , y = 170)

        botao_emprestar = Button(self.janela_emprestimo , width = 10 , height = 1 , text = 'Emprestar' , relief = 'flat' , font = 'Arial 13 bold' , bg ='#1D1DC2' , command = self.Emprestar)
        botao_emprestar.place(x = 15 , y = 190)
        


    #a interface grafica para pegar os dados do livro pra remover o mesmo
    def remover_livro(self):
        self.janela.withdraw() # esconde a janela

        #valida caracteres o tamanho no caso
        def valida_isbn(action  , valor):
            if action == '1':    
                if len(valor) > 13:
                    return False
                
                if not valor.isdigit():
                    return False
            return True


        def voltar():
            self.janela.deiconify()
            self.janela_removerl.destroy()


        self.janela_removerl = Toplevel()
        self.janela_removerl.title('Remover Livro')
        self.janela_removerl.iconphoto(False , PhotoImage(file = 'sistema\\imagens\\livro.png'))
        self.janela_removerl.config(bg = '#C4C4C4')
        self.janela_removerl.geometry('280x220')
        self.janela_removerl.resizable(width = False , height = False)

        cmdisbn = (self.janela_removerl.register(valida_isbn), '%d' , '%P')

        #titulo da janela
        frame_titulo = Frame(self.janela_removerl , width = 300 , height = 60 , bg = '#0E85B0')
        frame_titulo.place(x = 0 , y = 0)

        label_titulo = Label(self.janela_removerl , width = 15 , height = 1 , text = 'Removendo Livro' , relief = 'flat' , font = 'Arial 20 bold' , bg = '#0E85B0')
        label_titulo.place(x = 10 , y = 10)

        #entrada e label para remover o livro do banco de dados
        
        #botao de voltar
        botao_voltar = Button(self.janela_removerl , width = 8 , height = 1 , text = 'Voltar' , relief = 'solid' , font = self.fonte , bg = '#C4C4C4' , command = voltar)
        botao_voltar.place(x = 180 , y = 65)

        #label para indicar o valor
        texto = '''Digite a isbn do Livro para deletar'''

        label_isbn = Label(self.janela_removerl , width = 25 , height = 1 , text = texto , relief = 'flat' , bg = '#C4C4C4' , font = 'Arial 12 bold')
        label_isbn.place(x = 5 , y = 100)

        #entrada do valor
        self.entrada2_isbn = Entry(self.janela_removerl , width = 14 , font = 'Arial 10 bold' , relief = 'solid' , validate='key' , validatecommand=cmdisbn)
        self.entrada2_isbn.place(x = 10 , y = 130)

        #aviso de compo vazio
        self.label_aviso = Label(self.janela_removerl ,  width = 1 , height = 1, text = '' , font = 'Arial 10  bold' , relief = 'flat' , bg = '#C4C4C4' , fg = '#BB0C00')
        self.label_aviso.place(x = 114 , y = 120)

        #orientando o campo vazio
        self.label_orientandoAviso = Label(self.janela_removerl , width = 15 , height = 1 ,  text = '' , relief = 'flat' , font = 'Arial 9 bold' , bg = '#C4C4C4' , fg = '#BB0C00')
        self.label_orientandoAviso.place(x = 10 , y = 150)

        #deletar
        botao_deletar = Button(self.janela_removerl , width = 15 ,  height = 1 , text = 'Deletar' , relief = 'flat' , font = 'Arial 13 bold', bg = '#1D1DC2' , command = self.remover)
        botao_deletar.place(x = 10 , y = 170)

    
    #pegar os dados do livro e botar no banco de dados, a interface grafica
    def pegarDados_livro(self):
        '''
        aqui pegaremos os dados do livro adicionamos no banco de dados
        '''
        self.janela.withdraw()


        def valida_isbn(action , valor):

            if action == '1':    
                if len(valor) > 13:
                    return False

                if not valor.isdigit():
                    return False
            return True


        def valida_ano(action, value_if_allowed):   
            if action == '1':
                # Verifica se o valor inserido é numérico
                if not value_if_allowed.isdigit():
                    return False
                # Verifica se o comprimento do texto não excede o máximo permitido
                if len(value_if_allowed) > 4:
                    return False
            return True


        def voltar():
            self.add_livro.destroy()
            self.janela.deiconify()


        self.add_livro = Toplevel()
        self.add_livro.title('Adicionar Livro')
        self.add_livro.geometry('310x400')
        self.add_livro.iconphoto(False , PhotoImage(file = 'sistema\\imagens\\livro.png'))
        self.add_livro.config(bg = '#C4C4C4')
        self.add_livro.resizable(width=False , height = False)

        #  aqui sao os limitados de caracteres
        cmdisbn = (self.add_livro.register(valida_isbn), '%d' , '%P') # limitar a entrada do isbn
        cmdano = (self.add_livro.register(valida_ano) , '%d' , '%P') # limitar a entrada do ano

        fonte = 'Arial 10 bold' # a fonte para as entradas
        fonte_cupom = 'Arial 13 bold'
        cor_c = '#BB0C00'

        #Frames
        # Titulo
        frame_titulo = Frame(self.add_livro , width = 310 , height = 60 , bg = '#0E85B0')
        frame_titulo.place(x = 0 , y = 0)

        #botao de voltar
        botao_voltar = Button(self.add_livro , width = 8 , height = 1 ,  text = 'Voltar' ,  bg = '#C4C4C4' , font = self.fonte , relief = 'solid' , command = voltar)
        botao_voltar.place(x = 210 , y = 70)

        #Label
        #label do titulo de exbir que fica la em cima dizendo do que a pagina se tratar
        label_titulo = Label(self.add_livro , width = 12 , height = 1 , text = 'Adicionar Livro' , relief = 'flat' , font = 'Arial 20 bold' , bg = '#0E85B0')
        label_titulo.place(x = 10 , y = 10)

        #entradas e labels
        #label e entrada do titulo
        # label para indincar o valor que a entrada vai valer.
        self.label_titulol = Label(self.add_livro , width  = 7 , height = 1 , text = '*Titulo' , relief = 'flat' , font = self.fonte , bg = '#C4C4C4')
        self.label_titulol.place(x = 5 , y = 90)

        #entrada para inserir o titulo
        self.entrada_titulo = Entry(self.add_livro , width = 30 , relief = 'solid', font=fonte)
        self.entrada_titulo.place(x = 5 , y = 115)

        #cupom obrigatorio do titulo
        self.aviso_cupomT = Label(self.add_livro , width = 1 , height = 1 , text = '' ,bg = '#C4C4C4' , relief = 'flat' , font = fonte_cupom , fg = cor_c)
        self.aviso_cupomT.place(x = 220 , y = 110)

        #label e entrada do autor
        #label indicar o valor da entrada
        label_autor = Label(self.add_livro ,width = 5 , height = 1 , text = '*Autor', relief = 'flat' , font = self.fonte , bg = '#C4C4C4')
        label_autor.place(x = 13 , y = 140)
        
        #entrada para inserir o valor
        self.entrada_autor = Entry(self.add_livro , width = 25 , font = fonte , relief = 'solid')
        self.entrada_autor.place(x = 5 , y = 165)

        #cupom obrigatorio do autor
        self.aviso_cupomA = Label(self.add_livro , width = 1, height = 1 , text = '' , bg = '#C4C4C4' , fg = cor_c , font = fonte_cupom)
        self.aviso_cupomA.place(x = 185 , y = 160)

        #label e entrada isbn

        # label indincado o valor da entrada
        label_isbn = Label(self.add_livro , width = 5 , height = 1, text = '*Isbn' , relief = 'flat' , bg = '#C4C4C4' , font = self.fonte)
        label_isbn.place(x = 13 , y = 190)
        
        #ondem o valor se inserido
        self.entrada_isbn = Entry(self.add_livro , width = 15 ,font = fonte , relief = 'solid' , validate='key' , validatecommand=cmdisbn)
        self.entrada_isbn.place(x = 5 , y = 215)

        #cupom indicando que aquela entrada é abrigatorio
        self.aviso_cupomI = Label(self.add_livro , width = 1 , height = 1 , text = '' , fg = cor_c , bg = '#C4C4C4'  , relief = 'flat' , font = fonte_cupom)
        self.aviso_cupomI.place(x = 115 , y = 210)

        #Label e entrada da editora

        # label indicando o valor da entrada
        label_editora = Label(self.add_livro , width = 8 , height = 1 , font = self.fonte , relief = 'flat' , text = '*Editora', bg = '#C4C4C4')
        label_editora.place(x = 5 , y = 240)

        # ondem sera inserido o valor
        self.entrada_editora = Entry(self.add_livro , width = 25 , font = fonte , relief = 'solid')
        self.entrada_editora.place(x = 5 , y = 265)

        self.aviso_cupomE = Label(self.add_livro , width = 1 , height = 1 , text = '' , bg = '#C4C4C4' , fg = cor_c , font = fonte_cupom , relief = 'flat')
        self.aviso_cupomE.place(x = 185 , y = 260)

        # Label e entrada do ano de publicação do livro
        label_ano = Label(self.add_livro , width = 6 , height = 1 , text = '*Ano' , font = self.fonte , relief = 'flat' , bg = '#C4C4C4')
        label_ano.place(x = 10 , y = 290)

        self.entrada_ano = Entry(self.add_livro , width = 4 , font = fonte , relief = 'solid' , validate='key' , validatecommand=cmdano)
        self.entrada_ano.place(x = 5  , y = 315)
        self.aviso_cupomAno = Label(self.add_livro , width  = 1 , height = 1 , text = '' , font = fonte_cupom , fg = cor_c , bg = '#C4C4C4' , relief = 'flat')
        self.aviso_cupomAno.place(x = 40 , y = 310)

        #botao de confirmar as informações
        self.label_atencao = Label(self.add_livro ,  width = 25 , height = 1 , text = '' , relief = 'flat' , font = 'Arial 8 bold' , bg = '#C4C4C4' , fg = 'Red')
        self.label_atencao.place(x = 10 , y = 340)

        botao_confirmarInfo = Button(self.add_livro , width  = 13 , height = 1 , text = 'Confirmar' , relief = 'flat' , bg = '#1D1DC2' , font = self.fonte , command = self.add_livroDados)
        botao_confirmarInfo.place(x = 15 , y = 360)

        #Defs para adicionar os dados e etc.

    def add_livroDados(self):
        '''
        essa funcao vai trabalha em conjunto a 'pegarDados_livro' adicionando os dados ao banco e tratamento de error
        '''
        from fucionalidades import Livros

        titulo = self.entrada_titulo.get().strip()
        autor = self.entrada_autor.get().strip()
        isbn = self.entrada_isbn.get().strip()
        editora = self.entrada_editora.get().strip()
        ano = self.entrada_ano.get().strip()

        #incação de campos nao preenchidos

        if titulo != '':
            self.aviso_cupomT['text'] = ''
        
        if autor != '':
            self.aviso_cupomA['text'] = ''

        if isbn != '':
            self.aviso_cupomI['text'] = ''

        if editora != '':
            self.aviso_cupomE['text'] = ''

        if ano != '':
            self.aviso_cupomAno['text'] = ''

        if titulo != '' and autor != '' and isbn != '' and editora != '' and ano != '' and len(ano) == 4 and len(isbn) == 13:
            self.error = False 
            self.label_atencao['text'] = ''
            self.entrada_ano.delete(0 , END)
            self.entrada_autor.delete(0 , END)
            self.entrada_titulo.delete(0 , END)
            self.entrada_editora.delete(0 , END)
            self.entrada_isbn.delete(0 , END)

            self.label_atencao.update()

        else:
            cupom_incompleto = False

            if autor == '':
                self.aviso_cupomA['text'] = '*'
            
            if titulo == '':
                self.aviso_cupomT['text'] = '*'

            if isbn == '':
                self.aviso_cupomI['text'] = '*'

            if ano == '':
                self.aviso_cupomAno['text'] = '*'

            if editora == '':
                self.aviso_cupomE['text'] = '*'

            if len(isbn) < 13:
                self.label_atencao['text'] = '"ISBN" deve ter 13 caracteres'
                cupom_incompleto = True

            if len(ano) < 4:
                self.label_atencao['text'] = '"ANO" deve ter 4 caracteres'

            if not cupom_incompleto:
                self.label_atencao['text'] = '*Preenchar todos os cupom'

            self.label_atencao.update()
            self.error = True

        if self.error == False:
            livro_info = Livros(titulo=titulo , autor = autor , isbn = isbn , editora = editora , ano_publicação = ano)
            livro_info.add_livros()
            self.atualizar_banco()
            self.Limpar_tabela()
            self.atualizar_tabela()
            self.add_livro.destroy()
            self.janela.deiconify()

        
    def remover(self):
        '''
        Esssa funcao trabalhar com a funcao 'remover_livro' ele deletar o mesmo ao banco de dados e faz um tratamento de error.
        '''
        try:
            isbn = int(self.entrada2_isbn.get().strip())
        except ValueError:
            isbn = ''


        if isbn != '':
            self.label_aviso['text'] = ''
            self.label_orientandoAviso['text'] = ''
            self.entrada2_isbn.delete(0 , END)
            error = False

        else:
            self.label_aviso['text'] = '*'
            self.label_orientandoAviso['text'] = '*Campo vazio!!!'
            error = True

        if error == False:
            from tkinter import messagebox

            encontrador = False
            for valor in self.atualizar_banco():
                if valor[2] == isbn:
                    encontrador = True
                    nome_livro = valor[0]

            if encontrador:    
                livro = self.Livros(isbn=isbn)
                livro.Del_livros()
                self.Limpar_tabela()
                self.atualizar_banco()
                messagebox.askokcancel('Aviso' ,f'O livro "{nome_livro}", foi deletado do banco de dados')

            else:
                messagebox.askokcancel('Aviso',f'Não existe isbn, "{isbn}" no nosso banco de dados')
                
            self.atualizar_tabela()

            self.janela.deiconify()
            self.janela_removerl.destroy()


    def Emprestar(self):
        isbn = self.entrada_isbnEmprestimo.get().strip()

        certo = existe = False

        if isbn != '':
            self.label_errorCarac['text'] = ''


        if isbn != '' and len(isbn) == 13:
            self.label_avisoCampo['text'] = ''
            self.label_errorCarac['text'] = ''
            certo = True

        else:
            if len(isbn) < 13:
                self.label_avisoCampo['text'] = 'Complete o "ISBN"!!!'
                self.label_errorCarac['text'] = '*'

            if isbn == '':
                self.label_avisoCampo['text'] = 'Campo vazio!!!'

        if certo:
            from fucionalidades import Livros
            from tkinter import messagebox
            livro = Livros(isbn = isbn)

            livro_emprestado = False

            for valores in self.atualizar_banco():
                if valores[2] == int(isbn):
                    existe = True
                    nome = valores[0]

                if valores[2] == int(isbn) and valores[5] == 0:
                    livro_emprestado = True
                    nome_Dolivro = valores[0]

            if not livro_emprestado:                    
                    if existe:
                        livro.emprestar_livros()
                        self.atualizar_banco()
                        self.Limpar_tabela()
                        self.atualizar_banco()
                        self.atualizar_tabela()
                        messagebox.askokcancel('Aviso' , f'O livro {nome} foi emprestado!!!')
                        self.janela.deiconify()
                        self.janela_emprestimo.destroy()

                    else:
                        tenta = messagebox.askquestion('Livro não foi encontrado!' , f'Não existem nenhum livro para com a isbn: "{isbn}". Tente novamente.')
                
                        if tenta == 'no':
                            self.janela_emprestimo.destroy()
                            self.janela.deiconify()
            else:
                messagebox.askquestion('Aviso' , f'O Livro {nome_Dolivro} esta emprestado, você não pode pegar emprestado:(')


    def Devolução(self):
        isbn = self.entrada_isbnD.get()
        campo_pre = campo_completo = certo = None

        if len(isbn) == 0:
            self.aviso_campoV['text'] = 'Campo Vazio!!!'
            self.aviso_label['text'] = '*'
            campo_pre = False

        if len(isbn) != 0:
            self.aviso_campoV['text'] = ''
            self.aviso_label['text'] = ''
            campo_pre = True

        if len(isbn) < 13 and len(isbn) >= 1:
            self.aviso_campoV['text'] = '"ISBN" esta incompleto, 13 caracteres.'
            self.aviso_label['text'] = '*'
            campo_completo = False

        if len(isbn) == 13:
            self.aviso_campoV['text'] = ''
            self.aviso_label['text'] = ''
            campo_completo = True
        
        if campo_pre and campo_completo:
            certo = True

        if certo:
            from fucionalidades import Livros
            from tkinter import messagebox
            livro = Livros(isbn = isbn)
            existe = nome_Dolivro = livro_emprestado = False
            
            for valores in self.atualizar_banco():
                if valores[2] == int(isbn):
                    nome_Dolivro = valores[0]
                    existe = True

                if valores[5] == 0 and valores[2] == int(isbn):
                    livro_emprestado = True
                    nome_Dolivro = valores[0]


            if livro_emprestado:
                if existe:
                    livro.devolução_livro()
                    self.atualizar_banco()
                    self.Limpar_tabela()
                    self.atualizar_banco()
                    self.atualizar_tabela()
                    self.entrada_isbnD.delete(0 , END)
                    messagebox.askokcancel('Aviso' , f'O "{nome_Dolivro}", foi devolvido!!!')
                    self.janela_devol.destroy()
                    self.janela.deiconify()

                else:
                    tenta = messagebox.askquestion('Aviso' , f'Não existe ISBN "{isbn}". Tente novamente.')

                    if tenta == 'no':
                        self.janela_devol.destroy()
                        self.janela.deiconify()

            else:
                messagebox.askokcancel('Aviso' , f'O Livro {nome_Dolivro} não foi emprestado')
                self.entrada_isbnD.delete(0 ,END)


    def Pesquisa(self):
        opcao = self.opcao_pesquisa.get()
        campo_vazio = False
        #'Titulo' , 'Autor' , 'Editora'

        if opcao == 'Titulo':
            pesquisa = 0

        if opcao == 'Autor':
            pesquisa = 1

        if opcao == 'Editora':
            pesquisa = 3

        if opcao == 'Ano':
            pesquisa = 4

        if len(self.pesquisa_tabela.get()) == 0:
            campo_vazio = True
            self.label_avisoPesquisa['text'] = 'Campo Vazio!!!'

        if pesquisa in (0,1,3,4) and not campo_vazio:
            dados = self.atualizar_banco() # banco de dados
            resultado = False # a variavel responvel por fala 'teve algum resultado na pesquisa'
            pesquisas = [] # ondem irei guardar os resultado da pesquisa
            ondem = 0 # lugar de cochetes
            self.label_avisoPesquisa['text'] = ''

            for valores in dados:
                if str(valores[pesquisa]).lower() == self.pesquisa_tabela.get().lower():
                    resultado = True
                    pesquisas.append([]) # adionando um cochete para pesquisa, do dados
                    for valor in valores:
                        pesquisas[ondem].append(valor)
                    ondem += 1


            if not resultado:
                if pesquisa == 0:
                    self.label_avisoPesquisa['text'] = f'Não tem nenhum livro com o Titulo: {self.pesquisa_tabela.get()}'
                
                elif pesquisa == 1:
                    self.label_avisoPesquisa['text'] = f'Não tem nenhum livro com o Autor: {self.pesquisa_tabela.get()}'

                elif pesquisa == 3:
                    self.label_avisoPesquisa['text'] = f'Não tem nenhum livro com a Editora: {self.pesquisa_tabela.get()}'

                elif pesquisa == 4:
                    self.label_avisoPesquisa['text'] = f'Não tem nenhum livro lançado no ano de {self.pesquisa_tabela.get()}'

                self.label_avisoPesquisa.update()
            else:
                from time import sleep
                self.label_avisoPesquisa['text'] = ''
                self.Limpar_tabela()
                
                if len(pesquisas) != 0:
                    for linha in pesquisas:
                        if linha[5] == 1:
                            situação = 'Sim'
            
                        else:
                            situação = 'Não'
                        self.tabela.insert('' , 'end' ,  values = (linha[0] , linha[1] , linha[2] , linha[3] , linha[4] , situação))
                        sleep(0.1)
            self.janela.update()
            self.pesquisa_tabela['validate'] = 'none'


    def Ondenar(self):
        classifica = self.opcao_classi.get() # 'A-Z','Z-A'
        classi_por = self.opcao_por.get() # 'Titulo','Autor','Editora'
        dados = self.atualizar_banco()
        livros_ondenados = [] # a lista d livro ondenados

        letras_za = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
        letras_az = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        if classi_por == 'Titulo':
            ondenar = 0

        elif classi_por == 'Autor':
            ondenar = 1

        elif classi_por == 'Editora':
            ondenar = 3

        # A a Z
        if classifica == 'A-Z':
            numeros = [] # ondem vai ficar os titulo que começar com numeros
            lugar = 0 # vai colocar cada livro em um cochetes
            lugar_numerico = 0
            while True:
                if len(dados) == 0 or len(letras_az) == 0:
                    break
                
                for index , valores in enumerate(dados):
                    if valores[ondenar][0] not in ('1','2','3','4','5','6','7','8','9'):
                        if valores[ondenar][0].upper() == letras_az[0]:
                            livros_ondenados.append([])
                            for livro in valores:
                                livros_ondenados[lugar].append(livro)
                            del dados[index]
                            lugar+=1

                    else:
                        numeros.append([])
                        for livros in valores:
                            numeros[lugar_numerico].append(livros)
                        lugar_numerico += 1
                        del dados[index]
                del letras_az[0]

            if len(numeros) != 0:
                livros_ondenados+=numeros

        #Z a A
        elif classifica == 'Z-A':
            lugar = 0 # vai colocar cada livro em um cochetes
            lugar_numerico = 0
            numeros = [] # ondem vai ficar os titulo que começar com numeros
            while True:
                if len(dados) == 0 or len(letras_za) == 0:
                    break
                
                for index , valores in enumerate(dados):
                    if valores[ondenar][0] not in ('1','2','3','4','5','6','7','8','9'):
                        if valores[ondenar][0].upper() == letras_za[0]:
                            livros_ondenados.append([])
                            for livros in valores:
                                livros_ondenados[lugar].append(livros)
                            del dados[index]
                            lugar+=1
                    else:
                        numeros.append([])
                        for livros in valores:
                            numeros[lugar_numerico].append(livros)
                        lugar_numerico +=1
                        del dados[index]
                del letras_za[0]
                    
            if len(numeros) != 0:
                livros_ondenados+=numeros

        self.Limpar_tabela()
        if len(livros_ondenados) != 0:
            for linha in livros_ondenados:
                if linha[5] == 1:
                    situação = 'Sim'

                else:
                    situação = 'Não'
                self.tabela.insert('' , 'end' ,  values = (linha[0] , linha[1] , linha[2] , linha[3] , linha[4] , situação))
            self.janela.update()


if __name__ == '__main__':
    Gui()
