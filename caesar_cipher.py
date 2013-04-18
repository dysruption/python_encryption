#Caesar Cipher
message = 'This is the secret message'
key = 13

mode = 'encrypt'

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = (num + key)%len(LETTERS)
        elif mode == 'decrypt':
            num = (num - key)%len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol


print(translated)

