import requests
url = 'https://electronical.chall.pwnoh.io/encrypt'

plaintext = ""
for i in range(47, 0, -1):
    message = 'a' * i
    x = requests.get(url, params = {"message": message})
    resp = x.text
    parts = [resp[i:i+32] for i in range(0, len(resp), 32)]
    matchthis = parts[2]
    for j in range(33, 127):
        message1 = message + plaintext + chr(j)
        x = requests.get(url, params = {"message": message1})
        resp = x.text
        parts = [resp[i:i+32] for i in range(0, len(resp), 32)]
        check = parts[2]
        if check == matchthis:
            plaintext += chr(j)
            print(plaintext)
            break
print(plaintext)
