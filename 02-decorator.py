def copyright(func):
    # 함수를 인자로 받고 이 함수 내부에 다른 함수를 정의,
    # 이 내부함수에서 인자로 받은 함수를 실행
    # 겉에 있는 함수가 내부 함수를 반환하도록 함, 이를 데코레이터로 사용
    def new_func():
        print("@ copyrighit 2024")
        func()
    return new_func

@copyright
def smile():
    print("^^")
@copyright
def angry():
    print("ㅡㅡ")
@copyright
def love():
    print("♥")

smile()
angry()
love()