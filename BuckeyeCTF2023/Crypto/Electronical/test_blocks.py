import requests

url = 'https://electronical.chall.pwnoh.io/encrypt'

for i in range(48):
    message = 'a' * i
    x = requests.get(url, params = {"message": message})
    resp = x.text
    parts = [resp[i:i+32] for i in range(0, len(resp), 32)]
    # print 16-byte blocks
    print(str(i) + " " + str(parts))
