from flask import Flask, request, jsonify
from selenium_whatsapp import WhatsAppBot

app = Flask(__name__)
print("Creating whtsapp instance")
bot = WhatsAppBot()

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    contact_name = data.get('contact_name')
    message = data.get('message')

    if not contact_name or not message:
        return jsonify({'error': 'Missing contact_name or message'}), 400

    success = bot.send_message(contact_name, message)
    return jsonify({'success': success})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
