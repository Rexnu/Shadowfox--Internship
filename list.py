justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print("Justice league team =",justice_league)
print()

print("Number of members in the justice league =",len(justice_league))
print()

justice_league.extend(["Batgirl","Nightwing"])
print("After adding Batgirl and Nightwing =",justice_league)
print()

justice_league.insert(0,justice_league.pop(justice_league.index("Wonder Woman")))
print("Wonder Woman is now leader =",justice_league)
print()

justice_league.insert(justice_league.index("Flash")+1,justice_league.pop(justice_league.index("Green Lantern")))
print("After separating Aquaman and Flash =",justice_league)
print()
                      

justice_league.remove("Wonder Woman")
justice_league.remove("Superman")
justice_league.remove("Batman")
justice_league.remove("Green Lantern")
justice_league.remove("Flash")
justice_league.remove("Aquaman")
justice_league.remove("Batgirl")
justice_league.remove("Nightwing")
justice_league.extend(["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"])
print("New justice league team =",justice_league)
print()

justice_league.sort()
print("justice league in alphabetically =",justice_league)
print()
print("New leader =",justice_league[0])

