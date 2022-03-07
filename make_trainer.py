# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:00:05 2021

@author: Jesper
"""

import random
import sys

class skills():
    def __init__(self):
        self.brawl       = 0
        self.throw       = 0
        self.evasion     = 0
        self.weapons     = 0
        self.alert       = 0
        self.athletic    = 0
        self.nature      = 0
        self.stealth     = 0
        self.allure      = 0
        self.etiquette   = 0
        self.intimidate  = 0
        self.perform     = 0
        self.crafts      = 0
        self.lore        = 0
        self.medicine    = 0
        self.science     = 0
    
class attributes():
    def __init__(self):
        self.strength    = 1
        self.dexterity   = 1
        self.vitality    = 1
        self.insight     = 1
    
class social_att():
    def __init__(self):
        self.tough       = 1
        self.cool        = 1
        self.beauty      = 1
        self.cute        = 1
        self.clever      = 1

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
                
def choose_random_attr(attr, points, limit):
    vari = list(vars(attr).keys())
    values = list(vars(attr).values())
    old_points = sum(values)
    
    if points > old_points:
        for i in range(points-old_points):
            done = False
            while done == False:
                
                avail_att = []
                for j in vari:
                    if getattr(attr,j) < limit:
                        avail_att.append(j)    
                if len(avail_att) < 1:
                    done = True
                    print("Ran out of space for point distribution!")
                    break
                
                att = random.choice(avail_att)
                att_num = getattr(attr, att)
                if att_num < limit:
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

def get_name(sex):
    f = open(sex.lower() + '_names.txt', 'r', encoding='utf-8')
    g = open('surnames.txt', 'r', encoding='utf-8')
    fname_lst = f.read().split('\n')
    sname_lst = g.read().split('\n')
    fname = random.choice(fname_lst)
    sname = random.choice(sname_lst)
    name = fname + ' ' + sname
    return name

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

class trainer():
    
    def stat_bases(self):
        if self.age < 13:
            abase = 0
            sbase = 2
        elif self.age < 20:
            abase = 2
            sbase = 2
        elif self.age < 65:
            abase = 4
            sbase = 4
        else:
            abase = 3
            sbase = 6
            
        if self.rank == "Starter":
            kbase = 5
            klim = 1
        elif self.rank == "Beginner":
            abase += 2
            sbase += 2
            kbase = 9
            klim = 2
        elif self.rank == "Amateur":
            abase += 4
            sbase += 4
            kbase = 12
            klim = 3
        elif self.rank == "Ace":
            abase += 6
            sbase += 6
            kbase = 14
            klim = 4
        elif self.rank == "Professional":
            abase += 8
            sbase += 8
            kbase = 15
            klim = 5
        elif self.rank == "Master":
            abase += 8
            sbase += 14
            kbase = 15
            klim = 5
            self.extra_pass = 2
        elif self.rank == "Champion":
            abase += 14
            sbase += 14
            kbase = 16
            klim = 5
        self.abase = abase
        self.sbase = sbase
        self.kbase = kbase
        self.klim = klim
    
    def update(self):
        if self.age < 13:
            abase = 0
            sbase = 2
        elif self.age < 20:
            abase = 2
            sbase = 2
        elif self.age < 65:
            abase = 4
            sbase = 4
        else:
            abase = 3
            sbase = 6
            
        self.rank_num = where(["Starter", "Beginner", "Amateur", "Ace", "Professional", "Master", "Champion"], self.rank)
        self.extra_pass = 0
        
        if self.rank_num >= 0:
            choose_random_skills(self.skills, 5, 1)
            choose_random_attr(self.attributes, 4+abase, 5)
            choose_random_attr(self.social_att, 5+sbase, 5)
        if self.rank_num >= 1:
            choose_random_skills(self.skills, 9, 2)
            choose_random_attr(self.attributes, 4+abase + 2, 5)
            choose_random_attr(self.social_att, 5+sbase + 2, 5)
        if self.rank_num >= 2:
            choose_random_skills(self.skills, 12, 3)
            choose_random_attr(self.attributes, 4+abase + 4, 5)
            choose_random_attr(self.social_att, 5+sbase + 4, 5)
        if self.rank_num >= 3:
            choose_random_skills(self.skills, 14, 4)
            choose_random_attr(self.attributes, 4+abase + 6, 5)
            choose_random_attr(self.social_att, 5+sbase + 6, 5)
        if self.rank_num >= 4:
            choose_random_skills(self.skills, 15, 5)
            choose_random_attr(self.attributes, 4+abase + 8, 5)
            choose_random_attr(self.social_att, 5+sbase + 8, 5)
        if self.rank_num >= 5:
            self.extra_pass = 2
            choose_random_attr(self.social_att, 5+sbase+14, 5)
        if self.rank_num >= 6:
            choose_random_attr(self.attributes, 4+abase + 14, 7)
            choose_random_skills(self.skills, 16, 5)
            
        self.hp = self.base_hp + self.attributes.vitality + self.extra_pass
        self.will = self.attributes.insight + 2 + self.extra_pass
    
    def __init__(self, name, age, sex, rank, random=True, nature=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.rank = rank
        self.base_hp = 4
        self.skills = skills()
        self.attributes = attributes()
        self.social_att = social_att()
        self.nature, self.confidence = get_nature(nature)
        self.hp = self.base_hp + self.attributes.vitality
        self.will = self.attributes.insight + 2
        if random == True:
            self.update()
        else:
            self.stat_bases()
        