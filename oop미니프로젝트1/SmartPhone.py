from Address import Addr
class SmartPhone:
    def __init__(self):
        self.addr_list=[]
    def add_address(self,addr_instance):
        if len(self.addr_list)<10:
            self.addr_list.append(addr_instance)
        else:
            print("저장공간이 가득 찼습니다(최대 10개)")
    def show_all_addresses(self):
        if not self.addr_list:
            print("저장된 연락처가 없습니다")
            return
        print("\==전체목록==")
        for addr in self.addr_list:
            addr.show_info()
    def update_address(self,name, new_phone,new_email,new_address,new_group):
        for addr in self.addr_list:
            if addr.name==name:
                addr.phone=new_phone
                addr.email=new_email
                addr.address=new_address
                addr.group=new_group
                print(f"{name}연락처가 변경되었습니다")
                return
        print(f"{name}님을 찾을 수 없습니다")
    def delete_address(self,name):
        for addr in self.addr_list:
            if addr.name==name:
                self.addr_list.remove(addr)
                print("삭제가 완료되었습니다")
                return
        print(f"{name}을(를) 찾을수가 없습니다")
    def search_address(self,name):
        for addr in self.addr_list:
            if addr.name==name:
                print("검색결과 : ")
                addr.show_info()
                return
        print(f"{name}을(를)찾을 수 없습니다")
