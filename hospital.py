import sys
paciente1 = {"Nome" : "","Idade" : "", "Estado Clínico" : ""}

nome_paciente1 = input("Insira o nome do paciente : ")
paciente1["Nome"] = nome_paciente1

idade_paciente2 = input("Insira a idade do paciente : ")
paciente1["Idade"] = idade_paciente2
if idade_paciente2 >= "100":
    print("O paciente aparenta estar morto")
    sys.exit()



estcli_paciente1 = input("O paciente está doente ? ")
if estcli_paciente1 == "Sim" or estcli_paciente1 == "sim":
    paciente1["Estado Clínico"] = "Doente"
elif estcli_paciente1 == "Não" or estcli_paciente1 == "não":
    paciente1["Estado Clínico"] = "Saúdavel"



print("Nome :",paciente1["Nome"])
print("Idade :",paciente1["Idade"])
print("Estado Clínico :",paciente1["Estado Clínico"])


paciente1_validacao = input("Os dados fornecidos estão corretos ? ")
if paciente1_validacao == "Sim" or paciente1_validacao == "sim":
    print("Ok")

elif paciente1_validacao == "Não" or paciente1_validacao == "não":
    paciente1_pergunta = input("Gostaria de fazer alguma correção ? ")


    if paciente1_pergunta == "Sim" or paciente1_pergunta == "sim":

        paciente1_pergunta2 = input("Gostaria de fazer a alteração no Nome,Idade ou Estado Clínico ? ")
        if paciente1_pergunta2 == "Nome" or paciente1_pergunta2 == "nome":
            paciente1_renome = input("Re-insira o nome do paciente : ")
            paciente1["Nome"] = paciente1_renome
            print("Nome :", paciente1["Nome"])

            paciente1_nomeper = input("O nome do paciente está correto ? ")
            if paciente1_nomeper == "Sim" or paciente1_nomeper == "sim":
                print("Ok")


            elif paciente1_nomeper == "Não" or paciente1_nomeper == "não":
                print("Ok")
                paciente1_renome2 = input("Re-insira o nome do paciente : ")
                paciente1["Nome"] = paciente1_renome2
                print("Nome :", paciente1["Nome"])


        elif paciente1_pergunta2 == "Idade" or paciente1_pergunta2 == "idade":
            paciente1_reidade = input("Re-insira a idade do paciente : ")
            paciente1["Idade"] = paciente1_reidade
            print("Idade :", paciente1["Idade"])
            paciente1_idadeper = input("A idade do paciente está correta ? ")

            if paciente1_idadeper == "Sim" or paciente1_idadeper == "sim":
                print("Ok")

            elif paciente1_idadeper == "Não" or paciente1_idadeper == "não":
                print("Ok")
                paciente1_reidade2 = input("Re-insira a idade do paciente : ")
                paciente1["Idade"] = paciente1_reidade2


        elif paciente1_pergunta2 == "Estado Clínico" or paciente1_pergunta2 == "Estado Clinico" or paciente1_pergunta2 == "estado clínico" or paciente1_pergunta2 == "estado clinico":
            paciente1_reestcli = input("Re-insira o estado clínico do paciente : ")

            if paciente1_reestcli == "Doente" or paciente1_reestcli == "doente":
                paciente1["Estado Clínico"] = "Doente"
                print("Estado Clínico :", paciente1["Estado Clínico"])

            elif paciente1_reestcli == "Saúdavel" or paciente1_reestcli == "saudavel" or paciente1_reestcli == "Saudavel" or paciente1_reestcli == "saúdavel":
                paciente1["Estado Clínico"] = "Saúdavel"
                print("Estado Clínico :", paciente1["Estado Clínico"])


            paciente1_estper = input("O estado clínico está correto ? ")
            if paciente1_estper == "Sim" or paciente1_estper == "sim":
                print("Ok")


            elif paciente1_estper == "Não" or paciente1_estper == "não":
                print("Ok")
                paciente1_estcli2 = input("Re-insira o Estado clinico do paciente : ")

                if paciente1_estcli2 == "Doente" or paciente1_estcli2 == "doente":
                    paciente1["Estado Clínico"] = "Doente"
                    print("Estado Clínico :", paciente1["Estado Clínico"])

                elif paciente1_estcli2 == "Saúdavel" or paciente1_estcli2 == "saudavel" or paciente1_estcli2 == "Saudavel" or paciente1_estcli2 == "saúdavel":
                    paciente1["Estado Clínico"] = "Saúdavel"
                    print("Estado Clínico :", paciente1["Estado Clínico"])


        paciente1_pergunta22 = input("Gostaria de fazer mais alguma correção ? ")
        if paciente1_pergunta22 == "Não" or paciente1_pergunta22 == "nao":
            print("Ok")


        elif paciente1_pergunta22 == "Sim" or paciente1_pergunta22 == "sim":
            paciente1_pergunta23 = input("Gostaria de fazer a alteração no Nome,Idade ou Estado Clínico ? ")

            if paciente1_pergunta23 == "Nome" or paciente1_pergunta23 == "nome":
                paciente1_renome = input("Re-insira o nome do paciente : ")
                paciente1["Nome"] = paciente1_renome
                print("Nome :", paciente1["Nome"])
                paciente1_nomeper = input("O nome do paciente está correto ? ")

                if paciente1_nomeper == "Sim" or paciente1_nomeper == "sim":
                    print("Ok")

                elif paciente1_nomeper == "Não" or paciente1_nomeper == "não":
                    print("Ok")
                    paciente1_renome2 = input("Re-insira o nome do paciente : ")
                    paciente1["Nome"] = paciente1_renome2
                    print("Nome :", paciente1["Nome"])


            elif paciente1_pergunta23 == "Idade" or paciente1_pergunta23 == "idade":
                paciente1_reidade = input("Re-insira a idade do paciente : ")
                paciente1["Idade"] = paciente1_reidade
                print("Idade :", paciente1["Idade"])
                paciente1_idadeper = input("A idade do paciente está correta ? ")

                if paciente1_idadeper == "Sim" or paciente1_idadeper == "sim":
                    print("Ok")
                elif paciente1_idadeper == "Não" or paciente1_idadeper == "não":

                    print("Ok")
                    paciente1_reidade2 = input("Re-insira a idade do paciente : ")
                    paciente1["Idade"] = paciente1_reidade2


            elif paciente1_pergunta23 == "Estado Clínico" or paciente1_pergunta23 == "Estado Clinico" or paciente1_pergunta23 == "estado clínico" or paciente1_pergunta23 == "estado clinico":
                paciente1_reestcli = input("Re-insira o estado clínico do paciente : ")

                if paciente1_reestcli == "Doente" or paciente1_reestcli == "doente":
                    paciente1["Estado Clínico"] = "Doente"
                    print("Estado Clínico :", paciente1["Estado Clínico"])

                elif paciente1_reestcli == "Saúdavel" or paciente1_reestcli == "saudavel" or paciente1_reestcli == "Saudavel" or paciente1_reestcli == "saúdavel":
                    paciente1["Estado Clínico"] = "Saúdavel"
                    print("Estado Clínico :", paciente1["Estado Clínico"])

                paciente1_estper = input("O estado clínico está correto ? ")

                if paciente1_estper == "Sim" or paciente1_estper == "sim":
                    print("Ok")

                elif paciente1_estper == "Não" or paciente1_estper == "não":
                    print("Ok")

                    paciente1_estcli2 = input("Re-insira o Estado clinico do paciente : ")
                    if paciente1_estcli2 == "Doente" or paciente1_estcli2 == "doente":
                        paciente1["Estado Clínico"] = "Doente"
                        print("Estado Clínico :", paciente1["Estado Clínico"])

                    elif paciente1_estcli2 == "Saúdavel" or paciente1_estcli2 == "saudavel" or paciente1_estcli2 == "Saudavel" or paciente1_estcli2 == "saúdavel":
                        paciente1["Estado Clínico"] = "Saúdavel"
                        print("Estado Clínico :", paciente1["Estado Clínico"])


        paciente1_pergunta24 = input("Gostaria de fazer mais alguma correção ? ")
        if paciente1_pergunta24 == "Não" or paciente1_pergunta24 == "nao":
            print("Ok")

        elif paciente1_pergunta24 == "Sim" or paciente1_pergunta24 == "sim":
            paciente1_pergunta25 = input("Gostaria de fazer a alteração no Nome,Idade ou Estado Clínico ? ")

            if paciente1_pergunta25 == "Nome" or paciente1_pergunta2 == "nome":
                paciente1_renome = input("Re-insira o nome do paciente : ")
                paciente1["Nome"] = paciente1_renome
                print("Nome :", paciente1["Nome"])
                paciente1_nomeper = input("O nome do paciente está correto ? ")

                if paciente1_nomeper == "Sim" or paciente1_nomeper == "sim":
                    print("Ok")

                elif paciente1_nomeper == "Não" or paciente1_nomeper == "não":
                    print("Ok")
                    paciente1_renome2 = input("Re-insira o nome do paciente : ")
                    paciente1["Nome"] = paciente1_renome2
                    print("Nome :", paciente1["Nome"])


            elif paciente1_pergunta25 == "Idade" or paciente1_pergunta25 == "idade":
                paciente1_reidade = input("Re-insira a idade do paciente : ")
                paciente1["Idade"] = paciente1_reidade
                print("Idade :", paciente1["Idade"])
                paciente1_idadeper = input("A idade do paciente está correta ? ")

                if paciente1_idadeper == "Sim" or paciente1_idadeper == "sim":
                    print("Ok")

                elif paciente1_idadeper == "Não" or paciente1_idadeper == "não":
                    print("Ok")
                    paciente1_reidade2 = input("Re-insira a idade do paciente : ")
                    paciente1["Idade"] = paciente1_reidade2


            elif paciente1_pergunta25 == "Estado Clínico" or paciente1_pergunta25 == "Estado Clinico" or paciente1_pergunta25 == "estado clínico" or paciente1_pergunta25 == "estado clinico":
                paciente1_reestcli = input("Re-insira o estado clínico do paciente : ")
                if paciente1_reestcli == "Doente" or paciente1_reestcli == "doente":
                    paciente1["Estado Clínico"] = "Doente"
                    print("Estado Clínico :", paciente1["Estado Clínico"])

                elif paciente1_reestcli == "Saúdavel" or paciente1_reestcli == "saudavel" or paciente1_reestcli == "Saudavel" or paciente1_reestcli == "saúdavel":
                    paciente1["Estado Clínico"] = "Saúdavel"
                    print("Estado Clínico :", paciente1["Estado Clínico"])
                paciente1_estper = input("O estado clinico está correto ? ")

                if paciente1_estper == "Sim" or paciente1_estper == "sim":
                    print("Ok")

                elif paciente1_estper == "Não" or paciente1_estper == "não":
                    print("Ok")
                    paciente1_estcli2 = input("Re-insira o Estado clinico do paciente : ")

                    if paciente1_estcli2 == "Doente" or paciente1_estcli2 == "doente":
                        paciente1["Estado Clínico"] = "Doente"
                        print("Estado Clínico :", paciente1["Estado Clínico"])

                    elif paciente1_estcli2 == "Saúdavel" or paciente1_estcli2 == "saudavel" or paciente1_estcli2 == "Saudavel" or paciente1_estcli2 == "saúdavel":
                        paciente1["Estado Clínico"] = "Saúdavel"
                        print("Estado Clínico :", paciente1["Estado Clínico"])
print("Ficha do Paciente",paciente1["Nome"],":")
print("     Nome :",paciente1["Nome"])
print("     Idade :",paciente1["Idade"])
print("     Estado Clínico :",paciente1["Estado Clínico"])