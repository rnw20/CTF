import requests

url = 'https://electronical.chall.pwnoh.io/encrypt'
flag = ""

for i in range(47, 0, -1):
    # create message
    message = 'a' * i
    x = requests.get(url, params = {"message": message})
    resp = x.text

    # split into 16-byte blocks
    parts = [resp[i:i+32] for i in range(0, len(resp), 32)]

    # store target hex sequence
    matchthis = parts[2]

    # iterate through possible characters
    for j in range(33, 127):
        # append known flag to message and test a character
        message1 = message + flag + chr(j)
        x = requests.get(url, params = {"message": message1})
        resp = x.text
        parts = [resp[i:i+32] for i in range(0, len(resp), 32)]
        check = parts[2]
        
        # check if the two hex sequences are the same
        if check == matchthis:
            flag += chr(j)
            print(flag)
            break
