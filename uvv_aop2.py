import os
import time

try:
    """ pede ao usuário para digitar a quantidade de alunos do curso
        se nada for digitado ou for digitado um valor inválido, 100 será o número padrão
    """
    alunos = int(input("Digite a quantidade de alunos (o padrão é 100): "))
except:
    alunos = 100

print("Digite para AOP1 e AOP3 valores entre 0 e 1.0.")
print("Para AOP2 os valores válidos estão ente 0 e 2.0.")
print("A avaliação possui notas válidas entre 0 e 6.0. \n")

lst_notas = [] 
i=0
while(i<alunos):

    print("Digite as notas do aluno #{} \n".format(i+1))
   
 
    # Este laço garante que os valores digitados pelo usuário para as notas sejam coerentes
    while True:
        try:

            nota_aop1 = float(input("Nota AOP1 (entre 0 e 1.0): "))
            nota_aop2 = float(input("Nota AOP2 (entre 0 e 2.0): "))
            nota_aop3 = float(input("Nota AOP3 entre 0 e 1.0: "))
            avaliacao = float(input("Nota AVALIAÇÃO entre 0 e 6.0: "))

                # variável que verifica se os valores estão dentro do range das notas
            verifica_notas = 0 <= nota_aop1 <= 1.0 and 0 <= nota_aop2 <= 2.0 and 0 <= nota_aop3 <= 1.0 and 0 <= avaliacao <= 6.0

            """ se algum dos valores estiverem errados, é lançada uma exceção, 
                e o  usuário terá de repetir o processo 
            """
            if not verifica_notas:
                raise ValueError("A nota da AOP1 e AOP3 devem estar entre 0 e 1.0, AOP2 0 e 2.0 e AVALIAÇÃO 0 e 6.0.")
                    

        except ValueError as e:
            print("Nota inválida:", e)

        else:
            break

    media_modulo = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao 


    if media_modulo < 7.0:
        print("O aluno está de recuperação! A média {:.2f} é insuficiente.".format(media_modulo))

        # laço para verficar se a nota da avaliação é válida
        while True:

                try:
                    prova_final = float(input("Digite a nota da prova final do aluno #{}: ".format(i+1)))


                    if not 0 <= prova_final <= 10.0:
                        raise ValueError("A nota para avaliação deve estar entre 0 e 10.")
                        
                    elif prova_final < 5.0:
                        print("Aluno reprovado! A nota {:.1f} obtida na prova final é insuficiente.".format(prova_final))

                    else:
                        print("Aluno aprovado! Nota obtida na prova final foi de {:.1f}.".format(prova_final))

                    media_modulo = prova_final


                except ValueError as e:
                    print("Nota inválida:", e)

                else:
                    break

    else:
        print("Aluno aprovado! Nota = ", media_modulo)

    lst_notas.append(media_modulo)

    i+=1
    # espera 2s para o usuário ver o status do aluno
    time.sleep(2)
    # verifica qual o sistema operacional do usuário e limpa a tela
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# listas de aprovados e reprovados
lst_ap = []
lst_rep = []

""" percorre cada elemento da lista de notas, se esse for menor que 5 será adicionado a lista 
    de reprovados, se não, a nota é maior que 5, portanto é adicionado a lista de aprovados.
"""
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
