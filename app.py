import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("dark")

# Criação das funcionalidades 
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    # Aqui você pode adicionar a lógica de validação do login
    if usuario == "Lucas" and senha == "1234":
       resultado_login.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Usuário ou senha incorretos.",text_color="red")

#Criação da janela principal
app=ctk.CTk()
app.title("Sistema de login")
app.geometry("300x200")
#Criação de campos
#Label
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)

#Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

#Label
label_senha= ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha ", show="*")
campo_senha.pack(pady=10)

#Button
button_login = ctk.CTkButton(app, text="Login", command=validar_login)
button_login.pack(pady=10)

#Campo de feedback de login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

#Iniciar a aplicação
app.mainloop()