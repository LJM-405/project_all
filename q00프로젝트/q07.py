email="hong.gildong@exmple.com"
print(email.split('@'))
parts=email.split('@')
print(email.find('@'))
print(email[:email.find('@')],email[email.find('@')+1:])
print(parts[0].upper(),parts[1].replace(".com",""))