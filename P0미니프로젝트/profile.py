student={'name':'김민준','age':20,'major':'컴퓨터공학'}
del student['major']
student['email']='minjun@exmple.com'
student['hobbies']=['python','game']
student['age']=21
print("항목수",len(student))
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone','등록되지않음'))
print(f"{'email'in student} {'major'in student}")
print("="*38)
print(f"{'PRFIE':<8}")
print("="*38)
print(f"{'이름':<8}{student['name']:^8}")
print(f"{'나이':<8}{student['age']:^8}")
print(f"{'이메일':<8}{student['email']:^8}")
print(f"{'전화':<8}{student.get('phone','등록되지않음'):^8}")
print("-"*38)
print(f"{'취미':<8}{str(student['hobbies']):^8}")
print("="*38)
