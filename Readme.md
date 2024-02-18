# Abip Server

O Abip Server é uma aplicação backend construída com Flask que recebe um texto através de uma rota específica e o escreve na tela. O principal caso de uso para este projeto é de leitura de código de barras, como no aplicativo Abip App, disponível no repositório [AbipApp](https://github.com/anatanael/AbipApp).

# Funcionalidades

- API Flask: Expõe uma API REST simples usando o Flask para receber e processar dados de texto.
- Integração com a Área de Transferência: Utiliza a biblioteca pyclip para copiar o texto recebido para a área de transferência.
- Automação: Utiliza o pyautogui para simular a digitação no teclado, automatizando a entrada do texto recebido.

# Pré-requisitos

1. Python 3.x instalado
2. Pip (instalador de pacotes Python)

# Instalação

1. Clone o repositório

```
https://github.com/anatanael/AbipServer.git
```

2. Navegue até o diretório do projeto

```
cd AbipServer
```

3. Instale as dependências

```
pip install -r requirements.txt
```

# Uso

Execute o Abip Server

```
python abip.py
```

Para enviar um texto a ser exibido, faça uma solicitação POST para o endpoint /barcode com um payload JSON:

```
curl -X POST -H "Content-Type: application/json" -d '{"barcode": "seu_texto_aqui"}' http://localhost:5002/barcode
```

Substitua "seu_texto_aqui" pelo texto que deseja exibir.

### Exemplo de requisição

<p align="center">
 <img src="https://github.com/anatanael/AbipServer/assets/51931199/02b46b4e-6f6b-4be9-b0ab-3eb624df5994" width="350" />
</p>

# Configuração

O servidor pode ser configurado usando variáveis de ambiente. Se necessário, crie um arquivo .env na raiz do projeto com as seguintes variáveis:

1. PORT_APP: Especifique a porta na qual o servidor deve ser executado. O padrão é 5002.

# Sair da Aplicação

Para sair da aplicação de forma segura, clique no ícone da bandeja do sistema e selecione "Encerrar" no menu.

# Build

### Utilizando o [pyinstaller](https://pyinstaller.org/) é possível gerar o build da aplicação

```
pyinstaller --onefile --add-data "assets:assets" --noconsole --icon=assets/abip.ico abip.py
```

É possível alterar a porta padrão criando um arquivo abip.config no mesmo diretório do executável.

```
PORT_APP=1234
```

# [Abip App](https://github.com/anatanael/AbipApp)

Abip App é um aplicativo mobile que utiliza este servidor.

<p align="center">
 <img src="https://github.com/anatanael/AbipServer/assets/51931199/2e28d8a3-9262-4965-9e68-40e05ec1cf16" width="200" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <img src="https://github.com/anatanael/AbipServer/assets/51931199/62c9f742-3932-44b8-9696-ba08014d10e4" width="200" />

</p>

# Download

[AbipServer](https://github.com/anatanael/AbipServer/releases)
