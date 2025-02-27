import requests
import plotly.express as px

# Definição da URL da API do GitHub para buscar repositórios Python populares
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

# Cabeçalho da requisição para solicitar a versão 3 da API do GitHub e resposta em JSON
headers = {"Accept": "application/vnd.github.v3+json"}

# Faz a requisição GET à API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # Exibe o código de status da resposta

# Converte a resposta JSON em um dicionário Python
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")  # Verifica se os resultados estão completos

#Processa as infos de repositórios 
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name= (repo_dict['name'])
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'> {repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    #Cria textos flutuantes
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text =f"{owner}<br />{description}" 
    hover_texts.append(hover_text)   

#Creates de visualization
title = "Most-Starred Python Projects on Github"
labels = {'x':'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', opacity=0.6)
fig.show()    


