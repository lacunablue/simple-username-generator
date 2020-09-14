# simple_username_generator
Summary: An <i>extremely</i> simple username generator based off of first and last name inputs.

Instructions for vanilla version:
- Note: This assumes you are familiar with IDE/Terminal use

1. This is a console/terminal only program currently, created using PyCharm
2. Open in an IDE or terminal
3. Run file (Shift + F10 in PyCharm, F5 in Spyder)
4. Invoke function ```u_generator()``` or import (see example below)
5. Type in first name
6. Type in last name
7. Inputs will be added as first, last, and username key-value pairs to dictionary
8. Username will be returned, OR uncomment print() for username to print to user

## Import example:

```
import json
import user_name_generator as ung
  
# load username if stored previously. if not, prompt for username and store
filename = 'username.json'

try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = ung.u_generator()
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"Account created; username '{username}' saved.")
else:
	print(f"Welcome back, {username}!")
```

TO DO
- [X] Turn into function and / or module
- [ ] Set this up so n amount of users can be saved to dictionary file (JSON?)
- [ ] Error handling
- [ ] If username already exists, suggest secondary, tertiary
- [ ] Research security best practices for storing user data
- [ ] Implement security research
