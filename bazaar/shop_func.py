def visit_shop(habitant):
    habitant.is_customer = True
    print("Someone came into your shop\n")
    boucle = True
    while boucle == True:
        rep = int(input("1.Ask about their day\n2.Make small talk\n3.Get status\n4.End conversation\n"))
        if rep == 1:
            pass
        elif rep == 2:
            pass
        elif rep == 3:
            print("This is " +str(habitant.first_name) + " " + str(habitant.last_name) + ".")
            if habitant.sex == 1:
                print("She " + habitant.get_age_categ() + ".")
                print("She looks " + habitant.get_status() + ".")
            else:
                print("He " + habitant.get_age_categ() + ".")
                print("He looks " + habitant.get_status() + ".")
        else:
            boucle = False