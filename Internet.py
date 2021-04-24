import requests

class internet:
	def check():
		try:
			requests.get('https://ultrontheai.github.io/SwarajPuppalwarUpdate/main.html')
			return 'online'
		except:
			return 'ofline'
	def show():
		print(internet.check())
internet.show()
