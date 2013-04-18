#Caesar Cipher Hacker

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
message = 'aUV`-V`-aUR-`RP_Ra-ZR``NTR'

for possible in range(len(LETTERS)):
    translated = ''
    for letter in message:
        num = LETTERS.find(letter)
        num = (num - possible)%len(LETTERS)
        translated = translated + LETTERS[num]


    print('Key #%s: %s' % (possible, translated))
