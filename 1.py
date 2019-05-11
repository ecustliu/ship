class Adress():
	detail = '广州'
	post_code = 110
	def info(self):
		print("Adress: ",self.detail)
		print("post_code :",self.post_code)


print(Adress.detail)
a = Adress()
a.info()
a.detail = "北京"
a.post_code = 100
a.info()