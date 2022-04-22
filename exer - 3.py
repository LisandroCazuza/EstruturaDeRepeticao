"""3.	Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';"""
print("--------------------------------------------")

while True:
    nome = input("Digite seu nome seu :  ").title()
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite sua salário: "))
    sexo = str(input("Digite sua sexualidade- F - Feminino   - M- Masculino  : ").title()
    if  (len(nome)) > 3 :
        print("   ")
    if   (len(nome)) < 3 :
        print("Somente nome com mais de 3 caracteres! ")
    if idade > 0 or   idade < 151 :
        print("   ")
    if salario > 0 :
        print(" ")
    if sexo == 'F' :
            print('Sexo Feminino.')
        
        