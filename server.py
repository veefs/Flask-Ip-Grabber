from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Assuming the request contains JSON data
    # Process the data received from the webhook
    print(data)
    
    with open('IpGrab.txt', 'a') as file:
        file.write(str(data) + '\n')

    return 'Webhook received successfully!', 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)