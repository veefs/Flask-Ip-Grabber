import socket
import requests

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


print("Hostname is: " + hostname + "\n" + "Ip is: " + IPAddr)

data = {
    "Hostname is ": hostname,
    "Ip is": IPAddr
}

# URL of your Flask server
url = "http://127.0.0.1:80/webhook"  # Change this to your actual server URL

# Send POST request with JSON data
response = requests.post(url, json=data)