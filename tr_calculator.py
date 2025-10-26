
class Islem:
    
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def hesapla(self):
        if self.operator not in "+-*/:":
            return "Lütfen doğru işlem seçiniz(+,-,*,/,:): "

        if self.operator == "+":
            return self.num1 + self.num2 
        elif self.operator == "-":
            return self.num1 - self.num2
        elif self.operator == "*":
            return self.num1 * self.num2
        elif self.operator in ["/", ":"]:
            return self.num1 / self.num2
      
        

while True:
    num1 = int(input("İlk sayınızı giriniz: "))
    operator = input("İşleminizi seçiniz: ")
    num2 = int(input("İkinci sayınızı giriniz: "))

    islem1 = Islem(num1, num2, operator)
    print("Sonuç:", islem1.hesapla())
