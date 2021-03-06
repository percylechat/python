class Male:
    def __init__(self, weight : int, size : float):
        self.weight = weight
        self.size = size
    def calc(self) -> float:
        result : float = self.weight / (self.size * self.size)
        return result

class Female:
    def __init__(self, weight : int, size : float):
        self.weight = weight - 10
        self.size = size
    def calc(self) -> float:
        result : float = self.weight / (self.size * self.size)
        return result

def imc_calc(sex : int =2, weight : int =60, size :float =1.70):
    #value : int = 0
    if sex == 1:
        #value = weight / (size * size)
        user = Male(weight, size)
        print("Your imc is " + str(user.calc()))
    if sex == 2:
        #value = (weight - 10) / (size * size)
        user = Female(weight, size)
        print("Your imc is " + str(user.calc()))
    #print("Your imc is " + str(value))

def call():
    sex : int = int(input("Are you :\n1 Male\n 2 Female\n"))
    ##while sex != 1 and sex != 2:
    ##    print("Please enter a number")
    ##    sex = input("Are you :\n1 Male\n 2 Female")
    weight : int = int(input("What is your weight in kilograms?"))
    size : int = float(input("What is your size in meter and centimeters (ex: 1.70)?"))
    imc_calc(sex, weight, size)

if __name__ == "__main__":
    call()