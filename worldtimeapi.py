import requests
import json
import locale

getlang = locale.getdefaultlocale()
lang = (getlang[0])
if lang == "pt_BR":
    cidade = input("Digite a cidade que voce deseja verificar o clima : ")
    api = input("Cole aqui sua api do site amdoren: ")
elif lang != "pt_BR":
    cidade = input("Enter a city you want to discover the weather:")
    api = input("Paste your amdoren site API here: ")
req2 = requests.get("https://www.amdoren.com/api/timezone.php?api_key="+api+"&loc="+cidade)
hora1 = json.loads(req2.text)
hora2 = hora1['time']
if lang == "pt_BR":
    print("Hora de %a : %a"%(cidade,hora2))
elif lang != "pt_BR":
    print("Time of %a : %a"%(city,hora2))