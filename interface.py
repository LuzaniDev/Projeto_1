import mysql.connector
import tkinter as tk
from tkinter import messagebox , ttk 
from ttkthemes import ThemedTk
import os
import hashlib

def FuncRegister(cpf, nome, sobrenome, idade, senha, janela_cadastro):
          
    
    '''
    FUNÇÃO CADASTRAR USUARIO NO BANCO DE DADOS.
    '''

    
    # Estabelece uma conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host='localhost',# <<<<<< mudar para o seu host (MySQL)
        user='root', # <<<<<< mudar para o seu user (MySQL)
        password='1234',# <<<<<< mudar para a sua senha (MySQL)
        database='projeto_1', # <<<<<< mudar para a sua database (MySQL) 
        # OBS: SE FOI USADO O SCRIPT NA PASTA DO PROJETO NÃO PRECISA ALTERAR A DATABASE
    )
    
    # Cria um cursor para executar consultas SQL
    cursor = conexao.cursor()
    
    
    # CRIPTOGRAFIA PARA A SENHA! ######################################################
    
    senha_padrão = senha.get()
    salt = os.urandom(16)  # Gere um "salt" de 16 bytes (128 bits)
    
    # Combina o "salt" com a senha
    senha_com_salt = salt + senha_padrão.encode()
    
    # Cria um objeto de hash SHA-256
    hash_obj = hashlib.sha256()
    
    # Atualiza o objeto de hash com a senha e o "salt" combinados
    hash_obj.update(senha_com_salt)
    
    # Obtenha o valor hash SHA-256 como uma string hexadecimal
    hash_hex = hash_obj.hexdigest()
    salt = salt.hex()


    ###################################################################################
    
    # Verificando as entrys do cadastro se estão preenchidas 
    if cpf.get() and nome.get() and sobrenome.get() and idade.get():
        messagebox.showinfo("Sucesso", "Dados válidos!")
        pass
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        janela_cadastro.destroy()

    # Define o comando SQL de inserção de dados
    comando = f'INSERT INTO users (cpf, nome, sobrenome, idade, senha, salt) VALUES (%s, %s, %s, %s, %s, %s)'
    
    # Define os valores a serem inseridos no banco de dados a partir dos parâmetros da função
    valores = (cpf.get(), nome.get(), sobrenome.get(), idade.get(), hash_hex, salt)



    # Executa o comando SQL com os valores fornecidos
    cursor.execute(comando, valores)
        
    # Confirma a inserção no banco de dados
    conexao.commit()
        
    # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()
    janela_cadastro.destroy() # fecha a aba cadastros



def AbrirCadastro():
    
    """
    FUNÇÃO PARA ABRIR A JANELA DE CADASTRO DE USUÁRIO.
    """
    
    # BASE DA JANELA (cadastrar usuario) 
    janela_cadastro = tk.Toplevel(framePrincipal)
    frame_cadastro = ttk.Frame(janela_cadastro)
    frame_cadastro.pack()
    janela_cadastro.resizable(0,0)
    janela_cadastro.title('Cadastro de Usuario')
    
    # LABELS (cadastrar usuario) 
    label_cpf = ttk.Label(frame_cadastro,text='Digite seu CPF: ')
    label_nome = ttk.Label(frame_cadastro,text='Digite seu Nome: ')
    label_sobrenome = ttk.Label(frame_cadastro,text='Digite seu Sobrenome: ')
    label_idade = ttk.Label(frame_cadastro,text='Digite sua Idade: ')
    label_senha = ttk.Label(frame_cadastro,text='Digite sua Senha: ')


    # ENTRYS (cadastrar usuario) 
    entry_cpf = ttk.Entry(frame_cadastro)
    entry_nome = ttk.Entry(frame_cadastro)
    entry_sobrenome = ttk.Entry(frame_cadastro)
    entry_idade = ttk.Entry(frame_cadastro)
    entry_senha = ttk.Entry(frame_cadastro,show= '*')


    # BUTTON (cadastrar usuario) 
    botao_cadastrar = ttk.Button(frame_cadastro,text='Cadastrar',command=lambda: FuncRegister(entry_cpf, entry_nome, entry_sobrenome, entry_idade, entry_senha, janela_cadastro))
    
    # GRID DO BUTTON (cadastrar usuario) 
    botao_cadastrar.grid(row=7,column=1,padx=5,pady=5)
    
    # GRID DAS LABELS (cadastrar usuario) 
    label_cpf.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    label_nome.grid(row=1,column=0,padx=5,pady=5,sticky="w")
    label_sobrenome.grid(row=2,column=0,padx=5,pady=5,sticky="w")
    label_idade.grid(row=4,column=0,padx=5,pady=5,sticky="w")
    label_senha.grid(row=6,column=0,padx=5,pady=5,sticky="w")

    # GRID DAS ENTRYS (cadastrar usuario) 
    entry_cpf.grid(row=0,column=1,padx=5)
    entry_nome.grid(row=1,column=1,padx=5)
    entry_sobrenome.grid(row=2,column=1,padx=5)
    entry_idade.grid(row=4,column=1,padx=5)
    entry_senha.grid(row=6,column=1,padx=5)
    
    

