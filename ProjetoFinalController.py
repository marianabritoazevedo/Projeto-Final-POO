#from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from ProjetoFinalModel import *
from datetime import datetime
import matplotlib.pyplot as plt

class ProjetoFinalController:

    def __init__(self):
        self.view = None
        self.root = tk.Tk()
        self.filename=None
        self.df = None

    def inicializa(self, view):
        #self.model = model
        self.view = view

        self.view.buttons['carrega']['command'] = lambda: self.leituraArquivo()
        self.view.buttons['procura']['command'] = lambda: self.browseFiles()
        self.view.buttons['insere']['command'] = lambda: self.insere_dado(self.view.e1, self.view.e2, self.view.e3, self.view.e4, self.view.e5)
        self.view.buttons['grafico1']['command'] = lambda: self.selecionar_dados_dispersao()
        self.view.buttons['grafico2']['command'] = lambda: self.selecionar_dados_boxplot()
        self.view.buttons['grafico3']['command'] = lambda: self.selecionar_dados_histograma()
        self.view.buttons['grafico4']['command'] = lambda: self.selecionar_dados_fda()

    def executa(self):
        self.root.maxsize(width=700, height=800)
        #self.root.geometry('700x700+0+0')
        self.root.resizable(width=0, height=0)
        self.root['bg'] = '#8dd0f7'
        self.root.title("Projeto Final POO")
        self.root.rowconfigure(0, weight=1) #Linha dados excel
        self.root.rowconfigure(1, weight=2) #Linha tabela
        self.root.rowconfigure(2, weight=1) #Linha da barra de rolagem
        self.root.rowconfigure(3, weight=2) #Linha botões
        self.root.rowconfigure(4, weight=1) #Linha adicionar novo item
        self.root.rowconfigure(5, weight=1) #Linha caixas de entrada novos itens
        self.root.rowconfigure(6, weight=2) #Linha textos caixa de entrada
        self.root.rowconfigure(7, weight=1) #Linha visualização de dados 
        self.root.rowconfigure(8, weight=1) #Linha botões
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.mainloop()

    def browseFiles(self):
        #Configurando função para permitir a leitura de arquivos
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("All files","*.*")))
        
        # Mudar conteúdo da labelArquivo
        self.view.labelArquivo.configure(text=filename)
        self.filename=filename
    
    def leituraArquivo(self):
        try:
            if self.filename is None:
                raise ArquivoVazio()
            else:
                extensao_arquivo = str(self.filename[-3] + self.filename[-2] + self.filename[-1])
                if extensao_arquivo != 'csv':
                    raise NotCSV()
            df = pd.read_csv(self.filename)
            self.df = df
            print(self.df)
            data = df.to_numpy().tolist()
            for linha in data:
                self.view.tree.insert("", "end", values=linha)
        except ArquivoVazio:
            tk.messagebox.showerror(title="Arquivo vazio", message="Por favor, selecione um arquivo .csv antes de carregá-lo!")
        except NotCSV:
            tk.messagebox.showwarning(title="Extensão inválida", message="Apenas arquivos do tipo .csv são válidos!")


    def insere_dado(self,e1,e2,e3,e4,e5):
        try:
            usuario = str(e1.get())
            e1.delete(0, "end")
            id_produto = str(e2.get())
            e2.delete(0, "end")
            categoria = str(e3.get())
            e3.delete(0, "end")
            valor = str(e4.get())
            e4.delete(0, "end")
            estrategia = str(e5.get())
            e5.delete(0, "end")
            data_e_hora = datetime.now()
            data_e_hora_ok = data_e_hora.strftime("%d/%m/%Y %H:%M")
            
            cliente = Cliente(usuario, valor)
            produto = Produto(id_produto,valor,estrategia,categoria)
            provedor = SistemaProvedorCanal()
            transacao = Transacao(cliente, produto, provedor, data_e_hora_ok, 0)

            lista_de_colunas= ['Transacao','Usuario','Provedor','Produto','ProdutoCategoria','Canal','ValorEmConta','ValorServico','DataHora','EstrategiaPreco','Fraude']
            pacote_de_transacoes = list()
            dados = Transacao.getData(transacao)
            pacote_de_transacoes.append(dados)
            dfNew = pd.DataFrame(pacote_de_transacoes, columns = lista_de_colunas)
            if self.df is None:
                raise NenhumArquivo() 
            self.df=self.df.append(dfNew,ignore_index=True)
            print(self.df)
            dfNew.to_csv(self.filename, mode='a', header=False, index=False)
            self.view.tree.insert("","0",values=dados)
        except NenhumArquivo:
            tk.messagebox.showwarning(title="Sem arquivo", message="Antes de inserir um dado, carregue um arquivo!")
        

        
    def selecionar_dados_histograma(self):
        df = self.df
        print(self.df)
        colunas = df.columns
        root2 = tk.Tk()

        self.label = tk.Label(root2, text="Colunas do gráfico", bg='#8dd0f7', height=2, font=('bold'))
        self.lista = tk.Listbox(root2, selectmode=tk.MULTIPLE)
        self.botaoOK = tk.Button(root2, text='OK', bg='#faf6ac', command=lambda: self.histograma(df, self.lista.curselection()))
        
        self.label.grid(row=0, column=0)
        self.lista.grid(row=1, column=0)
        self.botaoOK.grid(row=2, column=0)

        for item in colunas:
            self.lista.insert("end", item)
    
    def selecionar_dados_boxplot(self):
        df = self.df
        print(self.df)
        colunas = df.columns
        root2 = tk.Tk()
        
        self.label = tk.Label(root2, text="Colunas do gráfico", bg='#8dd0f7', height=2, font=('bold'))
        self.lista = tk.Listbox(root2, selectmode=tk.MULTIPLE)
        self.botaoOK = tk.Button(root2, text='OK', bg='#faf6ac', command=lambda: self.boxplot(df, self.lista.curselection()))
        
        self.label.grid(row=0, column=0)
        self.lista.grid(row=1, column=0)
        self.botaoOK.grid(row=2, column=0)

        for item in colunas:
            self.lista.insert("end", item)

    def selecionar_dados_fda(self):
        df = self.df
        print(self.df)
        colunas = df.columns
        root2 = tk.Tk()
        
        self.label = tk.Label(root2, text="Colunas do gráfico", bg='#8dd0f7', height=2, font=('bold'))
        self.lista = tk.Listbox(root2, selectmode=tk.MULTIPLE)
        self.botaoOK = tk.Button(root2, text='OK', bg='#faf6ac', command=lambda: self.fda(df, self.lista.curselection()))
        
        self.label.grid(row=0, column=0)
        self.lista.grid(row=1, column=0)
        self.botaoOK.grid(row=2, column=0)

        for item in colunas:
            self.lista.insert("end", item)
    
    def selecionar_dados_dispersao(self):
        df = self.df
        print(self.df)
        colunas = df.columns
        root2 = tk.Tk()
        
        self.label = tk.Label(root2, text="Colunas do gráfico", bg='#8dd0f7', height=2, font=('bold'))
        self.lista = tk.Listbox(root2, selectmode=tk.MULTIPLE)
        self.botaoOK = tk.Button(root2, text='OK', bg='#faf6ac', command=lambda: self.dispersao(df, self.lista.curselection()))
        
        self.label.grid(row=0, column=0)
        self.lista.grid(row=1, column=0)
        self.botaoOK.grid(row=2, column=0)

        for item in colunas:
            self.lista.insert("end", item)

    
    def boxplot(self, df, lista):
        try:
            nova_lista = []
            for i in lista:
                item = self.lista.get(i)
                print(item)
                nova_lista.append(item)
            for i in nova_lista:
                if i == "ProdutoCategoria" or i == "DataHora":
                    raise BoxplotInvalido()
            df.boxplot(column = nova_lista)
            plt.show()
        except BoxplotInvalido:
            tk.messagebox.showwarning(title="Histograma inválido", message="As colunas DataHora e CategoriaProduto não são válidas para montar um diagrama de caixa!")

    def histograma(self, df, lista):
        try:
            nova_lista = []
            for i in lista:
                item = self.lista.get(i)
                print(item)
                nova_lista.append(item)
            for i in nova_lista:
                if i == "ProdutoCategoria" or i == "DataHora":
                    raise HistogramaInvalido()
            df.hist(column = nova_lista)
            plt.show()
        except HistogramaInvalido:
            tk.messagebox.showwarning(title="Diagrama de caixa inválido", message="As colunas DataHora e CategoriaProduto não são válidas para montar um histograma!")
    
    def fda(self, df, lista):
        try:
            nova_lista = []
            for i in lista:
                item = self.lista.get(i)
                print(item)
                nova_lista.append(item)
            for i in nova_lista:
                if i == "ProdutoCategoria" or i == "DataHora":
                    raise FDAInvalida()
            df.hist(column = nova_lista, cumulative=True)
            plt.show()
        except FDAInvalida:
            tk.messagebox.showwarning(title="Função de distribuição acumulada inválida", message="As colunas DataHora e CategoriaProduto não são válidas para montar uma Função de distribuição acumulada!")

    def dispersao(self, df, lista):
        try:
            i = 0
            for item in lista:
                i = i + 1
            if i > 2:
                raise MaisDeDuasColunasDispersao()
            elif i < 2:
                raise UmaColunaDispersao
            coluna1 = lista[0]
            coluna2 = lista[1]
            df.plot.scatter(x=coluna1, y=coluna2)
            plt.show()
        except MaisDeDuasColunasDispersao:
            tk.messagebox.showerror(title="Gráfico de dispersão incorreto", message="Um gráfico de dispersão só pode ter duas colunas selecionadas!")
        except UmaColunaDispersao:
            tk.messagebox.showerror(title="Gráfico de dispersão incorreto", message="Selecione duas colunas para gerar o gráfico de dispersão!")
