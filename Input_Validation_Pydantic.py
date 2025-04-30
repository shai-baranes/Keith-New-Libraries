############################################################
# previously - python allow args with text (str) instead of float value - no issues what so ever
############################################################
class Account:
	"""docstring for Account"""
	def __init__(self, name: str, balance: float):
		self.name = name
		self.balance = balance




if __name__ == "__main__":
	account = Account(name="John", balance="Hello")
	print(account.name)
	print(account.balance)


print()

############################################################
# now - python prevents args with text (str) when typehints suggest Float
############################################################


from pydantic import BaseModel, field_validator, SecretStr

class Account(BaseModel):
	name: str
	balance: float
	password: SecretStr
	# password: str

	@field_validator("balance")
	def balance_must_be_positive(cls, value):
		if value < 0:
			raise ValueError("balance must be positive")
		else:
			return value

if __name__ == "__main__":
	account = Account(name="John", balance=5.0, password="1234") ## >> Value error, balance must be positive
	# account = Account(name="John", balance=-5.0, password=1234) ## >> Value error, balance must be positive
	# account = Account(name="John", balance="Hello") ## >> Input should be a valid number, unable to parse string as a number (upon: balance="Hello")

	account.balance = -100 # it works fine if defined after class instantiation

	print(account.name)
	print(account.balance)
	print(account.password) # **********


print()



############################################################
# now python prevents plugin negative also after the class instantiation
############################################################


class Account(BaseModel, validate_assignment=True):
	name: str
	balance: float
	# password: str

	@field_validator("balance")
	def balance_must_be_positive(cls, value):
		if value < 0:
			raise ValueError("balance must be positive")
		else:
			return value

if __name__ == "__main__":
	account = Account(name="John", balance=5.0) ## >> Value error, balance must be positive

	account.balance = 100
	# account.balance = -100 # it works fine if defines after class instantiation unless adding the 'validate_assignment=True'

	print(account.name)
	print(account.balance)


print()

############################################################
# now python prevents TBD
############################################################

from pydantic import Field

class Account(BaseModel, validate_assignment=True):
	name: str = Field(..., min_length=3, max_length=50, frozen=True)
	balance: float
	# password: str

	@field_validator("balance")
	def balance_must_be_positive(cls, value):
		if value < 0:
			raise ValueError("balance must be positive")
		else:
			return value

if __name__ == "__main__":
	account = Account(name="Al", balance=5.0) ## >> "String should have at least 3 characters"


	print(account.name)
	print(account.balance)

	# note also that you won't be able to change the name after been assigned