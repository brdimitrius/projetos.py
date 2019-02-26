import re
import requests
site = input("Digite o site voce deseja verificar a existencia de e-mails: ")
req_mail = requests.get(site)
regex_mail = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req_mail.text)


count_mail = len(regex_mail)
if count_mail >= 1:
    print("Foram encontrados %a e-mails"%(count_mail))
    print("E-mails encontrados: %a"%(regex_mail))
#http://www.ccrmetrobahia.com.br/imprensa/contato