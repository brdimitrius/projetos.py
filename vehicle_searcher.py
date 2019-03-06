import requests
import re
import locale

getlang = locale.getdefaultlocale() # Lang
lang = (getlang[0]) # Lang

if lang == "pt_BR":
    langen = False
    langbr = True
    marca = input("Coloque a marca do carro aqui: ")
    modelo = input("Coloque o modelo do carro aqui: ")
elif lang != "pt_BR":
    langen = True
    langbr = False
    marca = input("Put the car brand here: ")
    modelo = input("Put your car model here: ")

if langbr == True:
    try:
        req = requests.get("https://www.icarros.com.br/"+marca+"/"+modelo)
        regex_nomes = re.findall("\w+ %s \w+ \w*" %(modelo),req.text)
        regex_preço = (re.findall("R\$ [0-9.]{1,10}",req.text))
        carro_nome = regex_nomes[0]
        carro_preço = regex_preço[0]
        preço = print("O carro %a foi encontrado no preço de %a"%(carro_nome,carro_preço))
    except:
        print("Ocorreu algum erro, reinicie o codigo")

elif langbr == False:
    try:
        req = requests.get("https://www.icarros.com.br/"+marca+"/"+modelo)
        regex_nomes = re.findall("\w+ %s \w+ \w*" %(modelo),req.text)
        regex_preço = (re.findall("R\$ [0-9.]{1,10}",req.text))
        carro_nome = regex_nomes[0]
        carro_preço = regex_preço[0]
        car_price1 = carro_preço.replace(".", "")
        car_price2 = car_price1.replace("R", "")
        car_price3 = car_price2.replace("$", "")
        car_price = int(car_price3)
        calc1 = (car_price / 4)
        calc11 = str(calc1)
        calc2 = calc11.replace(".0", "")
        calc22 = calc2.replace("5", "5.")
        calc = calc22
        preço = print("The %a was found for the price of %a"%(carro_nome,calc))
    except:
        print("Something went wrong, contact the developer")
