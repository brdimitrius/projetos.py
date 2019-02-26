import requests
import json
cidade = input("Digite a cidade que voce deseja verificar o clima : ")
api = input("Se voce possui uma api key no site openweathermap insira aqui, ou, se voce deseja usar a api padrao digite apip : ")
if api == "apip":
    api = "917638e8d00e6c4d466f24b8befcee61"
req = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cidade+"&APPID="+api)

#Verificar Hora
#reqhora = requests.get("https://www.amdoren.com/api/timezone.php?api_key=JY57P6SBYJuts2HiFRPrszNXBs2rzN&loc="+cidade)

#hora1 = json.loads(reqhora.text)
#hora2 = hora1['time']
#print("Hora de",cidade,":",hora2)

tempo = json.loads(req.text)

temperatura_req = int((tempo['main']['temp']))

temp2 = str(temperatura_req - 273.15)
temperatura = (temp2 + "°C")
print("Temperatura :",temperatura)
clima = (tempo['weather'][0]["main"])
if clima == "Clouds":
    clima2 = "Ceu limpo"
elif clima == "Haze":
    clima2 = "Neblina"
elif clima == "Gray":
    clima2 = 'Nublado'
elif clima == "Cloudy":
    clima2 = "Céu limpo com períodos nublados"
elif clima == "Sunny":
    clima2 = "Ensolarado"
elif clima == "Mainly sun":
    clima2 = "Sol entre as nuvens"
elif clima == "Overcast":
    clima2 = "Nublado"
elif clima == "Foggy":
    clima2 = "Nevoeiro"
elif clima == "Snowy" or clima == "Snow":
    clima2 = "Neve"
elif clima == "Sun and rain":
    clima2 = "Sol e chuva"
elif clima == "Rainy":
    clima2 = "Chuvoso"
elif clima == "Windy":
    clima2 = "Ventos fortes"
elif clima == "Stormy":
    clima2 = "Tempestuoso"
elif clima == "Rain":
    clima2 = "Chuvoso"
elif clima == "Heavy sea":
    clima2 = "Mar agitado"
elif clima == "Clear":
    clima2 = "Limpo"
elif clima == "Hot":
    clima2 = "Quente"
elif clima == "Could":
    clima2 = "Frio"
elif clima == "Wet":
    clima2 = "Umido"
elif clima == "Drizzling":
    clima2 = "Chuviscando/Garoa"
else:
    print(clima)
#CLIMA
print("Clima :",clima2)

#Umidade
umi = str(tempo['main']['humidity'])
umidade = ((umi)+"%")

print("Umidade :",umidade)

#Temperatura minima
temperatura_min_request = tempo['main']['temp_min']
temp_min_calc = str(temperatura_min_request - 273.15)
temperatura_mininima = (temp_min_calc+"°C")

print("Temperatua minima :",temperatura_mininima)

#Temperatura maxima
temperatura_max_request = tempo['main']['temp_max']
temp_max_calc = str(temperatura_max_request - 273.15)
temp_maxima = (temp_max_calc+"°C")

print("Temperatura maxima :",temp_maxima)