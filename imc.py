import functions as f

# Start interaction with the user
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
v_imc = str(f.imc(peso, altura))
# Call the function classifica, passing 3 variables and insert the result in variable v_class
v_class = f.classifica(sexo, peso, altura)

# Print the results
print('O seu IMC é:', v_imc[0:5])
print('A sua classificação é:', v_class)
