import datetime as DT

today = DT.date.today()
#_time = DT.time.tzname()
print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDate : {today}")

class C11:
    def __init__(self, age, nick_name, girlfriend, favorite_lecturer, tribe, favorite_food, favorite_drink, skills):
        self.age = age
        self.nick_name = nick_name
        self.girlfriend = girlfriend
        self.favorite_lecturer = favorite_lecturer
        self.tribe = tribe
        self.favorite_food = favorite_food
        self.favorite_drink = favorite_drink
        self.skills = skills

    def Pprint(self):
        x = print("age              :\t", self.age, "\nNick_name        :\t", self.nick_name, "\nGirlfriend       :\t", self.girlfriend,
                  "\nFavorite_lecturer:\t", self.favorite_lecturer, "\nTribe            :\t", self.tribe, "\nFavorite food    :\t",
                  self.favorite_food, "\nFavorite drink   :\t", self.favorite_drink, "\nskills           :\t", self.skills, "\n\n")
        return x
                  

Josiah_Chaombamzati = C11(25,"Jacho or Data Bus", "hendrina kadzanja", "chimwemwe", "mlomwe uyu", "rice and any nyama", "madzi a pa reception",
            "wasting Wi-Fi data bundle")
Lumbani_Phiri = C11(15, "Twitter", "Type C", "Kalulu", "Mtumbuka wa kwa Chinsapo", "Jiggs", "Jada", "DeeJaying")
Brandon_Gumeni = C11(24, "Brandizzy or Baby Lung", "go and ask twitter", "unfortunately none, becouse we dont have any lecturer with nyash", "blantyre tribe", "mole's product", "Scout Gin", "Coughing good WEED")
Lamecki_Mvula = C11(18, "Goat", "Soul mate", "unfortunately Mr Said", "Police tribe", "Chips cha ma Cont", "Solu", "Euro truck Driving")
Simeon_Mulima = C11(22, "philoel or Asian_Gee", "analandidwa ndi Josia", "Kanfosi", "Chewa", "ndinamapo apa", "mojo", "Beatmaking")
Frank_Nkunika = C11(21, "Chikomeni", "undisclosed", "kayaa!, even ma lecturer ena samuziwa lol", "BLack caucasian", "Nsima ya ku cafe", "Nyasa Gin", "Speaking puzzling English than Twitter")
Precious_Kaphuka = C11(23, "Precipee", "undisclosed", "Indian guy on YouTube", "Ngoni", "Rice with Nyemba", "Jaja", "Programming")

ICT_Cohort_11_member = [Josiah_Chaombamzati, Lumbani_Phiri, Brandon_Gumeni, Lamecki_Mvula, Simeon_Mulima, Frank_Nkunika, Precious_Kaphuka]
_ICT_Cohort_11_member = []
for _member in ICT_Cohort_11_member:
    if _member == Josiah_Chaombamzati:
        _ICT_Cohort_11_member.append("Josiah   Chaombamzati")
    elif _member == Lumbani_Phiri:
        _ICT_Cohort_11_member.append("Lumbani  Phiri")
    elif _member == Brandon_Gumeni:
        _ICT_Cohort_11_member.append("Brandon  Gumeni")
    elif _member == Lamecki_Mvula:
        _ICT_Cohort_11_member.append("Lamecki  Mvula")
    elif _member == Simeon_Mulima:
        _ICT_Cohort_11_member.append("Simeon   Mulima")
    elif _member == Frank_Nkunika:
        _ICT_Cohort_11_member.append("Frank    Nkunika")
    else:
        _ICT_Cohort_11_member.append("Precious Kaphuka")

PG_name = print("\t\t\t\t\t\t\t\t\tDONT'T - CARE - SNITCH\n\n")
Guest_name = input("\t\t\t\t\t\t\t\t\tplease enter your name  :  ")
Guest_sex = str(input("\n\n\t\t\t\t\t\t\t\t\tmale  /   female        :  "))
prefix = ""

if Guest_sex.lower() == "male":
    prefix = "Mr"
elif Guest_sex.lower() == "female":
    prefix = "Miss"
else:
    prefix = ""

print(f"\n\t\t\t\t\t\t\t\t.........hello {prefix} {Guest_name}...........\n\t\t\t\t\t\tWelcome to precipee's program called The C11 Snitch.v1.1 ")
print(
    """\n\"\"\"\"\"\"\"\"\"\"\n
    The Snitch.v1.1 will show you the information of any ICT Cohort_11 member of your desire.\n
    if you have any additional information, please inform our developer.
    \n\"\"\"\"\"\"\"\"\"\""\n\t\t\t\t\t\t\t\t\t.......now lets begin.......\n
    """
)
guestsChoice = list(input(f"Would you like to continue {prefix} {Guest_name}?       Enter y for YES / n for NO : "))
flag = "y"
print("\n")

for choice in guestsChoice:
    if choice != flag:
        print(f"\n.....................Thanks for visit {prefix} {Guest_name}.....................\n\n\n\n")
        quit()

flag2 = True
while flag2 == True:
    print("    ICT Cohort 11 Boys")
    print("    --- ------ -- ----")
    for num, name in enumerate(_ICT_Cohort_11_member):
        num += 1
        _name = str(name)
        print(f"{num} : {_name}\n")

    chosen_member = int(input("!PLEASE! Enter  your option number  : "))
    print("\n")

    if chosen_member == 1:
        C11.Pprint(Josiah_Chaombamzati)
    elif chosen_member == 2:
        C11.Pprint(Lumbani_Phiri)
    elif chosen_member == 3:
        C11.Pprint(Brandon_Gumeni)
    elif chosen_member == 4:
        C11.Pprint(Lamecki_Mvula)
    elif chosen_member == 5:
        C11.Pprint(Simeon_Mulima)
    elif chosen_member == 6:
        C11.Pprint(Frank_Nkunika)
    elif chosen_member == 7:
        C11.Pprint(Precious_Kaphuka)
    else:
        print("invalid number")

    #print("\n")
    last_choice = input("would you like to choose another member  ( Enter  y for Yes / n for NO )  :  ")
    if last_choice.lower() == "y":
        continue
    else:
        print(f"\n.....................Thanks for visit {prefix} {Guest_name}.....................\n\n\n\n")
        flag2 = False
        quit()
