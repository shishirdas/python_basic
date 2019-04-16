

class user:
	name = ''
	email = ''
	password = ''
	login = False

	def login(self):
		email= input("Enter your email:")
		password = input("Enter your password:")

		if email == self.email and password == self.password:
			login = True
			print("Login Successfully")
		else:
			print("Login failed!")

	def logout(self):
		login = False
		print("Logged out")

	def isLoggedIn(self):
		if self.login:
			return True
		else:
			return False
	def profile(self):
		
		if self.isLoggedIn():
			print(self.name,"\n",self.email)
		else:
			print("user is not Logged in")



user1 = user()
user1.name = "shishir"
user.email = "dasshishir@gmail.com"
user1.password = "12345"
user1.login()
user1.profile()
var = input()
			