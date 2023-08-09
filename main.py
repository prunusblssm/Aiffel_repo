# 나만의 n면체 주사위 클래스 이름은 FunnyDice로 합니다. (Dice는 주사위라는 뜻이에요)
# 주사위 면의 개수 n을 인스턴스 변수로 선언해 주사위 면의 개수 n을 입력할 수 있게 합니다.
# throw란 메서드로 주사위를 던져서 1 ~ n 중 하나의 값이 나오게 합니다.
# 주사위의 값을 특정한 값으로 세팅하기 : setval이란 기능을 통해 특정 값을 user가 선택할 수 있는 치팅 기능을 넣어도 재밌을 것 같네요.
# 현재 주사위 값 얻기 : 주사위를 던졌든, 주사위 값을 세팅했든 주사위의 값을 user한테 알려줘야 합니다.
# getval이란 기능을 추가해서 user가 현재 주사위의 값을 읽을 수 있게 해줍니다.

from random import randrange

#FunnyDice 클래스 정의
class FunnyDice:
    def __init__(self, n=6):
        self.n = int(n) #주사위 면의 개수 설정, n은 정수타입으로 입력
        self.numbers = list(range(1, n+1)) # 1부터 n까지의 숫자 리스트 생성
        print(self.numbers)
        self.index = randrange(0, self.n) #주사위 던진 후 나온 값의 인덱스 설정
        print(self.index) # print(self.numbers)
        self.val = self.numbers[self.index] #주사위 던진 후 나온 값 설정

    #주사위를 던지는 메서드
    def throw(self):
        self.index = randrange(0, self.n) #무작위 인덱스 선택을 한다.
        self.val = self.numbers[self.index] # 해당 인덱스의 값으로 주사위 눈의 값 설정

    #주사위 값 조회 메서드
    def getval(self):
        return self.val

    #주사위 값 설정 메서드
    def setval(self, val):
        if val <= self.n:
            self.val = val
        else:
            msg = f"주사위에 없는 숫자입니다. 주사위는 1~{self.n}까지 있습니다."
            raise ValueError(msg)


# 주사위 면의 개수를 입력받는 함수
def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요: "))
    return n

#메인 함수
def main():
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    #print("행운의 숫자는? {}".format(mydice.getval()))
    print(f"행운의 숫자는? {mydice.getval()}") ##하지만 이보다 더 간편하게 f-string을 사용하여 코드를 표현할 수 있습니다.
                                            # f-string은 문자열 안에서 변수나 표현식을 간편하게 삽입할 수 있는 방법을 제공합니다

#프로그램 시작점
if __name__=='__main__':
    main()
#if __name__ == "__main__": 블록을 사용하여 프로그램 시작점을 정의하여
# 주사위 프로그램을 직접 실행했을 때만 main() 함수가 호출되도록 구성
#https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720
#__name__ : interpreter가 실행 전에 만들어 둔 글로벌 변수
