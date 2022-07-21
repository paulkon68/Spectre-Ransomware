import base64

with open('sp.png', 'rb') as imagefile:
    base64string = base64.b64encode(imagefile.read()).decode('ascii')

print(base64string)
