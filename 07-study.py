# 반복되는 뭔가가 있고 이걸 하나의 집단 내에서 속성, 행위로 나눌 수 있겠구나
# -> 이럴 때 class를 정의한다.

class Cal:
    def __init__(self, a, b): # 생성자, construtor : 메모리에 올라오는 순간 즉시 실행됩니다.
        # self는 class를 instance로 만들었을 때 그 instance를 지칭
        self.a = a
        self.b = b
        

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

cal1 = Cal(1, 2) # self는 instance를 의미하니까 이러면 Cal의 self가 cal1을 가리키게 됨

print(cal1.a)
print(cal1.b)
print(cal1.add())

# instance는 각각이 독립적이다.
cal2 = Cal(3, 4)

print(cal2.a)
print(cal2.b)

# instance 변수를 외부에서 수정할 수도 있음

cal1.a = 7

print(cal1.a)
print(cal1.b)
print(cal1.add())