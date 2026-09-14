
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def append(self, data):
        new_node=Node(data)
#만약 공백일경우
        if self.head is None:
            self.head=new_node
            return
#만약 이미 칸있는경우
        current=self.head
        while current.link is not None:
            current=current.link
#맨마지막칸의 링크에 새로운칸 만들기
        current.link=new_node
#정리해서 출력하는 함수
    def print_list(self):
        current=self.head
        result=[]
        while current is not None:
            result.append(str(current.data))
            current=current.link
        print("L=("+",".join(result)+")")
#숫자를 중간에 넣어 출력하고싶을때
    def insert_after(self,taget_data,new_data):
        current=self.head
        while current is not None:
            if current.data==taget_data:
                break
            current=current.link
            if current is None:
                print(f"오류: {taget_data}노드를 찾을 수 없습니다")
                return
            new_node=Node(new_data)
            new_node.link=current.link
            current.link=new_node
#역순으로 만들기
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next_node=current.link#임시로잡기
            current.link=prev#현재칸을 돌려서 앞사람을 잡게하기
            prev=current#다음을위해 한칸전진
            current=next_node#내가 전진
        self.head=prev
if __name__=="__main__":
    L=SingleLinkedList()
    print("(1)공백리스트에 노드3개 삽입하기")
    L.append(1)
    L.append(3)
    L.append(7)
    L.print_list()
    print("(2)3 노드 뒤에 5노드 삽입히기")
    L.insert_after(3,5)
    L.print_list()
    print("(3)리스트 노드를 역순으로 바꾸기")
    L.reverse()
    L.print_list()