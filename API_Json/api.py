#Em um exemplo de request, como por exemplo, subir um post em uma rede
#geralmente temos o path (que vem logo depois do dominio na url), o body
#(o post em si) e o header(como se fosse uma permissão para o request, contendo tipo de data etc)
#já na response, temos o status code(como 404 etc) e o body(post que retornou)

#os principais tipos de requests são get (puxar algo), delete, post e put

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code: ", response.status_code)
print("Content-Type: ", response.headers.get("Content-Type"))


data = response.json()
print("Post Title: ", data["title"])


#--------------------------------------------------------

#exemplo colocando um query parameter 

import requests

url = "https://reqres.in/api/users"
params = {"page": 2}

response = requests.get(url, params = params)
print("Final URL: ", response.url)

response.raise_for_status()  #funciona como um alarme de segurança para erros

data = response.json()
print("Page: ", data["page"])
for users in data["data"]:
    print(users["email"])

#--------------------------------------------------------

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello python",
    "body": "Testing post",
    "userId": 1,
}

response = requests.post(url, json=payload)

print("Status Code: ", response.status_code)

data = response.json()
print(data)

#--------------------------------------------------------

import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status() 
    print("Success: ", response.json())
except requests.exceptions.Timeout:  #aqui, eu puxo o exception pelo request, pois nem todo erro gera um response!
        print("Tempo passou")
except requests.exceptions.RequestException as e:
     print("Requisição falhou: ", e)

