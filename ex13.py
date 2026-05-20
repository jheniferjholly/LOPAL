print("Digite sua senha")
valido = ["12345678", "87654321", "18273645"]
senha = " "
while senha != valido:
    senha= input("")
    if senha in valido:
        print("Sua senha valida")
        break
    else:
        print("Sua senha é invalida")




