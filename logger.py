# https://github.com/C0derByM4H6301
# Coded by M4H6301
import rich
import datetime
from rich.console import Console
from datetime import date
console = Console()
bugun = str(date.today())# dosyaya yazarken
filename="logs/"+str(date.today())+".log"
filemod="a"
sati = datetime.datetime.now().strftime("%H:%M:%S")
class yaz:
    def error(text):
        console.print(sati+" | "+"[bold][underline][red]ERROR[/][/][/] - "+"[bold][white]"+text+"[/][/]")
    
    def info(text):
        console.print(sati+" | "+"[bold][underline][blue]INFO[/][/][/] - "+"[bold][white]"+text+"[/][/]")

    def status(text):
        console.print(sati+" | "+"[bold][underline][yellow]STATUS[/][/][/] - "+"[bold][white]"+text+"[/][/]")


    # gerektimi yazar eklerim

def error(text, yazsin=False):
    f = open(filename, filemod)
    f.write("{"+sati+"}"+":"+"["+bugun+"] "+" - ERROR  - "+text+"\n")
    if yazsin == True:
        yaz.error(text)

def info(text, yazsin=False):
    f = open(filename, filemod)
    f.write("{"+sati+"}"+":"+"["+bugun+"] "+" - INFO   - "+text+"\n")
    if yazsin == True:
        yaz.info(text)

def status(text, yazsin=False):
    f = open(filename, filemod)
    f.write("{"+sati+"}"+":"+"["+bugun+"] "+" - STATUS - "+text+"\n")
    if yazsin == True:
        yaz.status(text)

# gerkti mi eklerim
