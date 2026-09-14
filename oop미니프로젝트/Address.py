class Addr:
    def __init__(self,name,phone_number,email,home_address,group):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.home_address=home_address
        self.group=group
    def show_info(self):
        print(f"'이름'{self.name},'전화번호'{self.phone_number},'이메일'{self.email},'주소'{self.home_address},'그룹'{self.group}")