def AbrirPerfil(users):

    """
    FUNÇÃO PARA ABRIR A JANELA DE PERFIL DO USUÁRIO.
    """
    
    
    # BASE DA JANELA (perfil usuario) 
    janela_perfil = tk.Toplevel(janela)
    perfil_frame = ttk.Frame(janela_perfil)
    janela_perfil.resizable(0,0)
    janela_perfil.title('Perfil do Usuario')

    # LABELS (perfil usuario)
    show_id = ttk.Label(perfil_frame,text=f'ID: {users[0]}',font=('Arial', 15))
    show_cpf = ttk.Label(perfil_frame,text=f'Cpf: {users[1]}',font=('Arial', 15))
    show_nome = ttk.Label(perfil_frame,text=f'Nome: {users[2]}',font=('Arial', 15))
    show_sobrenome = ttk.Label(perfil_frame,text=f'Sobrenome: {users[3]}',font=('Arial', 15))
    show_idade = ttk.Label(perfil_frame,text=f'Idade: {users[4]}',font=('Arial', 15))

    # GRIDS/PACK (perfil usuario)
    perfil_frame.pack()
    show_id.grid(row=0, column=0, padx=5, pady=5,sticky="w")
    show_cpf.grid(row=1, column=0, padx=5, pady=5,sticky="w")
    show_nome.grid(row=2, column=0, padx=5, pady=5,sticky="w")
    show_sobrenome.grid(row=3, column=0, padx=5, pady=5,sticky="w")
    show_idade.grid(row=4, column=0, padx=5, pady=5,sticky="w")



def FuncLogin():
    
    '''
    FUNÇÃO LOGIN DE USUARIO.
    '''

    # Estabelece uma conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host='localhost',# <<<<<< mudar para o seu host (MySQL)
        user='root', # <<<<<< mudar para o seu user (MySQL)
        password='1234',# <<<<<< mudar para a sua senha (MySQL)
        database='projeto_1', # <<<<<< mudar para a sua database (MySQL) 
        # OBS: SE FOI USADO O SCRIPT NA PASTA DO PROJETO NÃO PRECISA ALTERAR A DATABASE
    )
    
    # Cria um cursor para executar consultas SQL
    cursor = conexao.cursor()

    # Obtém o login e a senha fornecidos pelo usuário
    login = entry_login.get()
    senha = entry_senha.get()


    # Comandos MySQL de consulta.
    SQL_login = 'SELECT * FROM users WHERE cpf = %s'
    SQL_Senha = 'SELECT senha FROM users WHERE cpf = %s'
    SQL_Salt = 'SELECT salt FROM users WHERE cpf = %s'

    # Executa as consultas SQL
    cursor.execute(SQL_login, (login,))
    login_resultados = cursor.fetchall()

    cursor.execute(SQL_Senha, (login,))
    senha_resultados = cursor.fetchall()

    cursor.execute(SQL_Salt, (login,))
    salt_resultados = cursor.fetchall()

    # Verifica se o login foi encontrado no banco de dados
    if login_resultados:
        
        
        # Convertendo a lista de caracteres 'salt_resultados' em uma única string
        salt_resultados = ''.join(salt_resultados[0])

        # Convertendo a lista de caracteres 'senha_resultados' em uma única string
        senha_resultados = ''.join(senha_resultados[0])

        # Armazenando a senha resultante em 'senha_armazenada_hash'
        senha_armazenada_hash = senha_resultados

        # Convertendo a string hexadecimal 'salt_resultados' em bytes e armazenando em 'salt_armazenado'
        salt_armazenado = bytes.fromhex(salt_resultados)

        
        # Senha fornecida pelo usuário para verificação
        senha_fornecida = senha
        
        # Combine o "salt" recuperado com a senha fornecida
        senha_com_salt = salt_armazenado + senha_fornecida.encode()
        
        # Crie um objeto de hash SHA-256
        hash_object = hashlib.sha256()
        
        # Atualize o objeto de hash com a senha e o "salt" combinados
        hash_object.update(senha_com_salt)
        
        # Calcule o hash da senha fornecida
        hash_fornecido = hash_object.hexdigest()
        
        # Verifica se a senha corresponde ao login
        if hash_fornecido == senha_armazenada_hash:
            
            # Chama a função AbrirPerfil com o primeiro resultado de login
            AbrirPerfil(login_resultados[0])

        else:
            # Exibe uma mensagem de erro se a senha estiver incorreta
            messagebox.showerror("Erro", "Senha incorreta.")
            
    else:
        # Exibe uma mensagem de erro se o login não foi encontrado
        messagebox.showerror("Erro", "Login não encontrado.")
        
    # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()



# JANELA PRINCIPAL
janela = ThemedTk(theme="clam")
janela.title('Sistema de Login')
janela.resizable(0,0) # bloqueia o redimensionamento de janela
framePrincipal = ttk.Frame(janela)
framePrincipal.pack()


# widgets JANELA PRINCIPAL

# labels JANELA PRINCIPAL
label_login = ttk.Label(framePrincipal, text='Login (cpf): ', font=('Arial', 16))
label_senha = ttk.Label(framePrincipal, text='Senha:', font=('Arial', 16))

# entrys JANELA PRINCIPAL
entry_login = ttk.Entry(framePrincipal)
entry_senha = ttk.Entry(framePrincipal, show='*')

# buttons JANELA PRINCIPAL
button_login = ttk.Button(framePrincipal, text='Login', command=FuncLogin)
button_cadastro = ttk.Button(framePrincipal, text='Cadastrar', command=AbrirCadastro)

# Grid dos widgets na JANELA PRINCIPAL
label_login.grid(row=0, column=0, padx=5, pady=5)
label_senha.grid(row=1, column=0, padx=5, pady=5)
entry_login.grid(row=0, column=1, padx=5, pady=5)
entry_senha.grid(row=1, column=1, padx=5, pady=5)
button_login.grid(row=2, column=1, padx=10, pady=10)
button_cadastro.grid(row=2, column=0, padx=10, pady=10)

janela.mainloop()