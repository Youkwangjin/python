from pack2.test34etc import Employee

# 상속은 기본 클래스를 재사용해주는 기법이다. 상속을 통해 추상화를 이용한 다형성 표현이 가능하다.

class Temporary(Employee):
    ilsu = 0
    ildang = 0

    def __init__(self, irum, nai, ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang

    def pay(self):
        return self.ilsu * self.ildang

    def data_print(self):
        self.irumnai_print()
        print('월급 : ' + str(self.pay()))


t = Temporary('홍길동', 25, 20, 150000)
t.data_print()


class Regular(Employee):
    salary = 0

    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary

    def pay(self):
        return self.salary

    def data_print(self):
        self.irumnai_print()
        print('급여 : ' + str(self.salary))


r = Regular('한국인', 27, 3500000)
r.data_print()


class Salesman(Regular):
    sales = 0
    commission = 0.25

    def __init__(self, irum, nai, salary, sales, commission):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def pay(self):
        return super().pay() + self.sales * self.commission

    def data_print(self):
        self.irumnai_print()
        print('수령액 : ' + str(self.pay()))


s = Salesman('손오공', 29, 120000, 5000000, 0.25)
s.data_print()


