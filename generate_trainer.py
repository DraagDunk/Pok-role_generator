# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:48:18 2021

@author: Jesper
"""

import random
import make_trainer
import make_pokemon
#from tqdm import tqdm
import tkinter as tk


def import_all(path):
    r = open(path, "r")
    file = r.read().split("\n")
    pkmn_lst = []
    for j in range(len(file))[1:]:
        pkmn_str = file[j].split(";")
        pkmn_lst.append(pkmn_str[0])
    return pkmn_lst


def print_trainer(person,pokes,chosen_ability=False):
    
    name = person.name
    
    file_name = name.replace(" ", "_")
    f = open("trainers/" + file_name + ".txt", "w", encoding="utf-8")
    
    f.write("Name: " + person.name + " \t| \tAge: " + str(person.age) + " \t| \tSex: " + person.sex + 
            " \nRank: " + person.rank + " \t| \tNature: " + person.nature + 
            " \n========================================ATTRIBUTES===========================================" + 
            " \nCONFIDENCE: " + str(person.confidence) + " \t| \tHP: " + str(person.hp) + " \t| \tWILL: " + str(person.will) + 
            " \nSTRENGTH: " + str(person.attributes.strength) + " \t| \tDEXTERITY: " + str(person.attributes.dexterity) + 
            " \t| \tVITALITY: " + str(person.attributes.vitality) + " \t| \tINSIGHT: " + str(person.attributes.insight) + 
            " \n========================================SOCIAL=ATTRIBUTES====================================" +
            " \nTOUGH: " + str(person.social_att.tough) + " \t| BEAUTY: " + str(person.social_att.beauty) + 
            " \t| COOL: " + str(person.social_att.cool) + " \t| CUTE: " + str(person.social_att.cute) + 
            " \t| CLEVER: " + str(person.social_att.clever) + 
            " \n========================================SKILLS===============================================" +
            " \nBRAWL: " + str(person.skills.brawl) + " \t| \tTHROW: " + str(person.skills.throw) + " \t| \tEVASION: " + str(person.skills.evasion) + " \t| \tWEAPONS: " + str(person.skills.weapons) + 
            " \nALLURE: " + str(person.skills.allure) + " \t| \tETIQUETTE: " + str(person.skills.etiquette) + " \t| \tINTIMIDATE: " + str(person.skills.intimidate) + " \t| \tPERFORM: " + str(person.skills.perform) + 
            " \nALERT: " + str(person.skills.alert) + " \t| \tATHLETIC: " + str(person.skills.athletic) + " \t| \tNATURE: " + str(person.skills.nature) + " \t| \tSTEALTH: " + str(person.skills.stealth) +
            " \nCRAFTS: " + str(person.skills.crafts) + " \t| \tLORE: " + str(person.skills.lore) + " \t| \tMEDICINE: " + str(person.skills.medicine) + " \t| \tSCIENCE: " + str(person.skills.science) +
            " \n=============================================================================================" 
            )
    if len(pokes) > 0:
        f.write(
            " \n========================================POKÉMON============================================== \n"
            )
    
    for i in range(len(pokes)):
        p = pokes[i]
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
            
            if dam_lst[0] != "None" and dam_lst[0] != "Varies" and dam_lst[0] != "SetDamage" and dam_lst[0] != "Sameascopiedmove":
                f.write("(" + str(p.get_val(dam_lst[0]) + int(dam_lst[-1])) + ")"
                )
            else:
                pass
            
            f.write(
                    " \n\tAdded effect: " + move[5] + " \n"
                    )
    
        f.write("============================================================================================= \n")
    
    f.close()
    
    

def gen_trainer(age=None, sex=None, name=None, rank=None, poke_num=None):

    if age == None:
        age = random.randint(8,90)
    elif age == "Teen":
        age = random.randint(13,19)
    if sex == None:
        sex = random.choice(["Male", "Female"])
    if name == None:
        name = make_trainer.get_name(sex)
    if rank == None:
        rank = random.choice(["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"])
        
    person = make_trainer.trainer(name, age, sex, rank)
    chosen_ability = False
    
    if poke_num == None:
        poke_num = random.randint(1,6)
        
    starters = ["Caterpie", "Weedle", "Pidgey", "Rattata", "Spearow",
                "Nidoran F", "Nidoran M",
                "Vulpix", "Vulpix (Alola)", "Jigglypuff", "Venonat", "Diglett",
                "Diglett (Alola)", "Meowth (Galar)", "Growlithe", "Poliwag",
                "Machop", "Tentacool", "Ponyta", "Magnemite", "Seel", "Grimer",
                "Shellder", "Gastly", "Krabby", "Voltorb", "Koffing", "Staryu",
                "Omanyte", "Cyndaquil", "Hoothoot", "Ledyba", "Mareep", 
                "Marill", "Sunkern", "Pineco", "Snubbull", "Swinub", "Houndour",
                "Torchic", "Wurmple", "Seedot", "Taillow", "Wingull", "Shroomish",
                "Skitty", "Swablu", "Barboach", "Corphish", "Lileep", "Shuppet",
                "Duskull", "Spheal", "Starly", "Bidoof", "Combee", "Buizel",
                "Cherubi", "Drifloon", "Buneary", "Glameow", "Bronzor",
                "Bonsly", "Tepig", "Oshawott", "Lillipup", "Pidove", "Woobat",
                "Drilbur", "Timburr", "Tympole", "Petilil", "Dwebble",
                "Scraggy", "Trubbish", "Ducklett", "Vanillite", "Deerling",
                "Foongus", "Frillish", "Joltik", "Tynamo", "Litwick",
                "Chespin", "Bunnelby", "Fletchling", "Flabebe", "Espurr",
                "Honedge", "Inkay", "Binacle", "Skrelp", "Goomy",
                "Phantump", "Rowlet", "Popplio", "Cutiefly", "Rockruff",
                "Mudbray", "Dewpider", "Morelull", "Salandit", "Wimpod",
                "Scorbunny", "Swovet", "Rookidee", "Nickit", "Yamper",
                "Applin", "Sizzlipede", "Clobbopus", "Sinistea", "Hatenna",
                "Impidimp", "Milcery", "Snom"
                ]
#    stronger = ["Pidgeot", 
#            
#                ]
#    pkmn_all = import_all("pokemon.txt")
#    pname = random.choice(starters)
#    pname = "Dragonite"
#    psex = random.choice(["Male", "Female"])
#    p1 = make_pokemon.pokemon(pname, psex, rank)
##    
#    pokes = [p1]
#    
#    pokes = [make_pokemon.pokemon(k, sex, rank) for k in pkmn_all]
    
    pokes = []
    
    for i in range(poke_num):
        pokes.append(make_pokemon.pokemon(random.choice(starters),"random",rank))
        
    print_trainer(person,pokes,chosen_ability=chosen_ability)
        
    
