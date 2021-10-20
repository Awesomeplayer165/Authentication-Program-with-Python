class Evaluater:

	password = ""

	def __init__(self, password):
		self.password = password

	@property
	def hasAtLeast12Characters(self) -> bool:
		return len(self.password) >= 12

	@property
	def hasNumbers(self) -> bool:
		for char in self.password:
			try:    int(char); return True
			except: pass
		return False

	@property
	def hasSpecialCharacters(self) -> bool:
		for char in self.password:
			if char in ["!", "@", "#", "%", "^", "&", "~", "<", ">", "?", "/", "[", "]", ".", "|", "}", "{"]:
				return True
		
		return False

	def display(self):
		print("Your password", ("has" if self.hasAtLeast12Characters else "does not have"), end=" at least 12 characters\n")
		print("Your password", ("has" if self.hasNumbers             else "does not have"), end=" numbers\n")
		print("Your password", ("has" if self.hasSpecialCharacters   else "does not have"), end=" special characters\n")

eval = Evaluater(input("Enter a password: "))
eval.display()