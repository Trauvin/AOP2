
try:
    # pede ao usuário para digitar a quantidade de alunos do curso
    # se nada for digitado ou ocorrer um erro, 5 será o número padrão
    alunos = int(input("Digite a quantidade de alunos (o padrão é 5):"))
except:
    alunos = 5

lst_notas = [] 

i=0
while(i<alunos):

    print("Digite as notas do aluno #{}".format(i+1))

    while True:
        try:

            nota_aop1 = float(input("Nota AOP1: "))
            nota_aop2 = float(input("Nota AOP2: "))
            nota_aop3 = float(input("Nota AOP3: "))
            avaliacao = float(input("Nota AVALIAÇÃO: "))

            nota_total = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao

            if not 0 <= nota_total <= 10:
                raise ValueError("Você digitou alguma nota errada. Lembre-se dos limites de nota das atividades.")
            

        except ValueError as e:
            print("Nota final inválida:", e)

        else:
            break

    media_modulo = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao 

    if media_modulo < 7.0:
        print("O aluno está de recuperação! A média {:.2f} é insuficiente.".format(media_modulo))

        prova_final = float(input("Digite a nota da prova final do aluno: "))
        media_modulo = prova_final
    else:
        print("Aluno aprovado! Nota = ", media_modulo)

    lst_notas.append(media_modulo)

    i+=1


# calcular a porcentagem de aprovados e reprovados
# talvez usar numpy, não sei ainda
# uma alternativa é iterar todos os itens com o laço for
# e fazer um append em outra lista com aprovados e reprovados
# depois subtrair a quantidade de aprovado por reprovados

# listas de aprovados e reprovados
lst_ap = []
lst_rep = []

for i in lst_notas:

    if i < 5.0:
        lst_rep.append(i)
    else:
        lst_ap.append(i)

""" o tamanho da lista com as notas dos aprovados e reprovados, dirá quantos alunos obtiveram 
    resultado acima ou abaixo da média. Após isso, a porcentagem pode ser calculada.
"""
porcentagem_ap = (len(lst_ap) * 100) / alunos
procentagem_rep = 100 - porcentagem_ap
print("De um total de {} alunos, {:.2f}% foram aprovados!".format(alunos, porcentagem_ap))



        


