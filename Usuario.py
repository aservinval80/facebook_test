import requests
import json

class Usuario:
	nombre=""

	def __init__(self):
		self.url= "https://graph.facebook.com/v2.8/me"
		self.token="EAACEdEose0cBAHqF66PzxhZAeBLwe0pXHNAKP4DrKGArtOahZCCrZAhsRjdidZAkhJeZCIZBYACDSVT0RA2JZAfLAmECAgIYzRfS1D1Y58cVgr7f5tCV2WgLoAKTF57fg7lxWK2rhm8j1Rj0F5WVf6DwZC9LEJEkYw1tlQ5OGgXxsAZDZD"

	def obtenInformacion(self):
		parametros = {"access_token": self.token}
		resultado = requests.get(self.url, params=parametros).json()
		print(resultado)
		return resultado

