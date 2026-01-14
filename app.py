import customtkinter as ctk

# Aparência
ctk.set_appearance_mode("dark")      # "light" ou "dark"
ctk.set_default_color_theme("blue")  # blue, green, dark-blue

# Janela
app = ctk.CTk()
app.title("Tela de Login")
app.geometry("350x300")
app.resizable(False, False)

# Título
titulo = ctk.CTkLabel(app, text="Login", font=("Arial", 24))
titulo.pack(pady=20)

# Usuário
usuario = ctk.CTkEntry(app, placeholder_text="Usuário")
usuario.pack(pady=10)

# Senha
senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
senha.pack(pady=10)

# Função do botão
def entrar():
    if usuario.get() == "admin" and senha.get() == "123":
        print("Login realizado com sucesso")
    else:
        print("Usuário ou senha inválidos")

# Botão
botao = ctk.CTkButton(app, text="Entrar", command=entrar)
botao.pack(pady=20)

# Loop da janela
app.mainloop()
