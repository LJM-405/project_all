import os, sklearn.datasets as ds#난이걸불러올껀데
print(os.path.join(os.path.dirname(ds.__file__),'data'))#그파일이 어디에있는지 확인
#표를 불러올껀데
from sklearn.datasets import load_diabetes
df=load_diabetes(as_frame=True).frame
print(df.head())#맨앞에서 불러올꺼야
print(df.tail())#맨뒤에서 불러올꺼야