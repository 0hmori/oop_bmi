class BMI:
    def __init__(self, height, weight):
        # self.height = height  # インスタンス変数
        # self.weight = weight  # インスタンス変数
        self.value = weight / (height**2)

    # def calculate_bmi(self):
    # return self.weight / (self.height**2)


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print("tanaka")
# print(tanaka_bmi.height, tanaka_bmi.weight)
print(tanaka_bmi.value)

print("ssami")
# print(sasami_bmi.height, sasami_bmi.weight)
print(sasami_bmi.value)
