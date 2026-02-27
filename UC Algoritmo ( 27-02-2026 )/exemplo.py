altura = float(input("Digite a sua altura: "))
altura = altura * 100

print(f"Sua altura é de {altura} cm")
print("Sua altura é  de: ", altura, "cm")


nome = "Lucas"
idade = 17

texto = "Meu nome é {} e tenho {} anos".format(nome, idade)
texto = "Meu nome é {n} e tenho {i} anos". format(n=nome,i=idade)
texto = "Meu nome é %s e tenho %d anos" % (nome, idade)
print(texto)

#O f antes de uma string no python (ex: f"...") indica uma f-string (formatted sting literal ), introduzida na versão 3.6. Ela permite insetir variáveis ou expressões  diretamente dentro das chaves {} na string, tornando o código mais legível e rápido. O Python avalia a expressão e a substitui pelo seu valor.