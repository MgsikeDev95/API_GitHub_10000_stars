import requests

# Fazendo a requisição
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

#converte o objeto de resposta aem um dicionario
response_dict = r.json()
print(response_dict.keys())

#Usei para descobrir 

#print(sorted(repo_dict[0].keys()))
#Cada vez que o loop passa por uma iteração, ele imprime algo e depois avança para a próxima linha. 