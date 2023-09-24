class BMI:
    def __init__(self, height, weight):
        self.height = height  # インスタンス変数
        self.weight = weight  # インスタンス変数

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print(tanaka_bmi.height, sasami_bmi.height)
#print(sasami_bmi.height, sasami_bmi.height)

print(tanaka_bmi.calculate_bmi())
print(sasami_bmi.calculate_bmi())