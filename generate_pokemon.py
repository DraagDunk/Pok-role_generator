# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:25:35 2021

@author: Jesper
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:48:18 2021

@author: Jesper
"""

import random
import make_pokemon

#starters = ["Chespin", "Tepig", "Popplio", "Caterpie", "Wurmple", "Pidove", 
#            "Rattata", "Hoothoot", "Poliwag", "Sentret", "Wingull", "Pachirisu",
#            "Buneary", "Lillipup", "Tentacool", "Koffing", "Grimer", "Swinub",
#            "Skiddo", "Mareep", "Mudbray", "Skitty", "Ducklett", "Deerling",
#            "Woobat", "Tynamo", "Pumpkaboo", "Rockruff", "Sandygast", "Bidoof",
#            "Vulpix", "Bonsly", "Murkrow", "Pineco", "Munna", "Cottonee",
#            "Litwick", "Salandit", "Binacle", "Meowth (Galar)", "Milcery"
#            ]
##pname = random.choice(starters)
#psex = "random" #random.choice(["Male", "Female"])
#pname = "Caterpie"
#rank = "Starter"
#chosen_ability = True
#p = make_pokemon.pokemon(pname, psex, rank)

def print_pokemon(pname, p, chosen_ability=False):

    file_name = pname.replace(" ", "_")
    f = open("pokemon/" + file_name + ".txt", "w", encoding="utf-8")
    
    
    f.write("========================================" + p.species.upper() + "=============================================="
            " \n#" + str(p.number) + " " + p.species + " \t| \tSex: " + p.sex + " \t| \t"
            )
    
    if p.type2 == None:
        f.write(p.type1.upper())
    else:
        f.write(p.type1.upper() + "/" + p.type2.upper())
    
    f.write(" \nRank: " + p.rank + " \t| \tNature: " + p.nature + 
            " \nHeight: " + str(p.height) + "m \t| \tWeight: " + str(p.weight) + "kg \n"
            )
    
    if p.ability2 == None:
        f.write(p.ability1 + ": " + make_pokemon.describe_ability(p.ability1))
    else:
        if chosen_ability == True:
            ch_ab = random.choice((p.ability1, p.ability2))
            f.write(ch_ab + ": " + make_pokemon.describe_ability(ch_ab))
        else:
            f.write(p.ability1 + ": " + make_pokemon.describe_ability(p.ability1) + "\n" + 
                    p.ability2 + ": " + make_pokemon.describe_ability(p.ability2)
                    )
    
    f.write(" \n========================================ATTRIBUTES===========================================" +
            " \nCONFIDENCE: " + str(p.confidence) + " \t| \tHP: " + str(p.hp) + " \t\t| \tWILL: " + str(p.will) +
            " \nINITIATIVE: " + str(p.references.initiative) + " \t| \tDEFENSE: " + str(p.references.defense) + " \t| \tSP. DEFENSE: " + str(p.references.sdefense) + 
            " \nEVASION: " + str(p.references.evasion) + " \t| \tPHYS. CLASH: " + str(p.references.pclash) + " \t| \tSPEC. CLASH: " + str(p.references.sclash) + 
            " \nSTRENGTH: " + str(p.attributes.strength) + "/" + str(p.limits.strength) + 
            " | DEXTERITY: " + str(p.attributes.dexterity) + "/" + str(p.limits.dexterity) + 
            " | VITALITY: " + str(p.attributes.vitality) + "/" + str(p.limits.vitality) + 
            " | SPECIAL: " + str(p.attributes.special) + "/" + str(p.limits.special) + 
            " | INSIGHT: " + str(p.attributes.insight) + "/" + str(p.limits.insight) + 
            " \n========================================SOCIAL=ATTRIBUTES====================================" +
            " \nTOUGH: " + str(p.social_att.tough) + " \t| BEAUTY: " + str(p.social_att.beauty) + 
            " \t| COOL: " + str(p.social_att.cool) + " \t| CUTE: " + str(p.social_att.cute) + 
            " \t| CLEVER: " + str(p.social_att.clever) + 
            " \n========================================SKILLS===============================================" +
            " \nBRAWL: " + str(p.skills.brawl) + " \t| \tCHANNEL: " + str(p.skills.channel) + " \t| \tEVASION: " + str(p.skills.evasion) + " \t| \tCLASH: " + str(p.skills.clash) + 
            " \nALLURE: " + str(p.skills.allure) + " \t| \tETIQUETTE: " + str(p.skills.etiquette) + " \t| \tINTIMIDATE: " + str(p.skills.intimidate) + " \t| \tPERFORM: " + str(p.skills.perform) + 
            " \nALERT: " + str(p.skills.alert) + " \t| \tATHLETIC: " + str(p.skills.athletic) + " \t| \tNATURE: " + str(p.skills.nature) + " \t| \tSTEALTH: " + str(p.skills.stealth) + 
            " \n========================================MOVES================================================ \n"
            )
    
    for i in range(len(p.moves)):
        move = p.moves[i].split(";")
        acc_lst = move[3].replace(" ","").split("+")
        dam_lst = move[4].replace(" ","").replace("*","").split("+")
        f.write(move[0] + " \t| \t" + move[1] + " \t| \t" + move[2] + 
                " \n\tAccuracy: " + move[3] + " ("
                )
        if "/" in acc_lst[0]:
            acc_0_lst = acc_lst[0].split("/")
            acc1 = p.get_val(acc_0_lst[0]) + p.get_val(acc_lst[-1])
            acc2 = p.get_val(acc_0_lst[1]) + p.get_val(acc_lst[-1])
            f.write(str(acc1) + "/" + str(acc2))
            
        else:
            f.write(str(sum([p.get_val(acc_lst[i]) for i in range(len(acc_lst))]))
                    )
        
        f.write(")" + " \n\tDamage: " + move[4] + " "
                )
        
        if dam_lst[0] != "None" and dam_lst[0] != "Varies":
            f.write("(" + str(p.get_val(dam_lst[0]) + int(dam_lst[-1])) + ")"
            )
        else:
            pass
        
        f.write(
                " \n\tAdded effect: " + move[5] + " \n"
                )
    
    f.write("=============================================================================================")
    
    f.close()