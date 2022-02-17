from guizero import App, Slider, Text, Box
# tool to tell you what level monster u have 100% chance to combo in wonderland online

#forumla is |your party lvl devided by partysize = (this number) - 25 = (the level of monster u will 100% combo)
# the answer to that devided by the monsters level times your partysize = the % chance of you comboing
def yourlvl():
    
    c = c1.value + c2.value + c3.value + c4.value + p1.value + p2.value + p3.value + p4.value
    p = c / party_size.value
    g = p - 25
    answer.value = g
    
    t = g / monsterlevel.value
    r = t * party_size.value
    combo_answer.value = r
    

app = App("combo calulator for WLO/NWLO/WLORI/MWLO",height = 600, width = 550)

party_area = Box(app, align = "right", height = 600, width = 300)

monster_area = Box(app, align = "right", height = 600, width = 300)

##partysize
party_size_lable = Text(monster_area, "party size")
party_size = Slider(monster_area,start = 1 , end = 8, command = yourlvl)
monsterlevel_lable = Text(monster_area, "monsters level")
monsterlevel = Slider(monster_area, start = 1 , end = 199, command = yourlvl)
combo_lable = Text(monster_area, "your % at comboing the monster")
combo_answer = Text(monster_area, "0%")
blankspace3 = Text(monster_area,"")#YES ME KNOW THIS IS A BADWAY TO DO IT sush ya mush lol
thanks5 = Text(monster_area, "thanks Shawnco#8441")
thanks6 = Text(monster_area, "for pointing out im blind")
blankspace4 = Text(monster_area,"")#YES ME KNOW THIS IS A BADWAY TO DO IT sush ya mush lol
thanks = Text(monster_area, "thanks Real Cyber-cat#3197")
thanks1 = Text(monster_area, " for posting the formula")
thanks2 = Text(monster_area, "on choco discord")
blankspace2 = Text(monster_area, "")#YES ME KNOW THIS IS A BADWAY TO DO IT sush ya mush lol
thanks3 = Text(monster_area, "and thanks Vesemir#2137")
thanks4 = Text(monster_area, "for helping with UI layout ^_^")
blankspace = Text(monster_area, "")#YES ME KNOW THIS IS A BADWAY TO DO IT sush ya mush lol
note = Text(monster_area, "click/ hold click on the dark gray")
note1 = Text(monster_area, "dont try draging the slider")
blankblank = Text(monster_area, "")#YES ME KNOW THIS IS A BADWAY TO DO IT sush ya mush lol
note3 = Text(monster_area, "this tool dosnt account for your SPD")
notew = Text(monster_area, "IF U ARE RB ADD 99 TO LVL", color = (200,0,0))

#party level settings 
l1 = Text(party_area, "member 1")
c1 = Slider(party_area,start =1, end = 300, command = yourlvl)
l2 = Text(party_area, "member 2")
c2 = Slider(party_area, end = 300, command = yourlvl)
l3 = Text(party_area, "member 3")
c3 = Slider(party_area, end = 300, command = yourlvl)
l4 = Text(party_area, "member 4")
c4 = Slider(party_area, end = 300, command = yourlvl)
l5 = Text(party_area, "member 1 pet")
p1 = Slider(party_area, end = 300, command = yourlvl)
l6 = Text(party_area, "member 2 pet")
p2 = Slider(party_area, end = 300, command = yourlvl)
l7 = Text(party_area, "member 3 pet")
p3 = Slider(party_area, end = 300, command = yourlvl)
l8 = Text(party_area, "member 4 pet")
p4 = Slider(party_area, end = 300, command = yourlvl)
answerlable = Text(party_area, "u will 100% combo with monsters level")
answer = Text(party_area, "0")

app.display()
