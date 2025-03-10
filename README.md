How to Use/Como usar em pt ao fim
Download the files:

**1**-On the GitHub repository page, click the "Code" button and then select "Download ZIP".
Extract the ZIP file to a folder on your computer.
Install Python:

**2**- If you don't have Python installed, you can download and install it from the official website: https://www.python.org/downloads/.
Make sure to check the option "Add Python to PATH" during the installation process.
Install dependencies:

**3**-Install dependencies:
The script uses the plotly library to create the visualization. To install it, open your terminal or command prompt and run:
bash
pip install plotly


**4**-Run the script:
Execute the script by running the following command in your terminal or command prompt:
bash
python python_repos_visual.py

Como Usar
Baixe os arquivos:

**1**-Na página do repositório no GitHub, clique no botão "Code" e depois selecione "Download ZIP".
Extraia o arquivo ZIP para uma pasta no seu computador.
Instale o Python:

**2**-Se você ainda não tem o Python instalado, pode baixá-lo e instalá-lo a partir do site oficial: https://www.python.org/downloads/.
Certifique-se de marcar a opção "Add Python to PATH" durante o processo de instalação.

**3**-Instale as dependências:
O script usa a biblioteca plotly para criar a visualização. Para instalá-la, abra o terminal ou prompt de comando e execute:
bash
pip install plotly

**4**-Execute o script:
Execute o script rodando o seguinte comando no terminal ou prompt de comando:
bash
python
python_repos_visual.py

**FLOW**

The URL defines that we want to search for popular Python repositories with more than 10,000 stars.
The header informs that we want the response in JSON format from GitHub's API version 3.
We make a GET request to GitHub's API using requests.get() and store the response in the variable r. Then, response_dict = r.json() converts the response object into a dictionary.
After that, we check if the results are complete and print a message to test if the results were fully returned.

In response_dict, we have dictionaries obtained after storing the response in r, where we use a .get() request with a header to fetch the incoming data. After receiving the response, r.json() was used to convert the data into a Python dictionary.

The variable repo_dicts receives ['items'], which is a list of dictionaries. Then, we create 3 empty lists and use a for loop, where repo_dict (a temporary variable) will receive each of the pieces of information we specified. In this case, these pieces of information are the keys ['name'] and ['html_url'], which will create an f-string with the name, which will be a link to the repository, and ['stargazers_count'], which will define what will be assigned to the variables using the append() method.

Next, we create the data visualization using the plotly.express library, which is aliased as px.
title stores the name of the graph to be created, and labels stores the names that will be displayed on the graph's axes. fig = px.bar(...) determines that the graph will be a bar chart, and there we define what will be assigned to each axis: the name with the link on the X-axis and the number of stars on the Y-axis.
title= receives the value assigned to the variable I created, and labels= receives what will be written on each axis with the dictionary saved in the labels variable.
hover= receives the function to display the information when hovering over the bar (in this case, the owner and the description).
Afterward, with fig.update_layout(), we decide the font sizes for the title and the X and Y axes.
Then, fig.update_traces() allows us to style the color and opacity of the bars.
Finally, the graph is displayed with fig.show().


----------------------//----------------------//--------------------------------//--------------------------------------

O URL define que queremos buscar repositórios populares em Python com mais de 10.000 estrelas.  
O header informa que queremos a resposta no formato JSON da versão 3 da API do GitHub.  
Fazemos uma requisição GET à API do GitHub usando `requests.get()` e armazenamos na variável `r`. Depois, `response_dict = r.json()` converte o objeto de resposta em um dicionário.  
Após isso, verificamos se os resultados estão completos e imprimimos uma mensagem para testar se foram retornados os resultados completos.

No `response_dict`, temos um dicinário que foi obtido após armazenar na variável `r`, onde usamos uma requisição `.get()` com um cabeçalho (header) para obter a informação que viria. Após receber a resposta, `r.json()` foi utilizado para converter os dados em um dicionário Python.

A variável `repo_dicts` recebeu ´response_dict['items']`, que é uma lista de dicionários. Em seguida, criamos 3 listas vazias e usamos um loop `for`, onde `repo_dict` (uma variável temporária) vai receber cada uma das informações que estabelecemos. No caso, essas informações são as chaves `['name']` e `['html_url']`, que vão criar uma f-string com o nome, que será um link para o repositório, e `['stargazers_count']`, que vai definir o que será atribuído às variáveis com o método `append()`.

Depois, criamos a visualização dos dados usando a biblioteca `plotly.express`, que está com o alias `px`.  
`title` salva o nome do gráfico que será feito, e `labels` salva os nomes que serão expostos nos eixos do gráfico. `fig = px.bar(...)` determina que o gráfico será de barras, e ali determinamos o que será atribuído a cada eixo: no eixo X, o nome com link, e no eixo Y, a quantidade de estrelas.  
`title=` recebe o valor atribuído à variável que criei, e `labels=` recebe o que será escrito em cada eixo com o dicionário salvo na variável `labels`.  
`hover=` recebe a função de exibir as informações ao passar o mouse em cima da barra (no caso, o dono e a descrição).  
Depois, com `fig.update_layout()`, decidimos o tamanho das fontes usadas no título e nos eixos X e Y.  
Depois, `fig.update_traces()` permite que eu estilize a cor das barras e a opacidade.  
Finalmente, o gráfico é exibido com `fig.show()`.
