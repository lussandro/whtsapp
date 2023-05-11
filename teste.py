import requests

url = "http://127.0.0.1:5000/get_unread_messages"
response = requests.get(url)

if response.status_code == 200:
    unread_messages = response.json()["messages"]
    print("Mensagens não lidas:")
    for message in unread_messages:
        print(f"Nome: {message['name']}")
        print(f"Última mensagem: {message['last_message']}")
        print(f"Quantidade de mensagens: {message['message_count']}\n")
else:
    print(f"Erro ao obter mensagens não lidas. Status code: {response.status_code}")
