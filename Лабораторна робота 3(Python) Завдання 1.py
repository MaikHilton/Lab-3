def slice(input_string):
    if len(input_string) >= 4:  
        return input_string[1:-1]
    else:
        return "Рядок занадто короткий для виконання операції зрізу."

input_string = "Hello world!"
result = slice(input_string)
print(result)
