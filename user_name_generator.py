# this will need json file and unique id's for each user if used in user database
def u_generator():
	'''Generates dict and username from user provided first and last name.
		Ex. first: tim, last: andes, username: tandes

	Input: User input required, no function arguments.
		Returns: Created username extracted from dict.'''
	user = {}
  
	# Input: Get user's first/last name
	u_input_first = input("What is your first name? ").lower()
	u_input_last = input("What is your last name? ").lower()
  
	# create dict entries for first / last name
	user["first"], user["last"] = u_input_first, u_input_last
	# create username using first / last name key-value pairs
	u_name = user['first'][0] + user['last']
	# save 'username' as third and final dictionary entry
	user["username"] = u_name
  
	# Output: Return and/or print
	# print(f"\nSuggested username: {user['username']}")
	return user["username"]

