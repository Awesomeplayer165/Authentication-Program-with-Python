# Evaluater.py

class Evaluater:

	password: str = ""
	name:     str = ""
	username: str = ""

	def __init__(self, password: str, name: str, username: str):
		self.password = password
		self.name     = name
		self.username = username

	@property
	def hasNumbers(self) -> bool:
		for char in self.password:
			try:    int(char); return True
			except: pass
		return False

	@property
	def hasSpecialCharacters(self) -> bool:
		for char in self.password:
			if char in ["!", "@", "#", "%", "^", "&", "~", "<", ">", "?", "/", "[", "]", ".", "|", "}", "{"]: return True

		return False

	@property
	def hasAtLeast12Characters(self)    -> bool: return len(self.password) >= 12

	@property
	def hasCapitalLetters(self)         -> bool: return any(i.isupper() for i in self.password)

	@property
	def hasLowercaseLetters(self)       -> bool: return any(i.islower() for i in self.password)

	@property
	def containsName(self)              -> bool: return self.name.lower() in self.password.lower()

	@property
	def containsLiterallyPassword(self) -> bool: return self.password.lower() == "password"

	@property
	def containsUsername(self)          -> bool: return self.username.lower() in self.password.lower()

	@property
	def hasMoreThan100Characters(self)  -> bool: return len(self.password) > 100

	def display(self):
		print("Your password", ("has"  if self.hasAtLeast12Characters    else "*does not have"), end=" at least 12 characters\n")
		print("Your password", ("has"  if self.hasNumbers                else "*does not have"), end=" numbers\n")
		print("Your password", ("has"  if self.hasSpecialCharacters      else "*does not have"), end=" special characters\n")
		print("Your password", ("has"  if self.hasCapitalLetters         else "*does not have"), end=" capital letters\n")
		print("Your password", ("*has" if self.containsName              else "does not have"),  end=" your name in it\n")
		print("Your password", ("*has" if self.containsLiterallyPassword else "does not have"),  end=" literally password in it\n")
		print("Your password", ("*has" if self.containsUsername          else "does not have"),  end=" your username in it\n")
		print("Your password", ("*has" if self.hasMoreThan100Characters  else "does not have"),  end=" more than 100 characters\n")
		
		print(f"Total number of problems with password = {(not self.hasAtLeast12Characters) + (not self.hasNumbers) + (not self.hasSpecialCharacters) + (not self.hasCapitalLetters) + (not self.hasLowercaseLetters) + self.containsName + self.containsLiterallyPassword + self.containsUsername + self.hasMoreThan100Characters}")