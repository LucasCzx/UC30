programa {
    funcao inicio() {
        inteiro numero, i

        escreva("Digite um número: ")
        leia(numero)

        i = 1

        enquanto (i <= numero) {
            escreva(i, "\n")
            i = i + 1
        }

        escreva("Fim")
    }
}