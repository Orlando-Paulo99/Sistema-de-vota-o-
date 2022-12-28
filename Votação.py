from rich import print
import os

back_end=0
front_end=0
nulos=0


while True:
	print("-" *30)
	print(f"[on blue]BackEnd:[/] {back_end}{os.linesep}[on purple]FrontEnd:[/] {front_end}{os.linesep} [on red]Nulos:[/] {nulos}")
	print("-"*30)
	try:
		voto=int(input(f"Qual você prefere?{os.linesep}1-BackEnd{os.linesep}2-FrontEnd{os.linesep}seu voto:"))
		
		if voto==1:
			back_end+=1
		elif voto==2:
			front_end+=1
		else:
			nulos+=1
	except:
		print("Digite apenas 1 ou 2")

	
	
