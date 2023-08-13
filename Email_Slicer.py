email = input("Enter your email id: ").strip()

user_name = email[:email.index('@')]
domain= email[email.index('@')+1:]

print(f'User name is {user_name} amd your domain is {domain}')