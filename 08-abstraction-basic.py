"""
* 추상화 : abstraciton
* 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
(=사용할 때는 안에서 어떤 로직으로 어떻게 동작하는지 복잡한 부분은 모름)
* 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
"""

class Robot:
    population = 0 # 클래스 변수 (인스턴스들이 공유하는 변수)
    # 생성자 함수
    def __init__(self, name, code):
        self.name = name # 인스턴스 변수
        self.code = code # 인스턴스 변수
        Robot.population += 1
        
    def say_hi(self): # 인스턴스 메서드
        print(f"Greetings, my masters call me {self.name}")
        
    def cal_add(self, a, b): # 인스턴스 메서드
        return a + b
    
    def die(self): # 인스턴스 메서드
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")
        
    @classmethod # 클래스 메서드
    def how_many(cls): # self는 인스턴스를 의미하지만 cls는 클래스를 의미함
        print(f"We have {cls.population} robots.")
        
print(Robot.population) # 0

siri = Robot("siri", 21039788127)

print(Robot.population) # 1

jarvis = Robot("jarvis", 21039788129)

print(Robot.population) # 2

bixby = Robot("bixby", 21039788130)

print(Robot.population) # 3

siri.say_hi()
siri.cal_add(1, 2)

Robot.how_many() # 이렇게 호출 시 이 classmethod의 cls인자가 Robot을 가리킴
