import Token

while True:
    text = input("input > ")
    result, error = Token.run('<stdin>', text)  
    if error:
        print(error.as_string())
    else:
        print(result)
