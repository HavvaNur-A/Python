import re
characters=["\\?","\\*","\\!","\\%","\\&","\\=","\\#","\\.","\\;","\\{","\\}","\\_","\\)","\\("]
birthDay = input("Enter your birthday (in YYYY format): ")

def Control(password):
    if len(password)<8:
        raise Exception("Password must be at least 8 charachters long!")
    elif not re.search("[a-z]",password):  
        raise Exception("Password must include at least one lowercase letter!")
    elif not re.search("[A-Z]",password):
        raise Exception("Password must include at least one uppercase letter!")
    elif not re.search("[0-9]",password):
        raise Exception("Password must include at least one number!")
    elif not re.search(str(characters),password):
        raise Exception("Password must include at least one special character!")
    elif birthDay in password:
        raise Exception("Password must not contain your birtday!")
    elif re.search("\\d{2,}",password): 
        numbers=re.findall("\\d+",password)
        for number in numbers:
            if ''.join(sorted(number)) == number:
                raise Exception("Password must not contain consective numbers!")
    print("Your password is created successfully...")  

print("ATTENTİON!\n-Password must be at least 8 characters\n-Password include at least one lowercase letter,uppercase letter,number,special character\n Password-must not include your birtday\n-Password must not contain consective")
while True:
        try:
            password=input("Please create your password: ")
            Control(password)
        except Exception as Error:
            print(Error)
        else:
            break
