"""
* namespace : 개체를 구분할 수 있는 범위
* __dict__ : 네임스페이스를 확인할 수 있다. (dict형태로 반환)
* dir() : 네임스페이스의 key 값을 확인할 수 있다.
* __doc__ : class의 주석을 확인한다.
* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""

class Robot:
    """
    [Robot Class] # 어떤 클래스인지
    Author : 이예지 # 만든 사람
    Role : class의 역할
    """
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

siri = Robot("siri", 21039788127)

jarvis = Robot("jarvis", 21039788129)

bixby = Robot("bixby", 21039788130)

print(Robot.__dict__)
print(siri.__dict__) # instance 함수인 say_hi, cal_add는 siri의 namespace에 없는 것으로 나옴.
# 보통 함수를 정의하고 그 함수에 다른 함수를 다시 대입하는 경우는 없듯이 인스턴스 안에 인스턴스 함수를 포함하지는 않는 것.
# 메모리 효율을 위해서 파이썬이 인스턴스 메서드를 인스턴스의 네임스페이스에 정의하는 게 아니라 클래스의 네임스페이스에 정의.
print(jarvis.__dict__)

siri.cal_add(1, 2) # siri 인스턴스의 namespace에 cal_add가 없지만 사용가능한 이유는
# 파이썬은 인스턴스의 namespace에 없는 값은 인스턴스의 클래스의 namespace에서 찾아서 씀.
# 이 원리를 통해서 인스턴스를 통해서 클래스 변수, 클래스 메서드에 접근이 가능하다.
siri.how_many()

# 반대로 class.인스턴스메서드를 쓰면 self를 넣으라고 에러가 발생한다.
# TypeError: Robot.say_hi() missing 1 required positional argument: 'self'
#Robot.say_hi()
Robot.say_hi(siri) # 이렇게 인스턴스를 인자로 넘기면 해결은 가능한데 siri.say_hi()와 동일한 의미를 가진다.

print(dir(siri))

print(dir(Robot))

print(Robot.__doc__) # class에 대한 주석 확인

print(siri.__class__) # instance가 어떤 클래스로 만들어진 건지 확인