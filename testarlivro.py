from livro import livro

t = input("Digite o titulo do livro")
aut = input("Digite o autor do livro")
ano = input("Digite o ano de publicaçao do livro")

livro = Livro(t, aut, ano)

print("o titulo do livro é: ", livro.getTitulo())