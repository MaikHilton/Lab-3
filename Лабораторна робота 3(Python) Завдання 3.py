def convert_to_ascii(sentence):
    return ' '.join(str(ord(char)) for char in sentence)

sentence = "Hello, world!"
result = convert_to_ascii(sentence)
print(result)
