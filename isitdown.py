import sys
import requests
import locale
import getpass
import time
from socket import *

getlang = locale.getdefaultlocale() # Lang
lang = (getlang[0]) # Lang

namepc = getpass.getuser()
name = (namepc.title())

if lang != "pt_BR":
    print("Is it down?")
    time.sleep(1)
    print("")
    site = input("Hello, " + name + ", paste here the url (with https:// or http:// : ")
    print("")
    try:
        requestt = requests.get(site)
        status = requestt.status_code
        if status == 404:
            time.sleep(2)
            print("This site looks down")
        elif status == 200:
            time.sleep(2)
            print("The website is working correctly! :)")
        elif status == 204:
            time.sleep(2)
            print("It looks like this site is empty: O")
        elif status == 205:
            time.sleep(2)
            print("It looks like this site is empty: O")
        elif status == 306:
            time.sleep(2)
            print("The site has changed its proxy")
        elif status == 308:
            time.sleep(2)
            print("The site has changed url")
        elif status != 200 or status != 204 or status != 205 or status != 306 or status != 308 or status != 404:
            print("the site aswered with the code:" + status + ", this code is not in our system, probably the site is not available")
    except:
        print("Error, Invalid URL")
elif lang == "pt_BR":
    print("Esse Site Caiu?")
    time.sleep(1)
    print("")
    site = input("Ola, " + name + ", cole aqui a url do site (com https:// ou http:// : ")
    print("")
    try:
        requestt = requests.get(site)
        status = requestt.status_code
        if status == 404:
            time.sleep(2)
            print("O site caiu :(")
            time.sleep(2)
            pergdel = input("Gostaria de ver mais detalhes da conexao [s/n]?")
            time.sleep(2)
            if pergdel == "s":
                print(
                    "O recurso requisitado não foi encontrado, mas pode ser disponibilizado novamente no futuro. As solicitações subsequentes pelo cliente são permitidas.")
            elif pergdel == "n":
                sys.exit()
        elif status == 200:
            time.sleep(2)
            print("O site esta funcionando corretamente! :)")
            print("")
            time.sleep(2)
            pergdel = input("Gostaria de ver mais detalhes da conexao [s/n]? ")
            if pergdel == "s":
                print("")
                print("Esta classe de códigos de status indica a ação solicitada pelo cliente foi recebida, compreendida, aceita e processada com êxito. ")
            elif pergdel == "n":
                print("")
                print("Ok")
        elif status == 204:
            time.sleep(2)
            print("Parece que este site esta vazio :O")
            print("")
        elif status == 205:
            time.sleep(2)
            print("Parece que este site esta vazio :O")
            print("")
        elif status == 306:
            time.sleep(2)
            print("O Site mudou de proxy")
            print("")
        elif status == 308:
            time.sleep(2)
            print("O Site mudou de url")
            print("")
        else:
            if status != 200 or status != 204 or status != 205 or status != 306 or status != 308 or status != 404:
                print("O site respondeu com o codigo: " + status + ", este código não está em nosso sistema, provavelmente o site não está disponível")
    except:
        print("Erro, URL invalida")

#Created By: Braian Dimitrius
#Criado Por Braian Dimitrius