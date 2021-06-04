from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

class ProjetoFinalView:
  
  def __init__(self, root):

    #Colocando elementos
    self.label1 = tk.Label(root, text="Dados Excel", bg='#8dd0f7', height=2, font=('bold'))
    self.entryteste = tk.Entry(root)
    self.labelArquivo = tk.Label(root, bg='#8dd0f7')
    self.botaoCarrega = tk.Button(root, text='Carregar arquivo', bg='#faf6ac')
    self.botaoProcura = tk.Button(root, text='Procurar arquivo', bg='#faf6ac')
    self.label2 = tk.Label(root, text="Adicionar novo item", bg='#8dd0f7', height=2, font=('bold'))
    self.e1 = tk.Entry(root, width=10)
    self.e2 = tk.Entry(root, width=10)
    self.e3 = tk.Entry(root, width=10)
    self.e4 = tk.Entry(root, width=10)
    self.e5 = tk.Entry(root, width=10)
    self.inserir = tk.Button(root, text='Inserir', bg='#faf6ac')
    self.l1 = tk.Label(root, text="Usuário", bg='#8dd0f7')
    self.l2 = tk.Label(root, text="Id produto", bg='#8dd0f7')
    self.l3 = tk.Label(root, text="Categoria produto", bg='#8dd0f7')
    self.l4 = tk.Label(root, text="Valor", bg='#8dd0f7')
    self.l5 = tk.Label(root, text="Estratégia Preço", bg='#8dd0f7')
    self.label3 = tk.Label(root, text="Visualização dos dados", bg='#8dd0f7', height=2, font=('bold'))
    self.b1 = tk.Button(root, text='Gráfico de dispersão', bg='#faf6ac')
    self.b2 = tk.Button(root, text='Diagrama de caixa', bg='#faf6ac')
    self.b3 = tk.Button(root, text='Histograma', bg='#faf6ac')
    self.b4 = tk.Button(root, text='Função de distribuição acumulada', bg='#faf6ac')

    #Colocando tabela
    self.tree = ttk.Treeview(selectmode='browse')
    self.xsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
    #self.ysb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
    self.tree.configure(xscrollcommand=self.xsb.set)
    self.tree["columns"] = ("Transação", "Usuário", "Provedor", "Produto", "Categoria do produto", "Canal", "Valor em conta", "Valor do Serviço", "Data e hora", "Estratégia de Preço", "Fraude")
    self.tree['show'] = 'headings'
    i = 0
    for n in self.tree["columns"]:
      self.tree.heading(i, text=n)
      i = i + 1
    #self.tree.insert("",'end',text="L1",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L2",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L3",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L4",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L5",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L6",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))
    #self.tree.insert("",'end',text="L7",values=("Big1","Best",'1','2','3','4','5','6','7','8','9'))

    #Posicionando elementos
    self.label1.grid(row=0, columnspan=6, sticky='NSEW')
    self.tree.grid(row=1, columnspan=6)
    self.xsb.grid(row=2, columnspan=6,sticky='NSEW')
    self.labelArquivo.grid(row=3, column=0, columnspan=4,sticky='NSEW')
    self.botaoCarrega.grid(row=3, column=4, sticky='EW') 
    self.botaoProcura.grid(row=3, column=5, sticky='EW')
    self.label2.grid(row=4, columnspan=6,sticky='NSEW') 
    self.e1.grid(row=5,column=0,sticky='NSEW')
    self.e2.grid(row=5,column=1,sticky='NSEW')
    self.e3.grid(row=5,column=2,sticky='NSEW')
    self.e4.grid(row=5,column=3,sticky='NSEW')
    self.e5.grid(row=5,column=4,sticky='NSEW')
    self.inserir.grid(row=5,column=5,sticky='EW')
    self.l1.grid(row=6,column=0, sticky='EW')
    self.l2.grid(row=6,column=1, sticky='EW')
    self.l3.grid(row=6,column=2, sticky='EW')
    self.l4.grid(row=6,column=3, sticky='EW')
    self.l5.grid(row=6,column=4, sticky='EW')
    self.label3.grid(row=7, columnspan=6,sticky='NSEW')
    self.b1.grid(row=8,column=0, sticky='EW')
    self.b2.grid(row=8,column=1, sticky='EW')
    self.b3.grid(row=8,column=2, sticky='EW')
    self.b4.grid(row=8,column=3, columnspan=2, sticky='EW')

    #Criando dicionário com botões
    self.buttons = {}
    self.buttons['carrega'] = self.botaoCarrega
    self.buttons['procura'] = self.botaoProcura
    self.buttons['insere'] = self.inserir
    self.buttons['grafico1'] = self.b1
    self.buttons['grafico2'] = self.b2
    self.buttons['grafico3'] = self.b3
    self.buttons['grafico4'] = self.b4
  
  