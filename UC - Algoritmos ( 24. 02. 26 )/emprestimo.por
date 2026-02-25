programa {
    funcao inicio() {
        real imovel, salario, mensal, prestacao, limite
        inteiro anos, meses
        escreva("Qual é o valor da casa?  \n")
        leia(imovel)

        escreva("Qual é o seu salário:  \n")
        leia(salario)

        escreva("Quantos anos você irá pagar?  \n")
        leia(anos)
//Converter anos para meses
        meses = anos * 12

        prestacao = imovel / meses

        limite = salario *  0.30

        se(prestacao < limite) {
            escreva("Seu empréstimo está aprovado!")

        }senao{
            escreva("Seu empréstimo está negado!")
        }
    }
}