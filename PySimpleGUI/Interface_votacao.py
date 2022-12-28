import PySimpleGUI as sg

def login():
	sg.theme("DarkBlue15")
	t_login=[
		[sg.Text("Nome Completo")],
		[sg.Input(key="name",size=(12,1))],
		[sg.Text("Rg")],
		[sg.Input(key="n_rg",size=(12,1))],
		[sg.Text("Titulo")],
		[sg.Input(key="n_titulo",size=(12,1))],
		[sg.Button("Entrar")]
	]
	return sg.Window("Faça seu login",t_login,finalize=True)
	
def votos():
	sg.theme("DarkBlue15")
	t_votos=[
		[sg.Text(" ",key="r_back"),sg.Text(" ",key="r_front")],
		[sg.Text("1-Back"),sg.Text("2-Front")],
		[sg.Input(key="digi",size=(12,1))],
		[sg.Button("Reset"),sg.Button("Nulo"),sg.Button("Confirmar")]
	]
	return sg.Window("Faça seu voto",t_votos,finalize=True,size=(500,300))
	
#janelas
jan_login,jan_votos=login(),None
#loop
while True:
		window,event,values=sg.read_all_windows()
		#EVENTO PARA FECHAR TELA DE LOGIN
		if window==jan_login and event==sg.WIN_CLOSED:
			break
		#EVENTO PARA IR PARA TELA DE VOTOS
		if window==jan_login and event=="Entrar":
			jan_votos=votos()
			jan_login.hide()
			
		#EVENTO PARA RESETAR O SISTEMA
		if window==jan_votos and event=="Reset":
			sg.popup("Programa resetato")
			break
