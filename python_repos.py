import requests

#Fase exploratória para vizualizarmos as infos que recebos depois request
#Descobrir os dados que temos para pode extrair e criar uma visualização 
#Daquilo que realmente queremos no python_repos_visual.py

# Definição da URL da API do GitHub para buscar repositórios Python populares
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

# Cabeçalho da requisição para solicitar a versão 3 da API do GitHub e resposta em JSON
headers = {"Accept": "application/vnd.github.v3+json"}

# Faz a requisição GET à API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # Exibe o código de status da resposta

# Converte a resposta JSON em um dicionário Python
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")  # Exibe o total de repositórios encontrados
print(f"Complete results: {not response_dict['incomplete_results']}")  # Verifica se os resultados estão completos

# Lista de repositórios retornados
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
   print(f"Name: {repo_dict['name']}")
   print(f"Owner: {repo_dict['owner']['login']}")
   print(f"Stars: {repo_dict['stargazers_count']}")
   print(f"Repository: {repo_dict['html_url']}")
   print(f"Created: {repo_dict['created_at']}")
   print(f"Updated: {repo_dict['updated_at']}")
   print(f"Description: {repo_dict['description']}")

