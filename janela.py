#================================janela normal==============================
##Criar janela bonita com o TkInter
##https://www.youtube.com/watch?v=rQLO1m8oia4
#import tkinter
##Para deixar a janela do TkInter precisa instalar o pacote de customização:
##pip install customtkinter

#janela = tkinter.Tk()
##Aqui é o tamanho da janela
#janela.geometry("500x300")

#def clique():
#    print("Fazer Login")

#texto = tkinter.Label(janela, text="Fazer Login")
#texto.pack(padx=10, pady=10)

#botao = tkinter.Button(janela, text="Login", command=clique)
#botao.pack(padx=10, pady=10)

#janela.mainloop()
#================================janela normal==============================


#Página de projetos no github
#https://github.com/tomschimansky/customtkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

flagCheckbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
flagCheckbox.pack(padx=10, pady=10)
#checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()