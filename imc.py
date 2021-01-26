def imc_calc(sex : int =2, weight : int =60, size :float =1.70):
    value : int = 0
    if sex == 1:
        value = weight / (size * size)
    if sex == 2:
        value = (weight - 10) / (size * size)
    print("Your imc is " + str(value))

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