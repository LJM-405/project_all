from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error,r2_score
#데이터를 불러오고
X,y=load_diabetes(return_X_y=True)
#테스트를20퍼만 사용하겠다 선언
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#모델만들고 학습시키기
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
#결과값
print("평균오차=%6.2f"%mean_absolute_error(y_test,pred))
print("설명력=%7.4f"%r2_score(y_test,pred))
#추가해서 다시 검사
base=DummyRegressor(strategy="mean")
base.fit(X_train,y_train)
base_pred=base.predict(X_test)
#1번째와2번째 차이가 어느정도인데? 보는용
print("기준모델 평균오차=%.2f" % mean_absolute_error(y_test, base_pred))
print("기준모델 설명력 = %.4f" % r2_score(y_test, base_pred))
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import(accuracy_score,precision_score,recall_score,confusion_matrix)
y_train_c=(y_train > 140).astype(int)#140점넘으면 1(true라는것)
y_test_c=(y_test > 140).astype(int)
clf=LogisticRegression(max_iter=1000)
clf.fit(X_train,y_train_c)
pred=clf.predict(X_test)
print("정확도=%.4f"% accuracy_score(y_test_c,pred))
print("정밀도=%.4f"% precision_score(y_test_c,pred))
print("재현율=%.4f"% recall_score(y_test_c,pred))
print(confusion_matrix(y_test_c,pred))
base=DummyClassifier(strategy="most_frequent")
base.fit(X_train,y_train_c)
base_pred=base.predict(X_test)
print("기준모델 정확도=%.4f" % accuracy_score(y_test_c, base_pred))