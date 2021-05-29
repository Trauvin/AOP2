import os

try:
    """ pede ao usuário para digitar a quantidade de alunos do curso
        se nada for digitado ou ocorrer um erro, 5 será o número padrão
    """
    alunos = int(input("Digite a quantidade de alunos (o padrão é 5): "))
except:
    alunos = 5



lst_notas = [] 

i=0
while(i<alunos):

    print("Digite as notas do aluno #{}".format(i+1))

    # Este laço garante que os valores digitados pelo usuário para as notas sejam coerentes
    while True:
        try:

            nota_aop1 = float(input("Nota AOP1: "))
            nota_aop2 = float(input("Nota AOP2: "))
            nota_aop3 = float(input("Nota AOP3: "))
            avaliacao = float(input("Nota AVALIAÇÃO: "))

            nota_total = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao

            # variável que verifica se os valores estão dentro do range das notas
            dues_exmaquina = 0 <= nota_aop1 <= 1.0 and 0 <= nota_aop2 <= 2.0 and 0 <= nota_aop3 <= 1.0 and 0 <= avaliacao <= 6.0

            """ se algum dos valores estiverem errados, é lançada uma exceção, 
                e o  usuário terá de repetir o processo 
            """
            if not dues_exmaquina:
                raise ValueError("A nota da AOP1 e AOP3 devem estar entre 0 e 1.0, AOP2 0 e 2.0 e AVALIAÇÃO 0 e 6.0.")
            

        except ValueError as e:
            print("Nota inválida:", e)

        else:
            break

    media_modulo = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao 

    if media_modulo < 7.0:
        print("O aluno está de recuperação! A média {:.2f} é insuficiente.".format(media_modulo))

        prova_final = float(input("Digite a nota da prova final do aluno #{}: ".format(i+1)))
        media_modulo = prova_final
    else:
        print("Aluno aprovado! Nota = ", media_modulo)

    lst_notas.append(media_modulo)

    i+=1
    # verifica qual o sistema operacional do usuário e limpa a tela
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# listas de aprovados e reprovados
lst_ap = []
lst_rep = []

for i in lst_notas:

    if i < 5.0:
        lst_rep.append(i)
    else:
        lst_ap.append(i)

""" o tamanho da lista com as notas dos aprovados e reprovados dirá quantos alunos obtiveram 
    resultado acima ou abaixo da média. Após isso, a porcentagem pode ser calculada.
"""
porcentagem_ap = (len(lst_ap) * 100) / alunos
procentagem_rep = 100 - porcentagem_ap

# soma as notas dos aprovados e reprovados, para calcular a média geral da turma
media_turma = sum(lst_ap + lst_rep) / alunos

print("De um total de {} alunos, {:.1f}% foram aprovados! E {:.1f}% foram reprovados".format(alunos, porcentagem_ap, procentagem_rep))
print("A média geral da turma é ", media_turma)
