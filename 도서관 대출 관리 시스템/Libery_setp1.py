#규칙만들기
from abc import ABC, abstractmethod
class Libraryitem(ABC):
    total_items=0
    def __init__(self,title,item_id):
        self.title=title
        self.item_id=item_id
        self.is_loaned=False
        self.borrower=None
        Library.total_items += 1
    @abstractmethod
    def is_loaned(self):
        pass
    @abstractmethod
    def info(self):
        pass
#실행 테스트
x=Libraryitem("테스트","T001")