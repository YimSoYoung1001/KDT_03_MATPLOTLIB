# ----------------------------------------------------------------------------------
# 자동차 클래스
# 클랙스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성)
# 클래스 기능 : 주행, 정지, 후진
# ----------------------------------------------------------------------------------
# 직접접근 : "."을 찍어서 바로 접근하는 것
# 간접접근 : 메서드를 통해서 접근하는 것
# decorator : 간접접근을 직접접근 방식으로 표현할 수 있게 해주는 것!

class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, 카 인스턴스 메서드
    def driving(self, where, who):
        print(f'{where}에 {self.number}차가 {who}와 함꼐 주행함')

    def stop(self, where):
        print(f'{self.number}차가 {where}에 정지함')

    def back(self):
        print(f'{self.number}차가 후진함')


# ----------------------------------------------------------------------------------
# 자율주행자동차 클래스 생성 - 상속 적용
# 클랙스 이름 : SelfCar
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성)
# 클래스 기능 : 주행, 정지, 후진, 셀프
# ----------------------------------------------------------------------------------
class SelfCar(Car):
    # 클래스 속성 => 없음
    # 이것도 그대로 상속이 되는가?

    # 객체 즉 인스턴스 생성
    def selfDrive(self, place):
        print(f'{self.number}차가 목적지인 {place}로 자율주행함')


myCar = SelfCar(10, 'black', '11가 1234', '마티즈')
myCar.selfDrive('우리집')
myCar.back()
print(myCar.maker)


# ----------------------------------------------------------------------------------
# 자율비행자동차 클래스 생성 - 상속 적용
# 클랙스 이름 : FlyCar
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성)
# 클래스 기능 : 주행, 정지, 후진, 셀프, 날기
# ----------------------------------------------------------------------------------
class FlyCar(SelfCar):
    def fly(self, place, speed):
        print(f'{self.number}차가 목적지인 {place}로 {speed}의 속도로 날아감')

caar = FlyCar(20, 'rainbow', '12가 3456', 'SUV')
caar.fly('자취방', '마하')
caar.driving('태평양', '또 다른 나')