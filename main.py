import requests

url = "https://reqres.in/api/users?page=2"

try:
    response = requests.get(url=url)
except ConnectionError:
    print("Проверьте подключение к сети")
else:
    with open("response.txt", "wb") as file:
        file.write(response.content)

print(response)