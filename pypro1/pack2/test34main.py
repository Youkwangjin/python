from pack2.test34etc import Employee

class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        self.result = self.ilsu * self.ildang

    def data_print(self):
        self.pay()
        self.irumnai_print()
        print (", 월급 : {}".format(self.result))

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self, sales,commission):
        self.salary += (sales * commission)
        
    def data_print(self):
        self.irumnai_print()
        print (", 급여 : {}".format(self.salary))

class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        super().pay(sales,commission)


t = Temporary('홍길동', 25, 20, 15000)
t.data_print()
r = Regular('한국인', 27, 3500000)
r.data_print()
s = Salesman('손오공', 29, 1200000, 5000000, 0.25)
s.data_print()