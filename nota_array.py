
def seq_array_notas(lst):
    while True:
        try:
            for nota in lst:

                nota_aop1 = nota[0]
                nota_aop2 = nota[1]
                nota_aop3 = nota[2]
                avaliacao = nota[3]


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

