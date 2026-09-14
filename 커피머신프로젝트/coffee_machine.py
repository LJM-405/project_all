MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk": 150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"죄송합니다.{item}이 부족합니다")
            return False
    return True
#돈계산
def process_coins():
    print("동전을 넣어주세요")
    quarters=int(input("쿼터(.25센트)몇개?"))*0.25
    dimes=int(input("다임(.1센트)몇개?"))*0.10
    nikels=int(input("니켈(.05센트)몇개?"))*0.05
    pennies=int(input("페니(.01센트)몇개?"))*0.01
    total=quarters+dimes+nikels+pennies
    return total
#결제가 맞는지
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        if change>0:
            print(f"잔돈 {change}를 돌려드리겠습니다.")
        profit +=drink_cost
        return True
    else:
        print("죄송합니다 돈이 부족합니다")
        return False
#돈이 되면 계산후 제품내보내기
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"주문하신{drink_name}입니다!맛있게드세요!")
is_on=True
while is_on:
    choice=(input("어떤음료를 마시겠습니까?(espresso,latte,capuccino)"))
    if choice=="off":
        is_on=False
        print("커피머신을 종료합니다")
    elif choice=="report":
        print(f"물:{resources['water']}ml, 우유:{resources['milk']}ml,커피:{resources['coffee']}g,돈:${profit}")
    elif choice in MENU:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("잘못된 입력입니다 메뉴판에 있는메뉴를 선택해주세요")
