# =============================================================================================
# work 01.18. 임소영
# 코딩도장 클래스 : 34~36장
# =============================================================================================

# --------------------------------------------------------------
# 34장
# --------------------------------------------------------------

# 연습문제 34-5
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('배기')

x = Knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()


# 심사문제 34-6

class Annie:
    def __init__(self, *args):
        self.health = args[0]
        self.mana = args[1]
        self.AP = args[2]

    def kill(self):
        print(self.AP * 0.65 + 400)

word = [511.68, 334.0, 298]

Annie(*word)
Annie.kill()




# --------------------------------------------------------------
# 35장
# --------------------------------------------------------------
# 연습문제 35-5
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <=31

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')


# 심사문제 35-6
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        if hour <= 24 and minute <= 60 and second <= 60:
            return hour, minute, second

    @classmethod
    def from_string(cls):  # 문자열로 인스턴스를 만드는 메서드
        return cls.hour, cls.minute, cls.second


time_string = '23:35:59'

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)

else:
    print('잘못된 시간 형식입니다.')
