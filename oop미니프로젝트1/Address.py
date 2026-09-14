class Addr:
    def __init__(self,name,phone_number,email,home_address,group,birthday):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.home_address=home_address
        self.group=group
        self.birthday=birthday
    def show_info(self):
        print(f"'이름'{self.name},'전화번호'{self.phone_number},'이메일'{self.email},'주소'{self.home_address},'그룹'{self.group}'생일'{self.birthday}")
class CompanyAddr(Addr):
    def __init__(self, name, phone_number, email, home_address, group, birthday,compay_name,dept_name,job_title):
        super().__init__(name, phone_number, email, home_address, group, birthday)
        self.company_name=compay_name
        self.dept_name=dept_name
        self.job_title=job_title
    def show_info(self):
        super().show_info()
        print(f"'회사명:'{self.company_name}'부서이름:'{self.dept_name}'직급:'{self.job_title}")
class CustomerAddr(Addr):
    def __init__(self, name, phone_number, email, home_address, group, birthday,customer_name,custmer_item,custmer_title):
        super().__init__(name, phone_number, email, home_address, group, birthday)
        self.customer_name=customer_name
        self.customer_item=custmer_item
        self.customer_title=custmer_title
    def show_info(self):
        super().show_info()
        print(f"'거래처이름'{self.customer_name}'품목이름'{self.customer_item}'직급'{self.customer_title}")