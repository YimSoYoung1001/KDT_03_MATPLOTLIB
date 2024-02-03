# --------------------------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Pint2D
# 클래스 속성 : x, y, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# --------------------------------------------------------------------------------------
class Point2D:
    # 클래스 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, color, shape, size):
        print('Point2D거임')
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    # 객체 즉 인스턴스 메서드
    def draw(self):
        print(f'좌표 ({self.x}, {self.y})에 {self.shape}그리기')

    def printInfo(self):
        print('Point2D거임')
        print(f'위치: {self.x}, {self.y}')
        print(f'색상: {self.color}')
        print(f'형태: {self.shape}')



# --------------------------------------------------------------------------------------
# 3차원 점 클래스
# 클래스 이름 : Pint3D
# 클래스 속성 : x, y, z, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# --------------------------------------------------------------------------------------

class Point3D(Point2D):            #여기서 point2d는 부모클래스,super클래스 / point3d는 자식클래스, sub클래스
    # 클래스 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, z, color, shape, size):
        # 부모 객체 생성
        super().__init__(x,y, color, shape, size)    #상속을 받는다해도 자동으로 넘어오지 않는다. 부모도 만들어 놓아야 한다
        self.z = z
        print('Point3D')

    #  상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩
    # 상속 관계에서만 가능! 일부만 수정해서 쓰겠다악! 이제는 자식것이 존재하게이 부모것을 쓰지 않는다악!
    def printInfo(self):
        print('Point3D거임')
        print(f'위치: {self.x}, {self.y}, {self.z}')
        print(f'색상: {self.color}')
        print(f'형태: {self.shape}')

p2 = Point2D(10, 10, 'red', 'circle', (10,10))
p3 = Point3D(5, 5, 5, 'yellow', 'rectangle', (3,3,3))

print(p3.x, p3.y, p3.color, p3.shape, p3.size)

p3.printInfo()      #point2d를 상속받았으니까 소환 ㄱㄴ
