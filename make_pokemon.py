# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:27:38 2021

@author: Jesper
"""

import random
import sys

class skills():
    def __init__(self):
        self.brawl       = 0
        self.channel     = 0
        self.clash       = 0
        self.evasion     = 0
        self.alert       = 0
        self.athletic    = 0
        self.nature      = 0
        self.stealth     = 0
        self.allure      = 0
        self.etiquette   = 0
        self.intimidate  = 0
        self.perform     = 0
    
class limits():
    def __init__(self):
        self.strength   = 0
        self.dexterity  = 0
        self.vitality   = 0
        self.special    = 0
        self.insight    = 0
    
class attributes():
    def __init__(self):
        self.strength    = 1
        self.dexterity   = 1
        self.vitality    = 1
        self.special     = 1
        self.insight     = 1
    
class social_att():
    def __init__(self):
        self.tough       = 1
        self.cool        = 1
        self.beauty      = 1
        self.cute        = 1
        self.clever      = 1
    
class references():
    def __init__(self, strength, dexterity, vitality, special, insight, clash, evasion, alert, extra_pass):
        self.initiative     = dexterity + alert + extra_pass
        self.evasion        = dexterity + evasion + extra_pass
        self.pclash         = strength + clash + extra_pass
        self.sclash         = special + clash + extra_pass
        self.defense        = vitality + extra_pass
        self.sdefense       = insight + extra_pass
        
def choose_random_skills(skills, points, limit):
    vari = list(vars(skills).keys())
    values = list(vars(skills).values())
    
    for i in range(points-sum(values)):
        done = False
        while done == False:
            skill = random.choice(vari)
            skill_num = getattr(skills, skill)
            if skill_num < limit:
                setattr(skills, skill, skill_num + 1)
                done = True
                
def get_nature(nature=None):
    f = open('natures.txt', 'r')
    nat_str = f.read().split('\n')[1:]
    nats, confs = ([], [])
    for i in range(len(nat_str)):
        nset = nat_str[i].split()
        nats.append(nset[0])
        confs.append(nset[1])
        if nature != None:
            if nature == nset[0]:
                n_index = i
    if nature != None:
        index = n_index
    else:
        index = random.randint(0,len(nats)-1)
    nature = nats[index]
    confidence = confs[index]
    return nature, confidence
                
def choose_random_attr(attr, points, limits):
    vari = list(vars(attr).keys())
    values = list(vars(attr).values())
    old_points = (sum(values))
    
    if points > old_points:
        for i in range(points-old_points):
            done = False
            while done == False:
                
                avail_att = []
                for j in vari:
                    if type(limits) != int and getattr(attr,j) < getattr(limits,j):
                        avail_att.append(j)
                    elif type(limits) == int and getattr(attr,j) < limits:
                        avail_att.append(j)        
                if len(avail_att) < 1:
                    done = True
                    print("Ran out of space for point distribution!")
                    break
                
                att = random.choice(avail_att)
                att_num = getattr(attr, att)
                if type(limits) == int:
                    if att_num < limits:
                        setattr(attr, att, att_num + 1)
                        done = True
                else:
                    if att_num < getattr(limits,att):
                        setattr(attr, att, att_num + 1)
                        done = True
    else:
        for i in range(old_points-points):
            done = False
            while done == False:
                att = random.choice(vari)
                att_num = getattr(attr, att)
                if att_num > 1:
                    setattr(attr, att, att_num - 1)
                    done = True
              
def where(lst, string, begins=False):
    index = []
    for i in range(len(lst)):
        if begins == False:
            if string.lower() in lst[i].lower():
                index.append(i)
        elif begins == True:
            if lst[i].lower().startswith(string.lower()):
                index.append(i)
    if index == []:
        print(string + " was not found.")
        sys.exit()
#        return None
    return index[0]
                
def find_pokemon_string(species):
    f = open('pokemon.txt', 'r', encoding='utf-8')
    pkmn_lst = f.read().split('\n')[1:]
    indices = []
    for i in range(len(pkmn_lst)):
        lst_str = pkmn_lst[i].split(";")
        if lst_str[0] == species:
            indices.append(i)
    index = indices[0]
    pkmn_str = pkmn_lst[index]
    return pkmn_str

def describe_move(move):
    f = open('moves.txt', 'r')
    move_lst = f.read().split("\n")[1:]
    index = where(move_lst, move, begins=True)
    return move_lst[index]

def describe_ability(ability):
    f = open('abilities.txt', 'r')
    ability_lst = f.read().split("\n")[1:]
    index = where(ability_lst, ability, begins=True)
    lst_item = ability_lst[index].split(";")
    return lst_item[1]

class pokemon():

    def stat_bases(self):
        
        self.rank_num = where(["Starter", "Beginner", "Amateur", "Ace", "Professional", "Master", "Champion"], self.rank)
        self.extra_pass = 0
            
        if self.rank == "Starter":
            abase = 0
            sbase = 0
            kbase = 5
            klim = 1
        elif self.rank == "Beginner":
            abase = 2
            sbase = 2
            kbase = 9
            klim = 2
        elif self.rank == "Amateur":
            abase = 4
            sbase = 4
            kbase = 12
            klim = 3
        elif self.rank == "Ace":
            abase = 6
            sbase = 6
            kbase = 14
            klim = 4
        elif self.rank == "Professional":
            abase = 8
            sbase = 8
            kbase = 15
            klim = 5
        elif self.rank == "Master":
            abase = 8
            sbase = 14
            kbase = 15
            klim = 5
            self.extra_pass = 2
        elif self.rank == "Champion":
            abase = 14
            sbase = 14
            kbase = 16
            klim = 5
        self.abase = abase
        self.sbase = sbase
        self.kbase = kbase
        self.klim = klim

    
    def get_move_lst(self):
        moves_lst = self.pos_moves.split(",")
        pos_moves = []
        rank_str = "sbmcpxy"
        this_rank_str = rank_str[:self.rank_num+1]
        
        for i in range(len(moves_lst)):
            if moves_lst[i][0] in this_rank_str:
                pos_moves.append(moves_lst[i].split(":")[-1])
        return pos_moves
        
        
    def choose_moves(self):
        
        pos_moves = self.get_move_lst()
        
        rem_moves = self.attributes.insight + 2 - len(self.moves)
                
        if rem_moves > len(pos_moves):
            self.moves = pos_moves
        else:
            self.moves = random.sample(pos_moves,rem_moves)
                    
    def increase_limits(self, inc):
        lim_keys = list(vars(self.limits).keys())
        for i in range(len(lim_keys)):
            key_att = getattr(self.limits, lim_keys[i])
            if key_att + inc > 10:
                setattr(self.limits, lim_keys[i], 10)
            else:
                setattr(self.limits, lim_keys[i], key_att + inc)
        
    
    def update(self):
        
        self.rank_num = where(["Starter", "Beginner", "Amateur", "Ace", "Professional", "Master", "Champion"], self.rank)
        self.extra_pass = 0
        
        if self.rank_num >= 0:
            abase = 0
            sbase = 0
            kbase = 5
            klim = 1
            choose_random_skills(self.skills, 5, klim)
        if self.rank_num >= 1:
            abase += 2
            sbase += 2
            kbase += 4
            klim = 2
            choose_random_skills(self.skills, 9, klim)
        if self.rank_num >= 2:
            abase += 2
            sbase += 2
            kbase += 3
            klim = 3
            choose_random_skills(self.skills, 12, klim)
        if self.rank_num >= 3:
            abase += 2
            sbase += 2
            kbase += 2
            klim = 4
            choose_random_skills(self.skills, 14, klim)
        if self.rank_num >= 4:
            abase += 2
            sbase += 2
            kbase += 1
            klim = 5
            choose_random_skills(self.skills, 15, klim)
        if self.rank_num >= 5:
            self.extra_pass = 2
            sbase = 14
            choose_random_attr(self.social_att, 5+14, 5)
        if self.rank_num >= 6:
            if self.champ == False:
                self.increase_limits(2)
                self.champ = True
            abase = 14
            kbase += 1
            choose_random_skills(self.skills, 16, 5)
            
        choose_random_attr(self.attributes, self.base_total + abase, self.limits)
        choose_random_attr(self.social_att, 5 + sbase, 5)
        
        self.abase = abase
        self.sbase = sbase
        self.kbase = kbase
        self.klim = klim
            
            
        self.references = references(self.attributes.strength, 
                                     self.attributes.dexterity, 
                                     self.attributes.vitality,
                                     self.attributes.special,
                                     self.attributes.insight,
                                     self.skills.clash,
                                     self.skills.evasion,
                                     self.skills.alert,
                                     self.extra_pass
                                     )
        self.hp = self.base_hp + self.attributes.vitality + self.extra_pass
        self.will = self.attributes.insight + 2 + self.extra_pass
        if len(self.moves) == 0:
            self.choose_moves()
        for i in range(len(self.moves)):
            self.moves[i] = describe_move(self.moves[i])
        
    def get_info(self):
        pkmn_str = find_pokemon_string(self.species)
        pkmn_lst = pkmn_str.split(";")
        self.species = pkmn_lst[0]
        self.number = int(pkmn_lst[1])
        self.type1 = pkmn_lst[2]
        if pkmn_lst[3].lower() == "none":
            self.type2 = None
        else:
            self.type2 = pkmn_lst[3]
        self.base_hp = int(pkmn_lst[4])
        self.ability1 = pkmn_lst[5]
        if pkmn_lst[6].lower() == "none":
            self.ability2 = None
        else:
            self.ability2 = pkmn_lst[6]
        self.attributes.strength = int(pkmn_lst[7])
        self.attributes.dexterity = int(pkmn_lst[8])
        self.attributes.vitality = int(pkmn_lst[9])
        self.attributes.special = int(pkmn_lst[10])
        self.attributes.insight = int(pkmn_lst[11])
        self.base_att.strength = int(pkmn_lst[7])
        self.base_att.dexterity = int(pkmn_lst[8])
        self.base_att.vitality = int(pkmn_lst[9])
        self.base_att.special = int(pkmn_lst[10])
        self.base_att.insight = int(pkmn_lst[11])
        self.base_total = int(pkmn_lst[7]) + int(pkmn_lst[8]) + int(pkmn_lst[9]) + int(pkmn_lst[10]) + int(pkmn_lst[11])
        self.limits.strength = int(pkmn_lst[12])
        self.limits.dexterity = int(pkmn_lst[13])
        self.limits.vitality = int(pkmn_lst[14])
        self.limits.special = int(pkmn_lst[15])
        self.limits.insight = int(pkmn_lst[16])
        self.height = float(pkmn_lst[17])
        self.weight = float(pkmn_lst[18])
        self.pos_moves = pkmn_lst[19]
        self.sex_dist = pkmn_lst[20]
        
    def get_val(self, name):
        if type(name) == int or type(name) == float:
            return int(name)
        att_vari = list(vars(self.attributes).keys())
        soc_vari = list(vars(self.social_att).keys())
        ski_vari = list(vars(self.skills).keys())
        oth_vari = list(vars(self).keys())
        if name.lower() in att_vari:
            return getattr(self.attributes,name.lower())
        elif name.lower() in soc_vari:
            return getattr(self.social_att,name.lower())
        elif name.lower() in ski_vari:
            return getattr(self.skills,name.lower())
        elif name.lower() in oth_vari:
            return getattr(self,name.lower())
        else:
            return 0
        
    def gen_sex(self):
        if self.sex_dist.lower() in ["male", "female", "none"]:
            self.sex = self.sex_dist
        else:
            lim = float(self.sex_dist)
            roll = random.random()
            if roll >= lim:
                self.sex = "Female"
            elif roll < lim:
                self.sex = "Male"
    
    def __init__(self, species, sex, rank, random=True, nature=None):
        self.species = species
#        print(species)            
        self.rank = rank
        self.nature, self.confidence = get_nature(nature)
        self.skills = skills()
        self.attributes = attributes()
        self.base_att = attributes()
        self.limits = limits()
        self.social_att = social_att()
        self.get_info()
        if sex.lower() in ["male", "female", "none"]:
            self.sex = sex
        else:
            self.gen_sex()
        self.moves = []
        self.champ = False
        if random == True:
            self.update()
        else:
            self.stat_bases()
        
