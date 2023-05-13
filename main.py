import tkinter as tk
import tkinter.ttk as ttk
import tkinter.colorchooser as colorchooser
from tkinter import messagebox
import customtkinter as ctk
from clock import DigitalClock
import datetime
import sqlite3 as sql
import os.path as path

ctk.set_appearance_mode('Light')

class App():

    def __init__(self):

        self.cor1 = '#005353'
        self.cor2 = 'white'
        self.root = ctk.CTk()
        self.root.title('Estacionamento')
        self.root.configure(fg_color=self.cor1)
        self.root.geometry('1150x650+100+20')
        self.root.iconbitmap(bitmap='carro.ico')
        self.fonte1 = ctk.CTkFont(family='Times New Roman', weight='bold', size=23, slant='italic')
        self.fonte2 = ctk.CTkFont(family='Times New Roman', weight='bold', size=20)
        self.frames()
        self.labels()
        self.widgets()
        self.menus()
        self.preenche_treewiew()
        self.eventos_binding()
    def menus(self):

        self.barra_de_menus = tk.Menu(self.root)
        self.menu_patio = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.menu_patio.add_command(label='Pesquisar Veículo')
        self.menu_patio.add_command(label='Fechar Pátio')
        self.barra_de_menus.add_cascade(label='Patio', menu=self.menu_patio)
        self.menu_mensalista = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.menu_mensalista.add_command(label='Adicionar Mensalista', command=self.janela_inserir_mensalista)
        self.menu_mensalista.add_command(label='Excluir Mensalista')
        self.menu_mensalista.add_separator()
        self.menu_mensalista.add_command(label='Tabela de Mensalistas', command=self.janela_gerenciar_mensalista)
        self.barra_de_menus.add_cascade(label='Mensalistas', menu=self.menu_mensalista)
        self.menu_preco = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.menu_preco.add_command(label='Mudar tabela de preços')
        self.menu_preco.add_command(label='Verificar tabela de preços')
        self.menu_usuario = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.barra_de_menus.add_cascade(label='Preços', menu=self.menu_preco)
        self.menu_usuario.add_command(label='Mudar Senha')
        self.menu_usuario.add_command(label='Gerenciar Usuários')
        self.barra_de_menus.add_cascade(label='Usuários', menu=self.menu_usuario)
        self.menu_convenios = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.menu_convenios.add_command(label='Adicionar Conveniado')
        self.menu_convenios.add_command(label='Excluir Conveniado')
        self.menu_convenios.add_separator()
        self.menu_convenios.add_command(label='Gerenciar Convênios')
        self.barra_de_menus.add_cascade(label='Convênios', menu=self.menu_convenios)
        self.menu_config = tk.Menu(master=self.barra_de_menus, tearoff=False)
        self.menu_config.add_command(label='Modificar cor de fundo', command=self.comando_mudar_cor)
        self.barra_de_menus.add_cascade(label='Configurações', menu=self.menu_config)
        self.root.configure(menu=self.barra_de_menus)
    def frames(self):
        self.Frame1 = ctk.CTkTabview(master=self.root)
        self.Frame1.configure(fg_color=self.cor2, bg_color=self.cor1, border_width=3, border_color='black',
                              corner_radius=11)
        self.Frame1.add('Entrada')
        self.Frame1.add('Saida')
        self.Frame1.place(relx=0.02, rely=0.005, relwidth=0.96, relheight=0.495)
        self.frame2 = ctk.CTkFrame(master=self.root)
        self.frame2.configure(fg_color='white', bg_color=self.cor1, border_width=3, border_color='black')
        self.frame2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

        style_treeview_patio = ttk.Style()
        style_treeview_patio.configure("treeview_patio.Treeview", font = ('Arial', 10))
        style_treeview_patio.configure("treeview_patio.Treeview.Headings", background = 'lightgrey')

        self.treewiew = ttk.Treeview(master=self.frame2, columns=('Placa', 'Tipo', 'Marca', 'Cor', 'Hora'), show='headings',
                                     style="treeview_patio.Treeview")
        self.treewiew.tag_configure('myfont', font=('Arial', 15))
        self.treewiew.column('Placa', minwidth=0, width=100, anchor='center')
        self.treewiew.column('Tipo', minwidth=0, width=100, anchor='center')
        self.treewiew.column('Marca', minwidth=0, width=100, anchor='center')
        self.treewiew.column('Cor', minwidth=0, width=100, anchor='center')
        self.treewiew.column('Hora', minwidth=0, width=100, anchor='center')
        self.treewiew.heading('Placa', text='Placa', anchor='center')
        self.treewiew.heading('Tipo', text='Tipo', anchor='center')
        self.treewiew.heading('Marca', text='Marca', anchor='center')
        self.treewiew.heading('Cor', text='Cor', anchor='center')
        self.treewiew.heading('Hora', text='Hora', anchor='center')
        self.yScrollbar = ctk.CTkScrollbar(master=self.treewiew, orientation='vertical',command=self.treewiew.yview)
        self.yScrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.treewiew.configure(yscrollcommand=self.yScrollbar.set)
        self.treewiew.place(relx = 0, rely=0, relheight=1, relwidth=1)
        self.menu_treewiew = tk.Menu(master=self.treewiew, tearoff=False)
        self.menu_treewiew.add_command(label='Efetuar Saída', command=self.comando_menu_treewiew)
        self.menu_treewiew.add_command(label='Alterar Campo', command=self.comando_alterar)
        self.menu_frame1 = tk.Menu(master=self.root, tearoff=False)
        self.menu_frame1.add_command(label='Entrada', command=lambda: self.Frame1.set('Entrada'))
        self.menu_frame1.add_command(label='Saida', command=lambda: self.Frame1.set('Saida'))
    def labels(self):

        self.lb_relogio = tk.Label(master=self.Frame1, background='white', font=("TkTextFont", 40), anchor='center')
        self.lb_relogio.place(relx=0.67, rely=0.09, relwidth=0.32, relheight=0.86)

        self.imagem = tk.PhotoImage(file='entry.png')
        self.lb_auxiliar = tk.Label(master=self.Frame1.tab('Entrada'), image=self.imagem, background='white')
        self.lb_auxiliar.place(relx=0.01, rely=0.09, relwidth=0.26, relheight=0.86)

        self.imagem2 = tk.PhotoImage(file='exit.png')
        self.lb_auxiliar2 = tk.Label(master=self.Frame1.tab('Saida'), image=self.imagem2, background='white')
        self.lb_auxiliar2.place(relx=0.01, rely=0.09, relwidth=0.26, relheight=0.86)
        self.lb_entrada = ctk.CTkLabel(master=self.Frame1.tab('Entrada'))
        self.lb_entrada.configure(text='Entrada de Veículos', fg_color=self.cor2, bg_color=self.cor2,
                                  text_color='Black', font=self.fonte1)
        self.lb_entrada.place(relx=0.42, rely=0.03)
        self.lb_placa = ctk.CTkLabel(master=self.Frame1.tab('Entrada'))
        self.lb_placa.configure(text='Placa: ', font=self.fonte2, fg_color=self.cor2, bg_color=self.cor2,
                                text_color='black')
        self.lb_placa.place(relx=0.29, rely=0.245)

        self.lb_marca = ctk.CTkLabel(master=self.Frame1.tab('Entrada'))
        self.lb_marca.configure(text='Marca:', font=self.fonte2, fg_color=self.cor2, bg_color=self.cor2,
                                text_color='black')
        self.lb_marca.place(relx=0.29, rely=0.47)

        self.lb_saida_veiculo = ctk.CTkLabel(master=self.Frame1.tab('Saida'))
        self.lb_saida_veiculo.configure(text='Saída de Veículo', text_color='black', fg_color=self.cor2,
                                        bg_color=self.cor2, font=self.fonte1)
        self.lb_saida_veiculo.place(relx=0.42, rely=0.03)

        self.lb_placa2 = ctk.CTkLabel(master=self.Frame1.tab('Saida'))
        self.lb_placa2.configure(text='Placa: ', font=self.fonte2, text_color='black', fg_color=self.cor2,
                                 bg_color=self.cor2)
        self.lb_placa2.place(relx=0.29, rely=0.245)

        self.lb_cor = ctk.CTkLabel(master=self.Frame1.tab('Entrada'), anchor='w')
        self.lb_cor.configure(text='Cor: ', font=self.fonte2, text_color='black', fg_color=self.cor2,
                              bg_color=self.cor2)
        self.lb_cor.place(relx=0.5, rely=0.47)

        self.lb_convenio = ctk.CTkLabel(master=self.Frame1.tab('Saida'))
        self.lb_convenio.configure(text='Convênio:', font=self.fonte2, fg_color=self.cor2, bg_color=self.cor2,
                                   anchor='w')
        self.lb_convenio.place(relx=0.265, rely=0.47)
    def widgets(self):
        self.relogio = DigitalClock(tk_widget=self.lb_relogio)

        self.e_placa = ctk.CTkEntry(master=self.Frame1.tab('Entrada'))
        self.e_placa.configure(bg_color=self.cor2, fg_color='white',
                               font=ctk.CTkFont(family='Sans Serif', size=14, weight='bold'))
        self.e_placa.place(relwidth=0.12, relx=0.35, rely=0.23, relheight=0.15)

        self.tipo_veiculo = tk.StringVar()
        self.tipo_veiculo.set('Carro')
        self.radio_moto = ctk.CTkRadioButton(master=self.Frame1.tab('Entrada'), variable=self.tipo_veiculo,
                                             value='Moto', text_color_disabled='black', text='Moto')
        self.radio_moto.place(relx=0.5, rely=0.245)

        self.radio_carro = ctk.CTkRadioButton(master=self.Frame1.tab('Entrada'), variable=self.tipo_veiculo,
                                              value='Carro',
                                              text_color_disabled='black', text='Carro')
        self.radio_carro.place(relx=0.58, rely=0.245)

        self.lista_marcas = ['Não Específicado', 'VolksWagem', 'Ford', 'Chevrolet', 'Fiat', 'Renault', 'Peageult',
                             'Honda', 'Suzuki', 'Yamaha']
        self.combo_marca = ctk.CTkComboBox(master=self.Frame1.tab('Entrada'))
        self.combo_marca.configure(bg_color=self.cor2, fg_color='white', values=self.lista_marcas)
        self.combo_marca.set('Não Especificado')
        self.combo_marca.place(relx=0.35, rely=0.47, relwidth=0.13)

        self.lista_cor = ['Não Especificado', 'Vermelho', 'Prata', 'Azul', 'Verde', 'Preto', 'Branco']
        self.combo_cor = ctk.CTkComboBox(master=self.Frame1.tab('Entrada'))
        self.combo_cor.configure(fg_color='white', bg_color=self.cor2, values=self.lista_cor)
        self.combo_cor.set('Não Especificado')
        self.combo_cor.place(relx=0.54, rely=0.47, relwidth=0.13)

        self.btn_entrada = ctk.CTkButton(master=self.Frame1.tab('Entrada'), command=self.comando_btn_entrada)
        self.btn_entrada.configure(text='Entrada')
        self.btn_entrada.place(relx=0.44, rely=0.72, relheight=0.15, relwidth=0.1)

        self.e_placa2 = ctk.CTkEntry(master=self.Frame1.tab('Saida'))
        self.e_placa2.configure(fg_color='white', bg_color=self.cor2)
        self.e_placa2.place(relwidth=0.12, relx=0.35, rely=0.23, relheight=0.15)

        self.carimbado = tk.BooleanVar()
        self.carimbado.set(False)
        self.check_carimbado = ctk.CTkCheckBox(master=self.Frame1.tab('Saida'), text='Recibo Carimbado?',
                                               text_color='black', bg_color=self.cor2, variable=self.carimbado,
                                               onvalue=True, offvalue=False,
                                               font=ctk.CTkFont(family='Sans Serif', size=15))
        self.check_carimbado.place(relx=0.5, rely=0.24)

        self.lista_convenios = ['Nenhum', 'Banca do Edson', 'Banco do Dinei', 'Supermercado Baleia']
        self.combo_convenio = ctk.CTkComboBox(master=self.Frame1.tab('Saida'), fg_color='white', bg_color=self.cor2,
                                              values=self.lista_convenios)
        self.combo_convenio.set('Nenhum')
        self.combo_convenio.place(relx=0.35, rely=0.47, relwidth=0.17)

        self.btn_saida = ctk.CTkButton(master=self.Frame1.tab('Saida'), text='Saída', bg_color=self.cor2,
                                       command=self.comando_btn_saida)
        self.btn_saida.place(relx=0.44, rely=0.72, relheight=0.15, relwidth=0.1)

        estilo_sizegrip = ttk.Style()
        estilo_sizegrip.configure("TSizegrip", background=self.cor1)
        self.Sizegrip = ttk.Sizegrip(master=self.root, style="TSizegrip")
        self.Sizegrip.place(relwidth=0.1, relheight=0.1)
        self.Sizegrip.pack(side='bottom', anchor='se')
    def janela_calculadora(self, preco):

        self.janela = ctk.CTk()
        self.janela.configure(fg_color='white')
        self.preco = preco
        self.janela.title('Pagamento')
        self.janela.configure(background='white')
        self.janela.geometry('300x300+500+200')
        self.janela.resizable(False, False)
        fonte3 = ctk.CTkFont(family='Arial', size=12, weight='normal')
        self.lb_valor = ctk.CTkLabel(master=self.janela)
        self.lb_valor.configure(fg_color='white', font=fonte3, anchor='w', text_color='black', text='Valor a ser pago:')
        self.lb_valor.place(rely=0.1, relx=0.05)

        self.lb_preco = ctk.CTkLabel(master=self.janela)
        texto = 'R$ %.2f' % (preco)
        texto = texto.replace(".", ",")
        self.lb_preco.configure(text=texto, fg_color='white', text_color='black', font=fonte3)
        self.lb_preco.place(relx=0.39, rely=0.1)
        self.lb_valor_pago = ctk.CTkLabel(master=self.janela)
        self.lb_valor_pago.configure(text='Valor pago: ', font=fonte3, fg_color='white', anchor='w')
        self.lb_valor_pago.place(relx=0.05, rely=0.25)

        self.e_valor_pago = ctk.CTkEntry(master=self.janela)
        self.e_valor_pago.configure(fg_color='white', bg_color='white')
        self.e_valor_pago.insert(0, 'R$ ')
        self.e_valor_pago.place(relx=0.3, rely=0.25, relwidth=0.3)
        self.e_valor_pago.focus()

        self.btn_troco = ctk.CTkButton(master=self.janela, text='Calcular', bg_color='white',
                                       command=self.comando_calcular)
        self.btn_troco.place(relx=0.7, rely=0.25, relwidth=0.2)

        self.texto_troco = tk.StringVar(master=self.janela)
        self.texto_troco.set('')
        self.lb_troco = ctk.CTkLabel(master=self.janela)
        self.lb_troco.configure(fg_color='white', bg_color='white', anchor='w', font=fonte3, text='Troco: ')
        self.lb_troco.place(relx=0.05, rely=0.45)

        self.lb_valor_troco = tk.Label(master=self.janela)
        self.lb_valor_troco.configure(background='lightgrey', textvariable=self.texto_troco)
        self.lb_valor_troco.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.1)
        self.btn_ok = ctk.CTkButton(master=self.janela, command=self.comando_ok)
        self.btn_ok.configure(text='Ok', bg_color='white')
        self.btn_ok.place(relx=0.27, rely=0.8, relwidth=0.2)

        self.btn_cancel = ctk.CTkButton(master=self.janela)
        self.btn_cancel.configure(text='Cancelar', bg_color='white', command=lambda: self.janela.destroy())
        self.btn_cancel.place(relx=0.48, rely=0.8, relwidth=0.22)

        self.e_valor_pago.bind('<Return>', lambda e: self.comando_calcular())
        self.janela.mainloop()
    def eventos_binding(self):
        self.treewiew.bind('<Button-3>', self.binding_treewiew)
        self.treewiew.bind('<Double-Button-1>', self.binding_treewiew2)
        self.e_placa.bind('<Return>', self.binding_entry)
        self.lb_relogio.bind('<Button-3>', self.binding_root)
        self.lb_auxiliar.bind('<Button-3>', self.binding_root)
        self.root.bind('<Control-Tab>', self.binding_root2)
        self.e_placa2.bind('<Return>', self.binding_entry2)
    def comando_btn_entrada(self):

        """Obtém todas as informações de entrada e salva em um dicionario"""

        placa = self.e_placa.get()
        placa = placa.upper()
        tipo = self.tipo_veiculo.get()
        marca = self.combo_marca.get()
        cor = self.combo_cor.get()
        hora = datetime.datetime.now()
        hora = hora.strftime("%Y-%m-%d %H:%M:%S")
        hora = datetime.datetime.strptime(hora, "%Y-%m-%d %H:%M:%S")
        if placa == '':
            messagebox.showerror(title='Erro de entrada', message='Informe uma placa')

        else:
            veiculo = {'Placa': placa, 'Tipo': tipo, 'Marca': marca, 'Cor': cor,
                       'Hora': f'{hora.hour}:{hora.minute}:{hora.second}'}
            text_confirmacao = 'Confirmar os dados a seguir?\n'
            for i, j in veiculo.items():
                text_confirmacao += f'{i}: {j}\n'
            mensagem_confirmacao = messagebox.askokcancel(title='Confirmação de Entrada', message=text_confirmacao)
            if mensagem_confirmacao is True:
                self.conectar_banco_de_dados()
                self.cursor.execute("""SELECT Placa FROM mensalistas""")
                dados_mensalista = self.cursor.fetchall()
                placas = []
                for i in dados_mensalista:
                    placas.append(i[0])

                if placa in placas:
                    messagebox.showwarning('Mensalista', message='VEÍCULO MENSALISTA!!!')
                    self.e_placa.delete(first_index=0, last_index=tk.END)
                    self.tipo_veiculo.set('Carro')
                    self.combo_cor.set('Não especificado')
                    self.combo_marca.set('Não especificado')
                else:
                    try:
                        self.conectar_banco_de_dados()
                        self.cursor.execute("""INSERT INTO patio (Placa, Tipo, Marca, Cor, Hora) VALUES (?,?,?,?,?)""",
                                            (placa, tipo, marca, cor, hora))
                        self.conn.commit()
                        self.desconecta_banco_de_dados()
                        self.preenche_treewiew()
                        self.e_placa.delete(first_index=0, last_index=tk.END)
                        self.combo_marca.set('Não Especificado')
                        self.combo_cor.set('Não Especificado')
                        self.tipo_veiculo.set('Carro')
                    except sql.IntegrityError:
                        messagebox.showerror('Placa Existente',
                                             message='O veículo digitado já está no pátio, tente novamente!!!')
                        self.e_placa.delete(first_index=0, last_index=tk.END)
    def comando_btn_saida(self):
        self.placa_saida = self.e_placa2.get()
        self.placa_saida = self.placa_saida.upper()
        recibo_carimbado = self.check_carimbado.get()
        conveniado = self.combo_convenio.get()
        if self.placa_saida == '':
            messagebox.showerror(title='Erro de Saída', message='Digite a placa do veículo')
        else:
            self.conectar_banco_de_dados()
            self.cursor.execute("""SELECT Placa FROM Patio""")
            placas = self.cursor.fetchall()
            self.desconecta_banco_de_dados()
            for i in range(len(placas)):
                placas[i] = placas[i][0]
            if self.placa_saida not in placas:
                messagebox.showerror('', message='Veículo não está no pátio, tente outra placa!!')
                self.e_placa2.delete(first_index=0, last_index=tk.END)
            else:
                self.conectar_banco_de_dados()
                self.cursor.execute("""SELECT * FROM PATIO WHERE Placa = ?""", (self.placa_saida,))
                hora_saida = datetime.datetime.now()
                veiculo = self.cursor.fetchall()
                tipo_veiculo = veiculo[0][1]
                hora_entrada = veiculo[0][-1]
                hora_entrada = datetime.datetime.strptime(hora_entrada, "%Y-%m-%d %H:%M:%S")
                delta = hora_saida - hora_entrada
                horas = int(delta.total_seconds() / 3600)
                self.cursor.execute("""SELECT * FROM precos""")
                (preco_carro, preco_moto) = map(float, self.cursor.fetchall()[0])
                self.desconecta_banco_de_dados()
                if recibo_carimbado is False:
                    if tipo_veiculo == 'Carro':
                        preco = (horas+1) * preco_carro
                        self.janela_calculadora(preco)
                    else:
                        preco = preco_moto * (horas+1)
                        self.janela_calculadora(preco)
                elif recibo_carimbado is True:
                    if conveniado == 'Nenhum' or conveniado not in self.lista_convenios:
                        messagebox.showerror('Erro', message='Selecione um dos convênios válidos!!')
                    else:
                        self.conectar_banco_de_dados()
                        self.cursor.execute("""DELETE FROM patio WHERE Placa = ?""", (self.placa_saida,))
                        self.conn.commit()
                        self.desconecta_banco_de_dados()
                        self.preenche_treewiew()
                        self.e_placa2.delete(first_index=0, last_index=tk.END)
                        self.carimbado.set(False)
                        self.combo_convenio.set('Nenhum')
                        messagebox.showwarning('Sucesso', message='Saída Efetuada com sucesso!!!')
                        self.Frame1.set('Entrada')
    def comando_mudar_cor(self):
        self.root.configure(fg_color=colorchooser.askcolor()[1])
    def comando_menu_treewiew(self):
        linhas_selecionadas = self.treewiew.selection()
        placa_selecionada = self.treewiew.item(linhas_selecionadas, 'values')[0]
        self.e_placa2.delete(first_index=0, last_index=tk.END)
        self.e_placa2.insert(0, placa_selecionada)
        self.e_placa2.focus()
        self.Frame1.set('Saida')
    def comando_calcular(self):
        """Obtém o valor inserido pelo usuário e retorna o troco necessário"""
        valor_pago = self.e_valor_pago.get()
        valor_pago = valor_pago.replace("R$", "")
        valor_pago = valor_pago.replace(",", ".")
        valor_pago.rstrip()
        valor_pago.lstrip()
        valor_pago = float(valor_pago)
        troco = valor_pago - self.preco
        texto = 'R$ %.2f'%(troco)
        texto = texto.replace('.', ',')
        self.texto_troco.set(texto)
    def comando_ok(self):
        self.conectar_banco_de_dados()
        self.cursor.execute("""DELETE FROM patio WHERE PLACA = ?""", (self.placa_saida,))
        self.conn.commit()
        self.desconecta_banco_de_dados()
        self.preenche_treewiew()
        self.e_placa2.delete(first_index=0, last_index=tk.END)
        self.carimbado = False
        self.combo_convenio.set('Nenhum')
        self.janela.destroy()
        messagebox.showwarning(title='', message='Saída efetuada com sucesso\n'
                                                 'Não se esqueça de tocar o sino quando o veículo deixar o pátio!!!')
        self.Frame1.set('Entrada')
    def comando_alterar(self):
        def comando_btn_alterar():
            novo_tipo = tipo_veiculo.get()
            nova_marca = combo_marca.get()
            nova_cor = combo_cor.get()
            self.conectar_banco_de_dados()
            self.cursor.execute("""UPDATE patio SET Tipo = ?, Marca = ?, Cor = ? WHERE Placa = ?""",
                                (novo_tipo, nova_marca, nova_cor, registro[0]))
            self.conn.commit()
            self.desconecta_banco_de_dados()
            self.preenche_treewiew()
            self.janela_atualizar.destroy()

        indice_registro = self.treewiew.selection()
        registro = self.treewiew.item(indice_registro, option='values')

        self.janela_atualizar = ctk.CTkToplevel()
        self.janela_atualizar.geometry("400x300+450+50")
        self.janela_atualizar.resizable(False, False)
        self.janela_atualizar.title('Alterar Entrada de Veículo')
        self.janela_atualizar.configure(fg_color='white')
        fonte = ctk.CTkFont(family='Arial', size=12, slant='roman', weight='normal')
        lb_placa_nova = ctk.CTkLabel(master=self.janela_atualizar)
        lb_placa_nova.configure(text='Placa: ', anchor='w', font=fonte, fg_color='white', bg_color='white',
                                text_color='Black')
        lb_placa_nova.place(relx=0.02, rely=0.1)

        entry_placa_nova = ctk.CTkEntry(master=self.janela_atualizar)
        entry_placa_nova.configure(fg_color='white', bg_color='white', text_color='black')
        entry_placa_nova.place(relx=0.15, rely=0.1)
        entry_placa_nova.insert(index=0, string=registro[0])
        entry_placa_nova.configure(state=tk.DISABLED)

        tipo_veiculo = tk.StringVar()
        tipo_veiculo.set(value=registro[1])
        radio_moto = ctk.CTkRadioButton(master=self.janela_atualizar, variable=tipo_veiculo, value='Moto',
                                        text='Moto', font=fonte)
        radio_moto.place(relx=0.55, rely=0.1)

        radio_carro = ctk.CTkRadioButton(master=self.janela_atualizar, variable=tipo_veiculo, value='Carro',
                                         text='Carro', font=fonte)
        radio_carro.place(relx=0.72, rely=0.1)

        lb_marca = ctk.CTkLabel(master=self.janela_atualizar)
        lb_marca.configure(text='Marca: ', text_color='Black', font=fonte, fg_color='white', bg_color='white', anchor='w')
        lb_marca.place(relx=0.02, rely=0.3)

        combo_marca = ctk.CTkComboBox(master=self.janela_atualizar)
        combo_marca.configure(values=self.lista_marcas, fg_color='white', bg_color='white')
        combo_marca.place(relx=0.15, rely=0.3)
        combo_marca.set(value=registro[2])

        lb_cor = ctk.CTkLabel(master=self.janela_atualizar)
        lb_cor.configure(fg_color='white', bg_color='white', text='Cor: ', text_color='Black', anchor='w')
        lb_cor.place(relx=0.02, rely=0.5)

        combo_cor = ctk.CTkComboBox(master=self.janela_atualizar)
        combo_cor.configure(fg_color='white', bg_color='white', values=self.lista_cor)
        combo_cor.place(relx=0.15, rely=0.5)
        combo_cor.set(value=registro[3])

        btn_atualizar = ctk.CTkButton(master=self.janela_atualizar)
        btn_atualizar.configure(bg_color='white', text='Atualizar', command=comando_btn_alterar)
        btn_atualizar.place(relx=0.3, rely=0.78, relwidth=0.2, relheight=0.1)

        btn_cancelar = ctk.CTkButton(master=self.janela_atualizar, command=self.janela_atualizar.destroy)
        btn_cancelar.configure(text='Cancelar', bg_color='white')
        btn_cancelar.place(relx=0.55, rely=0.78, relwidth=0.2, relheight=0.1)
        self.janela_atualizar.mainloop()
    def janela_inserir_mensalista(self):

        def comando_btn_cadastrar():

            placa = e_placa.get()
            placa = placa.upper()
            tipo = tipo_veiculo.get()
            marca = combo_marca.get()
            cor = combo_cor.get()
            mensalidade = e_valor_mensalidade.get()
            mensalidade = mensalidade.replace('R$ ', '')
            mensalidade = mensalidade.replace(',', '.')
            mensalidade.lstrip()
            mensalidade.rstrip()
            nome = e_nome.get()

            if placa == '':
                messagebox.showerror('Veículo sem Placa', message='Insira uma placa válida para o veículo!')
                self.janela_mensalista.focus()
            else:
                try:
                    self.conectar_banco_de_dados()
                    self.cursor.execute("""INSERT INTO mensalistas (Placa, Tipo, Marca, Cor, Nome, Mensalidade) VALUES (?,?,?,?,?,?)""",
                                        (placa, tipo, marca, cor, nome, float(mensalidade)))
                    self.conn.commit()
                    self.desconecta_banco_de_dados()
                    messagebox.showwarning('Sucesso', 'Veículo mensalista adicionado com sucesso!!!')
                    self.janela_mensalista.destroy()

                except sql.IntegrityError as erro:
                    messagebox.showerror('Erro', message='Veículo já cadastrado como mensalista')
                    e_placa.delete(first_index=0, last_index=tk.END)
                    self.desconecta_banco_de_dados()
                    self.janela_mensalista.focus()

        fonte = ctk.CTkFont(family='Arial', size=12, weight='bold', slant='roman')
        self.janela_mensalista = tk.Toplevel(master=self.root)
        self.janela_mensalista.geometry('600x600')
        self.janela_mensalista.configure(background='white')
        self.janela_mensalista.resizable(False, False)
        self.janela_mensalista.title('Inserir Mensalista')
        lb_placa = ctk.CTkLabel(master=self.janela_mensalista)
        lb_placa.configure(fg_color='white', bg_color='white', text_color='black', font=fonte, text='Placa do veículo:',
                           anchor='w')
        lb_placa.place(relx=0.02, rely=0.1)

        e_placa = ctk.CTkEntry(master=self.janela_mensalista)
        e_placa.configure(fg_color='white', bg_color='white')
        e_placa.place(relx=0.25, rely=0.1)

        tipo_veiculo = tk.StringVar()
        tipo_veiculo.set('Carro')
        radio_moto = ctk.CTkRadioButton(master=self.janela_mensalista, value='Moto', text='Moto')
        radio_moto.configure(variable=tipo_veiculo)
        radio_moto.place(relx=0.6, rely=0.1)

        radio_carro = ctk.CTkRadioButton(master=self.janela_mensalista, value='Carro')
        radio_carro.configure(variable=tipo_veiculo, text='Carro')
        radio_carro.place(relx=0.75, rely=0.1)

        lb_marca = ctk.CTkLabel(master=self.janela_mensalista)
        lb_marca.configure(fg_color='white', bg_color='white', text='Marca do veículo: ', font=fonte, anchor='w')
        lb_marca.place(relx=0.02, rely=0.25)

        combo_marca = ctk.CTkComboBox(master=self.janela_mensalista, values=self.lista_marcas)
        combo_marca.configure(fg_color='white')
        combo_marca.place(relx=0.25, rely=0.25)

        lb_cor = ctk.CTkLabel(master=self.janela_mensalista)
        lb_cor.configure(fg_color='white', bg_color='white', font=fonte, anchor='w', text='Cor do veículo: ')
        lb_cor.place(relx=0.02, rely=0.4)

        combo_cor = ctk.CTkComboBox(master=self.janela_mensalista, values=self.lista_cor)
        combo_cor.configure(fg_color='white', bg_color='white')
        combo_cor.place(relx=0.25, rely=0.4)

        lb_valor_mensalidade = ctk.CTkLabel(master=self.janela_mensalista)
        lb_valor_mensalidade.configure(fg_color='white', bg_color='white', font=fonte, text_color='black', anchor='w',
                                       text='Valor da mensalidade: ')
        lb_valor_mensalidade.place(relx=0.02, rely=0.55)

        e_valor_mensalidade = ctk.CTkEntry(master=self.janela_mensalista)
        e_valor_mensalidade.configure(fg_color='white', bg_color='white')
        e_valor_mensalidade.insert(index=0, string='R$ ')
        e_valor_mensalidade.place(relx=0.3, rely=0.55)

        lb_nome = ctk.CTkLabel(master=self.janela_mensalista)
        lb_nome.configure(fg_color='white', bg_color='white', text_color='black', font=fonte, anchor='w',
                          text='Nome do Mensalista: ')
        lb_nome.place(relx=0.02, rely=0.7)

        e_nome = ctk.CTkEntry(master=self.janela_mensalista)
        e_nome.configure(fg_color='white', bg_color='white')
        e_nome.place(relx=0.3, rely=0.7, relwidth=0.6)

        btn_cadastrar = ctk.CTkButton(master=self.janela_mensalista, command=comando_btn_cadastrar)
        btn_cadastrar.configure(text='Cadastrar')
        btn_cadastrar.place(relx=0.3, rely=0.85, relwidth=0.18, relheight=0.08)

        btn_cancelar = ctk.CTkButton(master=self.janela_mensalista, command=self.janela_mensalista.destroy)
        btn_cancelar.configure(text='Cancelar')
        btn_cancelar.place(relx=0.5, rely=0.85, relwidth=0.18, relheight=0.08)

        self.janela_mensalista.mainloop()
    def janela_gerenciar_mensalista(self):

        def preenche_treeview():
            self.conectar_banco_de_dados()
            self.cursor.execute("""SELECT * FROM mensalistas""")
            mensalistas = self.cursor.fetchall()
            self.desconecta_banco_de_dados()
            Treeview.delete(*Treeview.get_children())
            for i in mensalistas:
                Treeview.insert('', index=0, values=(i[0], i[1], i[2], i[3], i[4], f'R$ {i[5]}'.replace('.', ',')))

        def comando_excluir():

            try:
                index = Treeview.selection()
                registro = Treeview.item(index, 'values')
                placa = registro[0]
                cliente = {'Placa': registro[0], 'Tipo': registro[1], 'Marca': registro[2], 'Cor':registro[3], 'Nome':registro[4], 'Mensalidade': registro[5]}
                texto = ''
                for i,j in cliente.items():
                    texto+=f'\n{i}: {j}'
                janela_principal.iconify()
                opcao = messagebox.askyesno('Deletar Mensalista', 'Tem certeza que deseja deletar o seguinte cliente mensalista?' + texto)

                if opcao is True:
                    self.conectar_banco_de_dados()
                    self.cursor.execute("""DELETE FROM mensalistas WHERE Placa = ?""", (placa, ))
                    self.conn.commit()
                    self.desconecta_banco_de_dados()
                    preenche_treeview()
                    janela_principal.deiconify()

                else:
                    janela_principal.deiconify()

            except tk.TclError as erro:
                print(erro)

            else:
                pass


        janela_principal = tk.Toplevel(master=self.root)
        janela_principal.configure(background='white')
        janela_principal.geometry('1400x600')
        janela_principal.title('Gerenciamento de Mensalistas')
        janela_principal.resizable(False, False)
        lb_titulo = ctk.CTkLabel(master=janela_principal)
        lb_titulo.configure(fg_color='white', bg_color='white', text='Veículos Mensalistas',
                            font=ctk.CTkFont(family='Arial', size=15, weight='bold', slant='italic'), anchor='center')
        lb_titulo.place(rely=0.02, relx = 0.425)

        frame1 = ctk.CTkFrame(master=janela_principal, border_width=0, border_color='black')
        frame1.configure(fg_color='white', corner_radius=0,)
        frame1.place(relx = 0.02, rely = 0.1, relwidth = 0.96, relheight = 0.85)

        estilo_treeview = ttk.Style()
        estilo_treeview.configure("nova_treeview.Treeview", font = ('Arial', 10))
        Treeview = ttk.Treeview(master=frame1, style='nova_treeview.Treeview')
        Treeview.configure(columns=('Placa', 'Tipo', 'Marca', 'Cor', 'Nome', 'Mensalidade'), show='headings')
        Treeview.column('Placa', anchor='center')
        Treeview.column('Tipo', anchor='center')
        Treeview.column('Marca', anchor='center')
        Treeview.column('Cor', anchor='center')
        Treeview.column('Nome', anchor='center')
        Treeview.column('Mensalidade', anchor='center')
        Treeview.heading('Placa', text='Placa', anchor='center' )
        Treeview.heading('Tipo', text='Tipo', anchor='center')
        Treeview.heading('Marca', text='Marca', anchor='center')
        Treeview.heading('Cor', text='Cor', anchor='center')
        Treeview.heading('Nome', text='Nome', anchor='center')
        Treeview.heading('Mensalidade', text='Mensalidade', anchor='center')


        yScrollbar = ctk.CTkScrollbar(master=Treeview, orientation='vertical', command=Treeview.yview)
        yScrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        Treeview.configure(yscrollcommand=yScrollbar.set)
        Treeview.place(relx=0, rely=0, relwidth=1, relheight=1)

        menu_treeview = tk.Menu(master=Treeview, tearoff=False)
        menu_treeview.add_command(label='Editar')
        menu_treeview.add_command(label='Excluir', command=comando_excluir)
        menu_janela_principal = tk.Menu(master=janela_principal, tearoff=False)
        menu_janela_principal.add_command(label='Fechar', command=janela_principal.destroy)

        Treeview.bind('<Button-3>', lambda event: menu_treeview.post(event.x_root, event.y_root))
        janela_principal.bind('<Button-3>', lambda event: menu_janela_principal.post(event.x_root, event.y_root))
        preenche_treeview()
        janela_principal.mainloop()
    def preenche_treewiew(self):
        self.treewiew.delete(*self.treewiew.get_children())
        self.conectar_banco_de_dados()
        self.cursor.execute("SELECT * FROM patio")
        linhas = self.cursor.fetchall()
        for i in linhas:
            self.treewiew.insert("", index=0, values=i)

        self.desconecta_banco_de_dados()
    def binding_treewiew(self, event):
        self.menu_treewiew.post(event.x_root, event.y_root)
    def binding_treewiew2(self, event):
        linha_selecionada = self.treewiew.selection()
        conteudo = self.treewiew.item(linha_selecionada, 'values')
        text = f'Placa : {conteudo[0]}\nTipo : {conteudo[1]}\nMarca: {conteudo[2]}\nCor : {conteudo[3]}\nHorário de Entrada: {conteudo[4]}'
        messagebox.showinfo('Info Veículo', message=text)
    def binding_entry(self, event):
        self.comando_btn_entrada()
    def binding_entry2(self, event):
        self.comando_btn_saida()
    def binding_root(self, event):
        self.menu_frame1.post(event.x_root, event.y_root)
    def binding_root2(self, event):
        if self.Frame1.get() == 'Entrada':
            self.Frame1.set('Saida')
        else:
            self.Frame1.set('Entrada')
    def conectar_banco_de_dados(self):
        self.conn = sql.connect('estacionamento.db')
        self.cursor = self.conn.cursor()
    def desconecta_banco_de_dados(self):
        self.conn.close()

window = App()
window.root.mainloop()
