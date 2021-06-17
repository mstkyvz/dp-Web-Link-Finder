#coding:utf-8
from colorama import Fore,init
import requests
import time
import sys
import re
import os

linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])

print("""\033[91m
    .S_sSSs      sSSs    sSSs   .S_sSSs     .S     S.     sSSs   .S_SSSs    
   .SS~YS%%b    d%%SP   d%%SP  .SS~YS%%b   .SS     SS.   d%%SP  .SS~SSSSS   
   S%S   `S%b  d%S'    d%S'    S%S   `S%b  S%S     S%S  d%S'    S%S   SSSS  
   S%S    S%S  S%S     S%S     S%S    S%S  S%S     S%S  S%S     S%S    S%S  
   S%S    S&S  S&S     S&S     S%S    d*S  S%S     S%S  S&S     S%S SSSS%P  
   S&S    S&S  S&S_Ss  S&S_Ss  S&S   .S*S  S&S     S&S  S&S_Ss  S&S  SSSY   
   S&S    S&S  S&S~SP  S&S~SP  S&S_sdSSS   S&S     S&S  S&S~SP  S&S    S&S  
   S&S    S&S  S&S     S&S     S&S~YSSY    S&S     S&S  S&S     S&S    S&S  
   S*S    d*S  S*b     S*b     S*S         S*S     S*S  S*b     S*S    S&S  
   S*S   .S*S  S*S.    S*S.    S*S         S*S  .  S*S  S*S.    S*S    S*S  
   S*S_sdSSS    SSSbs   SSSbs  S*S         S*S_sSs_S*S   SSSbs  S*S SSSSP   
   SSS~YSSY      YSSP    YSSP  S*S         SSS~SSS~S*S    YSSP  S*S  SSY    
                               SP                               SP          
                               Y                                Y      

                   Created By Walker - DeepWeb Link Finder

                              ELITHATZ AR-GE

\033[0m""")
z = "         [+] \033[91m#################################################"+Fore.WHITE+" [+]\n"

for x in z:
   sys.stdout.write(x)
   sys.stdout.flush()
   time.sleep(0.03)
   
try:
   keyword = sys.argv[1]
except:
   exit(Fore.RED+"\n\n\n   [!] Kullanim : "+Fore.WHITE+" python "+sys.argv[0]+' "Anahtar Kelimeler"')
   
url = "https://ahmia.fi/search/?q="+keyword
r = requests.get(url)
links = re.findall(keyword+'&redirect_url=(.*?)">',r.text)
texts = re.findall("<p>(.*?)</p>", r.text)
num = len(links)
save = open(keyword+".txt", "w")

for i in range(num):
   print(Fore.RED+"\n [Link]-> "+Fore.WHITE+links[i])
   try:
     print(Fore.RED+" [Text]-> "+Fore.WHITE+texts[i])
   except:
      pass
   try:
     save.write("\n[Link]-> "+links[i]+"\n[Text]-> "+texts[i]+"\n")
   except:
     save.write("\n[Link]-> "+links[i]+"\n")

print(Fore.RED+"\n\n [+] "+Fore.WHITE+"Toplam "+str(num)+" link bulundu!\n")