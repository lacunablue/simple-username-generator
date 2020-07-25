# create empty dictionary for new user
user = {}

# get user's first and last name
u_input_first = input("What is your first name? ").lower()
u_input_last = input("What is your last name? ").lower()

# create dictionary entries for first / last name
user["first"], user["last"] = u_input_first, u_input_last
# create username using first / last name key-value pairs
u_name = user['first'][0] + user['last']
user["username"] = u_name

# output result to user
print(f"\nSuggested username: {user['username']}")