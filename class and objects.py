class Avenger:
    def __init__(self,name,age,gender,super_power,weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return f"{self.name} - age:{self.age},gender:{self.gender},super_power:{self.super_power},weapon:{self.weapon}"

    def is_leader(self):
        return self.name == "captain america"  or self.name == "iron man"

    
avengers = [ Avenger("captain america",100,"male","super strength","shield"),
                 Avenger("iron man",48,"male","technology","armor"),
                 Avenger("black widow",35,"female","super human","batons"),
                 Avenger("hulk",40,"male","unlimited strength","no weapon"),
                 Avenger("thor",1500,"male","super energy","mjolnir"),
                 Avenger("hawkeye",35,"male","fighting skills","bow and arrows")]
for avenger in avengers :
               print(avenger.get_info())
               print("is leader:",avenger.is_leader())
               print()


             




             
