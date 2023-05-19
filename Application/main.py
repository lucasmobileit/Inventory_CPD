from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando Pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando  view
from view import *

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Criando janela
janela = Tk()
janela.title("Controle de inventário Rohde&Schwarz")
janela.geometry('900x600')
janela.configure(bg='grey92')
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames...
frame_cima = Frame(janela, width=1043, height=50, bg='white', relief=FLAT)
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=1043, height=303, bg='white', pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height=300, bg='white', relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Criando funções -------------------------------------------------------------------------------------------------------------------------------------
global tree


# Função inserir
def inserir():
    global imagem, image_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    modelo = e_model.get()
    serie = e_serial.get()
    valor = e_valor.get()
    data = e_cal.get()
    imagem = image_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos')
            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_serial.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_cal.delete(0, 'end')

    mostrar()


# Função para escolher imagem


# função atualizar
def atualizar():
    global imagem, image_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dict = tree.item(treev_dados)
        treev_lista = treev_dict['values']

        valor = treev_lista[0]  # Com isso irei pegar todo o valor

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_serial.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_cal.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_serial.insert(0, treev_lista[7])
        e_valor.insert(0, treev_lista[6])
        e_cal.insert(0, treev_lista[5])
        image_string = treev_lista[8]

        def update():
            global imagem, image_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            modelo = e_model.get()
            serie = e_serial.get()
            valor = e_valor.get()
            data = e_cal.get()
            imagem = image_string

            if imagem == '':
                imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao, modelo, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Por favor, preencha todos os campos')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_serial.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_cal.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frame_meio, command=update, width=13, text="  Confirmar ".upper(),
                             font=('Bahnschrift 8 bold'), overrelief=RIDGE, bg='green', fg='white')
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')


def deletar():
    try:
        treev_dados = tree.focus()
        treev_dict = tree.item(treev_dados)
        treev_lista = treev_dict['values']

        valor = treev_lista[0]  # Com isso irei pegar todo o valor

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Dados deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')


global imagem, image_string, l_imagem


def escolher_imagem():
    global imagem, image_string, l_imagem

    imagem = fd.askopenfilename()
    image_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_meio, bg='white', image=imagem, fg='blue')
    l_imagem.place(x=700, y=10)


# função para abrir imagem
def ver_imagem():
    global imagem, image_string, l_imagem

    treev_dados = tree.focus()
    treev_dict = tree.item(treev_dados)
    treev_lista = treev_dict['values']

    valor = [int(treev_lista[0])]
    item = ver_item(valor)
    imagem = item[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_meio, image=imagem, bg='white', fg='white')
    l_imagem.place(x=690, y=5)


# Trabalhando no frame_cima--------------------------------------------------------------------------------------------------------------------------

# Abrindo imagem
app_img = Image.open('inventorio.png')
app_img = app_img.resize((42, 42))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Controle de Inventário CPD", width=900, compound=LEFT,
                 relief=RAISED, anchor=NW, font=('Bahnschrift 20 bold'), bg='midnight blue', fg='white')
app_logo.place(x=0, y=0)

# Trabalhando no frame_meio-----------------------------------------------------------------------------------------------------------------------

# Criando entradas
l_nome = Label(frame_meio, text="Nome: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frame_meio, text="Área: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_local.place(x=10, y=40)
e_local = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frame_meio, text="Ativo: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_descricao.place(x=10, y=70)
e_descricao = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(frame_meio, text="Marca/Modelo: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_model.place(x=10, y=100)
e_model = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(frame_meio, text="Data da compra: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_cal.place(x=10, y=130)
e_cal = DateEntry(frame_meio, width=12, Background='dark blue', justify=LEFT, bordewidth=2, year=2023)
e_cal.place(x=130, y=131)

l_valor = Label(frame_meio, text="Valor da compra: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white', fg='black')
l_valor.place(x=10, y=160)
e_valor = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frame_meio, text="Número de série: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white',
                 fg='black')
l_serial.place(x=10, y=190)
e_serial = Entry(frame_meio, width=30, justify=LEFT, relief=SOLID)
e_serial.place(x=130, y=191)

# Criando botões

# Botão carregar:
l_carregar = Label(frame_meio, text="Imagem do item: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg='white',
                   fg='black')
l_carregar.place(x=10, y=220)
b_carregar = Button(frame_meio, command=escolher_imagem, width=29, text="Carregar ".upper(), compound=CENTER,
                    anchor=CENTER, font=('Bahnschrift 8 '), overrelief=RIDGE, bg='white', fg='black')
b_carregar.place(x=130, y=221)

# Botão inserir:
img_add = Image.open('add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frame_meio, image=img_add, command=inserir, width=95, text="  Adicionar ".upper(), compound=LEFT,
                   anchor=NW, font=('Bahnschrift 8 bold'), overrelief=RIDGE, bg='white', fg='black')
b_inserir.place(x=330, y=10)

# Botão atualizar:
img_update = Image.open('refresh.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frame_meio, command=atualizar, image=img_update, width=95, text="  Atualizar ".upper(), compound=LEFT,
                  anchor=NW, font=('Bahnschrift 8 bold'), overrelief=RIDGE, bg='white', fg='black')
b_update.place(x=330, y=50)

# Botão deletar:
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frame_meio, command=deletar, image=img_delete, width=95, text="  Deletar ".upper(), compound=LEFT,
                  anchor=NW, font=('Bahnschrift 8 bold'), overrelief=RIDGE, bg='white', fg='black')
b_delete.place(x=330, y=90)

# Botão Ver Item:
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frame_meio, image=img_item, command=ver_imagem, width=95, text="  Ver Item ".upper(), compound=LEFT,
                anchor=NW, font=('Bahnschrift 8 bold'), overrelief=RIDGE, bg='white', fg='black')
b_item.place(x=330, y=218)

# Labels quantidade total e valores
l_total = Label(frame_meio, text="", width=14, height=2, pady=5, anchor=CENTER, font=('Bahnschrift 17 bold'),
                bg='midnight blue', fg='white')
l_total.place(x=450, y=17)

l_valor_total = Label(frame_meio, text="   Valor total de todos os itens    ", height=1, anchor=NW,
                      font=('Bahnschrift 10 bold'), bg='midnight blue', fg='white')
l_valor_total.place(x=450, y=12)

l_qtd = Label(frame_meio, text="", width=14, height=2, anchor=CENTER, pady=5, font=('Bahnschrift 17 bold'),
              bg='midnight blue', fg='white')
l_qtd.place(x=450, y=90)

l_qtd_ = Label(frame_meio, text="   Quantidade total de itens    ", height=1, anchor=NW, font=('Bahnschrift 10 bold'),
               bg='midnight blue', fg='white')
l_qtd_.place(x=450, y=92)


# tabela -----------------------------------------------------------
def mostrar():
    global tree

    tabela_head = ['#Item', 'Nome', 'Sala/Área', 'Ativo', 'Marca/Modelo', 'Data da compra', 'Valor da compra',
                   'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frame_baixo, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_baixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_baixo.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center", "center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()

janela.mainloop()