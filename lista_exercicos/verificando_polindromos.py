palindromo = input("Digite o possível palíndromo: ")
palindromo = palindromo.lower().replace(" ", "")
possivelPalindromo = palindromo[::-1]

if possivelPalindromo == palindromo:
    print("É palíndromo")
else:
    print("Não é palindromo")