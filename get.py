import requests

print(requests.__version__)

print(requests.get("https://www.google.com"))

print(requests.get("https://raw.githubusercontent.com/jwadhwa213/Cmput404/main/get.py").text)
