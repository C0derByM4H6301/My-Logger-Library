# https://github.com/C0derByM4H6301
# Log reader for my log files
from rich.console import Console
from rich.table import Table
import os
console = Console()


for fi in os.listdir("logs/"):
	tablo = Table(title="My Love software log file: "+fi)
	tablo.add_column("Day", style = "cyan")
	tablo.add_column("Current time", style= "green")
	tablo.add_column("Type", style = "magenta")
	tablo.add_column("Description" , style = "yellow")

	f = open("logs/"+fi , "r")
	days = []
	current_times = []
	states = []
	descti = []

	for i in f.readlines():
		#console.print(i[1:9])
		days.append(i[1:9])
		#console.print(i[12:22])
		current_times.append(i[12:22])
		#console.print(i[27:33])
		states.append(i[27:33])
		#console.print(i[36:])
		descti.append(i[36:])
	f.close()
	"""
	console.print(days)
	console.print(current_times)
	console.print(states)
	console.print(descti)
	"""

	for a in range(len(days)):
		tablo.add_row(days[a] , current_times[a] , states[a] , descti[a][0:-1])

	console.print(tablo)
