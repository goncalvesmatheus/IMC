# Define function to calculate IMC
def imc(peso, altura):
    imc = peso / (altura*altura)
    return(imc)

# Define function to classification IMC.
def classifica(sexo, peso, altura):
    valor_imc = imc(peso, altura)

    # Do the calculation if male.
    if sexo == 'm':
        if valor_imc < 20.7:
            return "Abaixo do peso."
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso normal."
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return "Marginalmente acima do peso."
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return "Acima do peso ideal."
        elif valor_imc >= 31.1:
            return "Obesidade."
        else:
            return "Erro de calculo."

    # Do the calculation if female
    if sexo == 'f':
        if valor_imc < 19.1:
            return "Abaixo do peso."
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return "Peso normal."
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return "Marginalmente acima do peso."
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return "Acima do peso ideal."
        elif valor_imc >= 32.3:
            return "Obesidade."
        else:
            return "Erro de calculo."

# Start interation with the user
print('Vamos calcular seu IMC?')

# Validation sexo
valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F.')
    else:
        valid_sexo = True
        print('\n')

# Validation peso
valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso: (Ex. 68.5) ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso inválido. Número não pode ser negativo e nem maior que 350 Kg.')
        else:
            valid_peso = True
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto.')
print('\n')

# Validation altura
valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura: (Ex. 1.75) ')
    try:
        altura = float(altura)
        if altura <= 0.3 or altura > 3:
            print('Altura inválida. Número não pode ser menor que 0.3 ou maior que 3.')
        else:
            valid_altura = True
    except:
        print('Altura inválida. Use apenas números e separe os decimais com ponto.')
print('\n')

# Call the function imc, passing 2 variables and insert the result in variable v_imc converting the result in string
v_imc = str(imc(peso, altura))
# Call the function classifica, passing 3 variables and insert the result in variable v_class
v_class = classifica(sexo, peso, altura)

# Print the results
print('O seu IMC é:', v_imc[0:5])
print('A sua classificação é:', v_class)
