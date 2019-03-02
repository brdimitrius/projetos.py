import requests
import re
#padrao = (re.findall('3,\w\w',req.text))
reqdolar = requests.get("https://dolarhoje.com/")
regexdolar = (re.findall('R\$ (\d,\d{2})',reqdolar.text))
reqeuro = requests.get("https://dolarhoje.com/euro-hoje/")
regexeuro = (re.findall("R\$ (\d,\d{2})", reqeuro.text))
valoreurocomercial = regexeuro[4]
valoreuroturismo = regexeuro[1]
valordolarcomercial = regexdolar[4]
valordolarturismo = regexdolar[1]

int_valor_euroturis = float(valoreuroturismo.replace(',','.'))
int_valor_eurocomer = float(valoreurocomercial.replace(",","."))
int_valor_dollarcomer = float(valordolarcomercial.replace(',', '.'))
int_valor_dollarturis = float(valordolarturismo.replace(',','.'))

conv = input("CONVERSOR DE MOEDAS\nMOEDAS DISPONIVEIS :\n   DOLAR\n   EURO\nDeseja converter euro ou dolar ? : ")
if conv == "dolar":
    print("Valor do dolar comercial : R$%a"%(int_valor_dollarcomer))
    print("Valor do dolar turismo (Baseado no maior valor) : R$%a"%(int_valor_dollarturis))
    perg_convdol = input("Opçoes:\n[1] : Converter Dolares para reais\n[2] : Converter Reais Para Dolares\nDigite a sua opçao [1/2] : ")
    if perg_convdol == "1":
        perg_qual1 = input("Voce deseja converter dolar comercial ou dolar turismo para real? : ")
        if perg_qual1 == "comercial" or perg_qual1 == "comerciais" or perg_qual1 == "dolar comercial" or perg_qual1 == "dolares comerciais":
            perg_dollarcomer = int((input("Digite quantos dolares comerciais voce deseja converter para reais : ")))

            perg_int_dollarcomer = int(perg_dollarcomer)
            conver_dollar = (int_valor_dollarcomer * perg_int_dollarcomer)
            print("%s dolares custam %s reais"%(perg_dollarcomer,conver_dollar))
        elif perg_qual1 == "turismo" or perg_qual1 == "turismos" or perg_qual1 == "dolar turismo" or perg_qual1 == "dolares turismos" or perg_qual1 == "dolares turismos":
            perg_dollarturis = int((input("Digite quantos dolares de turismo voce deseja converter para reais : ")))
            perg_int_dollarturis = int(perg_dollarturis)
            conver_dollarturis = (int_valor_dollarturis * perg_int_dollarturis)
            print("%s dolares custam %s reais"%(perg_dollarturis,conver_dollarturis))
    elif perg_convdol == "2":
        perg_qual2 = input("Voce deseja converter reais para dolar comercial ou dolar turismo? : ")
        if perg_qual2 == "comercial" or perg_qual2 == "comerciais" or perg_qual2 == "dolar comercial" or perg_qual2 == "dolares comerciais":
            perg_dollareal = int((input("Digite quantos reais voce deseja converter para dolares comerciais : ")))
            perg_int_dollareal = int(perg_dollareal)
            conver_dollar2 = (perg_int_dollareal / int_valor_dollarcomer)
            print("%s reais custam %s dolares"%(perg_int_dollareal,conver_dollar2))
        if perg_qual2 == "turismo" or perg_qual2 == "turismos" or perg_qual2 == "dolar turismo" or perg_qual2 == "dolares turismos" or perg_qual2 == "dolares turismo":
            perg_dollarealturi = int((input("Digite quantos reais voce deseja converter para dolares de turismo : ")))
            perg_int_dollarealturi = int(perg_dollarealturi)
            conver_dollar2 = (perg_int_dollarealturi / int_valor_dollarturis)
            print("%s reais custam %s dolares de turismo" % (perg_int_dollarealturi, conver_dollar2))
elif conv == "euro" or conv == "EURO" or conv == "Euro":
    print("Valor Euro Comercial : R$%a"%(int_valor_eurocomer))
    print("Valor Euro Turismo (Baseado no maior valor) : R$%a"%(int_valor_euroturis))
    perg_conveuro = input("Opçoes:\n[1] : Converter Euro para reais\n[2] : Converter Reais Para Euro\nDigite a sua opçao [1/2] : ")
    if perg_conveuro == "1":
        perg_qualcteuro = input("Voce deseja converter euro comercial ou euro turismo para real? : ")
        if perg_qualcteuro == "comercial" or perg_qualcteuro == "comerciais" or perg_qualcteuro == "euro comercial" or perg_qualcteuro == "euros comerciais":
            perg_eurocomer = int((input("Digite quantos euros comerciais voce deseja converter para reais : ")))
            perg_int_eurocomer = int(perg_eurocomer)
            conver_euro = (int_valor_eurocomer * perg_int_eurocomer)
            print("%s euros custam %s reais"%(perg_eurocomer,conver_euro))#
        elif perg_qualtreuro == "turismo" or perg_qualtreuro == "turismos" or perg_qualtreuro == "euro turismo" or perg_qualtreuro == "euro turismos" or perg_qualtreuro == "dolares turismos":
            perg_euroturis = int((input("Digite quantos euros de turismo voce deseja converter para reais : ")))
            perg_int_euroturis = int(perg_euroturis)
            conver_dollarturis = (int_valor_euroturis * perg_int_euroturis)
            print("%s euros custam %s reais"%(perg_dollarturis,conver_dollarturis))
    elif perg_conveuro == "2":
        perg_qualeuro2 = input("Voce deseja converter reais para euro comercial ou reais para euro turismo? : ")
        if perg_qualeuro2 == "comercial" or perg_qualeuro2 == "comerciais" or perg_qualeuro2 == "euro comercial" or perg_qualeuro2 == "euros comerciais":
            perg_euroctreal = int((input("Digite quantos reais voce deseja converter para euros comerciais : ")))
            perg_int_euroctreal = int(perg_euroctreal)
            conver_euroct2 = (perg_int_euroctreal / int_valor_eurocomer)
            print("%s reais custam %s euros"%(perg_int_euroctreal,conver_euroct2))
        if perg_qualeuro2 == "turismo" or perg_qualeuro2 == "turismos" or perg_qualeuro2 == "dolar turismo" or perg_qualeuro2 == "dolares turismos" or perg_qualeuro2 == "dolares turismo":
            perg_eurorealtr = int((input("Digite quantos reais voce deseja converter para dolares de turismo : ")))
            perg_int_eurorealtr = int(perg_eurorealtr)
            conver_eurotrreal = (perg_int_eurorealtr / int_valor_euroturis)
            print("%s reais custam %s euros"%(perg_int_eurorealtr,conver_eurotrreal))