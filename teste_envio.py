import requests

url = "http://127.0.0.1:5000/send_message"
data = {
    "contact_name": "Bael",
    "message": "Olá! Esta é uma mensagem de teste."
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print("Erro ao enviar a mensagem. Status code:", response.status_code)
    print("Detalhes do erro:", response.json())
