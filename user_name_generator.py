user = {}

# get name
u_input_first = input("What is your first name? ").lower()
u_input_last = input("What is your last name? ").lower()

# create username
user["first"], user["last"] = u_input_first, u_input_last
u_name = user['first'][0] + user['last']
user["username"] = u_name

# output to user
print(f"\nSuggested username: {user['username']}")
