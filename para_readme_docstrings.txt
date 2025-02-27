# Este código faz uma requisição à API do GitHub para buscar repositórios Python
# com mais de 1000 estrelas, ordenados por número de estrelas. Ele verifica o
# status da resposta, converte os dados em um dicionário Python e exibe informações
# sobre os repositórios retornados.

# Passos do código:
# 1. Define a URL da API com parâmetros de busca (linguagem Python, mais de 1000 estrelas).
# 2. Configura os cabeçalhos para solicitar a versão 3 da API e receber a resposta em JSON.
# 3. Faz a requisição GET e armazena a resposta na variável 'r'.
# 4. Verifica o status code da resposta (200 indica sucesso).
# 5. Converte a resposta JSON em um dicionário Python.
# 6. Exibe o número total de repositórios encontrados e se os resultados estão completos.
# 7. Extrai a lista de repositórios retornados e exibe quantos foram retornados.
# 8. Examina o primeiro repositório da lista, conta suas chaves e as exibe em ordem alfabética.

# Saída esperada:
# - Status code: 200 (requisição bem-sucedida).
# - Total repositories: Número total de repositórios que correspondem à busca.
# - Complete results: True (resultados completos) ou False (resultados incompletos).
# - Repositories returned: Número de repositórios retornados (máximo de 30 por página).
# - Keys: Número de chaves (campos) no dicionário do primeiro repositório.
# - Lista de chaves: Nomes dos campos de informação sobre o repositório, ordenados alfabeticamente.

# Observações:
# - A API do GitHub retorna no máximo 30 repositórios por página.
# - O número total de repositórios pode variar ao longo do tempo.
# - As chaves do dicionário representam os metadados disponíveis sobre cada repositório.    
#for key in sorted(repo_dict.keys()):
#   print(key) para as chaves sorted(ordem alfabetica),repo dicts.keys(as chaves do dict)
# depois imprime tudo

1. url:
É o link (endpoint) da API que você quer acessar.

No seu caso, é a URL da API do GitHub para buscar repositórios Python populares:

python
Copy
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
2. headers:
É uma variável que você definiu como um dicionário Python.

Ela contém o cabeçalho Accept, que especifica o formato da resposta que você espera receber:

python
Copy
headers = {"Accept": "application/vnd.github.v3+json"}
Accept: Informa ao servidor que você quer uma resposta no formato JSON.

application/vnd.github.v3+json: Especifica que você quer a versão 3 da API do GitHub.

3. requests.get():
É a função que faz a requisição HTTP GET à URL especificada.

Ela recebe dois argumentos principais:

A url que você quer acessar.

O parâmetro headers, que contém os cabeçalhos personalizados que você definiu.

python
Copy
r = requests.get(url, headers=headers)
4. O que requests.get() retorna?
A função requests.get() retorna um objeto da classe Response (armazenado na variável r).

Esse objeto contém:

Cabeçalhos da resposta (r.headers): Metadados sobre a resposta.

Código de status (r.status_code): Por exemplo, 200 para sucesso, 404 para não encontrado.

Corpo da resposta (r.content ou r.text): O conteúdo da resposta, que no caso da API do GitHub é uma string JSON.

5. Convertendo a resposta para um dicionário:
Para acessar os dados da resposta de forma fácil, você converte o corpo da resposta (que está em JSON) para um dicionário Python usando o método .json():

python
Copy
response_dict = r.json()
Agora, response_dict é um dicionário que contém os dados retornados pela API.

6. O que tem dentro de response_dict?
O dicionário response_dict contém as informações retornadas pela API do GitHub.

Por exemplo:

response_dict['total_count']: O número total de repositórios encontrados.

response_dict['items']: Uma lista de dicionários, onde cada dicionário representa um repositório.

Resumo do fluxo:
URL: Você define o link da API que quer acessar.

Headers: Você especifica o formato da resposta que espera receber (JSON da versão 3 da API do GitHub).

Requisição: Usa requests.get() para fazer a requisição à URL, passando os cabeçalhos.

Resposta: A resposta é armazenada em r, e você converte o corpo da resposta (JSON) para um dicionário Python com r.json().

Dados: Agora você pode acessar os dados da API no dicionário response_dict.

   