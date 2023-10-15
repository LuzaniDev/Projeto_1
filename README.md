# Sistema de Login com MySQL e Tkinter


Este é um sistema de login simples desenvolvido em Python usando o módulo `tkinter` para a interface gráfica, o banco de dados MySQL para armazenar informações de login e o módulo `hashlib` para armazenar senhas de forma segura.


## Funcionalidades

O sistema de login possui as seguintes funcionalidades:

1. **Cadastro de Usuário:** Ao clicar no botão "Cadastrar", uma janela de cadastro é aberta, permitindo que o usuário insira seu CPF, nome, sobrenome, idade e senha. A senha é criptografada antes de ser armazenada no banco de dados.

2. **Login de Usuário:** O usuário pode inserir seu CPF e senha na janela principal e clicar no botão "Login". O sistema verifica se o CPF está cadastrado no banco de dados e se a senha fornecida corresponde à senha armazenada, usando criptografia para garantir a segurança.

3. **Perfil do Usuário:** Após o login bem-sucedido, uma janela de perfil é aberta, mostrando informações do usuário, como CPF, nome, sobrenome e idade.

## Estrutura do Código

O código é organizado em funções que realizam tarefas específicas, como cadastrar usuários, verificar o login e exibir o perfil. A estrutura do código inclui as seguintes funções:

- `FuncRegister` : Cadastra um novo usuário no banco de dados após validar os campos de entrada.

- `AbrirCadastro` : Abre a janela de cadastro de usuário.

- `AbrirPerfil` : Abre a janela de perfil do usuário.

- `FuncLogin` : Realiza o login do usuário, verificando o CPF e a senha fornecidos.

A janela principal é criada usando o `tkinter` e contém campos de entrada para CPF e senha, bem como botões para login e cadastro.

## Como Executar o Código

1. Certifique-se de que o Python e os módulos necessários (MySQL, Python, ttkthemes) estejam instalados nas versões correspondentes abaixo.
   * Python 3.11.5
   * Mysql-connector-python 8.1.0
   * ttkthemes 3.2.2

3. Configure seu servidor MySQL com o Script deixado nos arquivos.
   
5. Execute o código e você verá a janela de login.

6. Você pode clicar em "Cadastrar" para abrir a janela de cadastro ou inserir seu CPF e senha para fazer login.

Lembre-se de personalizar as informações do banco de dados, como nome de host, usuário e senha, de acordo com a sua configuração como mostrado na imagem abaixo.
![apresentação_1.png](https://github.com/LuzaniDev/Projeto_1/blob/main/apresenta%C3%A7%C3%A3o_1.png)

### Este é um exemplo simples de sistema de login em Python, e pode ser estendido e aprimorado de acordo com suas necessidades.
