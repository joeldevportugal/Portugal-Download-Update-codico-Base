import customtkinter
from tkinter import *

# defenir cores --------------------------------------------------------------------
cO0 ='#FFFFFF' # cor para o Label


janela = customtkinter.CTk()
janela.geometry('730x510+100+100')
janela.resizable(False, False)
janela.title('Portugal Download Update Dev Joel')

# criar a entry para colocar o URL ------------------------------------------------
EURL = customtkinter.CTkEntry(janela, width=700, placeholder_text='Insira o Endreço:')
EURL.place(x=5, y=10)
#----------------------------------------------------------------------------------
# criar label Capa ----------------------------------------------------------------
LCapa = Label (janela, bg=cO0, width=95, height=25)
LCapa.place(x=10, y=55)
#---------------------------------------------------------------------------------
# criar Botões -------------------------------------------------------------------
DwnMp3 = customtkinter.CTkButton(janela, text='Download Mp3')
DwnMp3.place(x=565,y=45)
DwnMp4 = customtkinter.CTkButton(janela, text='Download Mp4')
DwnMp4.place(x=565,y=85)
Bninfo = customtkinter.CTkButton(janela, text='Mostrar Informaçoes')
Bninfo.place(x=565,y=125)
Blimpar = customtkinter.CTkButton(janela, text='Limpar')
Blimpar.place(x=565,y=165)
BSair = customtkinter.CTkButton(janela, text='Sair')
BSair.place(x=565,y=205)
#---------------------------------------------------------------------------------
# criar a Listbox ----------------------------------------------------------------
LResultado = Listbox(janela, width=147)
LResultado.place(x=10, y=450)
#------------------------------------------------------------------------------------
janela.mainloop()