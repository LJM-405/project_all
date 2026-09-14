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