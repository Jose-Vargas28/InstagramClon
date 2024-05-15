#Instagram

print("Instagram")

user = input("Phone number, username or email")
password = input("Password")

if user == "Byron" and password == "123":
    print(f'Welcome {user}')
    print("Loading your post")
else:
    print("Sorry, your password was incorrect. Please double-check ypur password.")

print("Sing up to see photos and videos from your friends.")
input("Log in with Facebook")
facebook=input("Yes or No")
if facebook == "si":
    print("Welcome")
else:
    mobile=input("Mobile number or email")
    name=input("Full name")
    username=input("Username")            
    password=input("password")            
