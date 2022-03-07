# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:59:20 2021

@author: Jesper
"""

import tkinter as tk
import make_pokemon as mp
import make_trainer as mt
import generate_pokemon as gp
import random
from generate_trainer import import_all


class info():
    def __init__(self):
        self.name = ""
        self.species = ""
        self.rank = ""
        self.sex = ""
        self.nature = ""

ranks = ["Starter", "Beginner", "Amateur", "Ace", "Professional", "Master", "Champion"]
sexs = ["Male", "Female", "None"]
nats = ["Adamant","Bashful","Bold","Brave","Calm","Careful","Docile","Gentle",
        "Hardy","Hasty","Impish","Jolly","Lax","Lonely","Mild","Modest","Naive",
        "Naughty","Quiet","Quirky","Rash","Relaxed","Sassy","Serious","Timid"]

window = tk.Tk()

window.columnconfigure([0,1],weight=1,minsize=2,pad=10)
window.rowconfigure([0,1,2,3,4,5,6],weight=1,minsize=30)

pkmn_info = info()

name_text = tk.Label(text="Name:")
name_text.grid(row=0,column=0)
name_entry = tk.Entry()
name_entry.grid(row=0,column=1)

spec_text = tk.Label(text="Species:")
spec_text.grid(row=1,column=0)
spec_entry = tk.Entry()
spec_entry.grid(row=1,column=1)

rank_text = tk.Label(text="Rank:")
rank_text.grid(row=2,column=0)
rank_var = tk.StringVar(window)
rank_var.set(ranks[0])
rank_menu = tk.OptionMenu(window, rank_var, *ranks)
rank_menu.grid(row=2,column=1)

sex_text = tk.Label(text="Sex:")
sex_text.grid(row=3,column=0)
sex_var = tk.StringVar(window)
sex_var.set(sexs[0])
sex_menu = tk.OptionMenu(window, sex_var, *sexs)
sex_menu.grid(row=3,column=1)

nat_text = tk.Label(text="Nature:")
nat_text.grid(row=4,column=0)
nat_var = tk.StringVar(window)
nat_var.set(nats[0])
nat_menu = tk.OptionMenu(window, nat_var, *nats)
nat_menu.grid(row=4,column=1)

rand_var = tk.BooleanVar(window)
rand_var.set(False)
rand_box = tk.Checkbutton(text="Random", variable=rand_var, onvalue=True, offvalue=False)
rand_box.grid(row=5,column=1)

def generate_name():
    rand_name = mt.get_name(random.choice(["Male", "Female"]))
    name_str = rand_name + "s " + spec_entry.get()
    name_entry.delete(0,tk.END)
    name_entry.insert(0,name_str)
    
def generate_species():
    pkmn_lst = import_all("pokemon.txt")
    rand_spec = random.choice(pkmn_lst)
    spec_entry.delete(0,tk.END)
    spec_entry.insert(0,rand_spec)
    
def generate_rank():
    rand_rank = random.choice(ranks)
    rank_var.set(rand_rank)

def get_pkmn_sex(species, path):
    r = open(path, "r")
    file = r.read().split("\n")
    pkmn_lst = []
    sex_str = None
    for j in range(len(file))[1:]:
        pkmn_str = file[j].split(";")
        if species == pkmn_str[0]:
            sex_str = pkmn_str[-1]
    if sex_str == None:
        output = random.choice(sexs)
    elif sex_str in sexs:
        output = sex_str
    else:
        sex_num = float(sex_str)
        gen_num = random.random()
        if gen_num < sex_num:
            output = "Male"
        elif gen_num >= sex_num:
            output = "Female"
    return output

def generate_sex():
    rand_sex = get_pkmn_sex(spec_entry.get(), "pokemon.txt")
    sex_var.set(rand_sex)
    
def generate_nature():
    rand_nature = random.choice(nats)
    nat_var.set(rand_nature)
    
def generate_all():
    generate_species()
    generate_sex()
    generate_name()
    generate_rank()
    generate_nature()
    rand_var.set(True)

rand_name_button = tk.Button(text="~", command=generate_name)
rand_name_button.grid(row=0,column=2)

rand_spec_button = tk.Button(text="~", command=generate_species)
rand_spec_button.grid(row=1,column=2)

rand_rank_button = tk.Button(text="~", command=generate_rank)
rand_rank_button.grid(row=2,column=2)

rand_sex_button = tk.Button(text="~", command=generate_sex)
rand_sex_button.grid(row=3,column=2)

rand_nat_button = tk.Button(text="~", command=generate_nature)
rand_nat_button.grid(row=4, column=2)

rand_all_button = tk.Button(text="All Random", command=generate_all)
rand_all_button.grid(row=5,column=0)

def ok_end():
    pkmn_info.name = name_entry.get()
    pkmn_info.species = spec_entry.get()
    pkmn_info.rank = rank_var.get()
    pkmn_info.sex = sex_var.get()
    pkmn_info.nature = nat_var.get()
    window.destroy()

#name_button = tk.Button(master=prompt_frame, text="X", command=get_name)
#name_button.pack()
    
ok_button = tk.Button(text="Next", command=ok_end)
ok_button.grid(row=6,column=1)

window.mainloop()

#%%

pokemon = mp.pokemon(pkmn_info.species, 
                     pkmn_info.sex, 
                     pkmn_info.rank, 
                     random=rand_var.get(),
                     nature=pkmn_info.nature)

root = tk.Tk()
root.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11],weight=1,minsize=1,pad=10)
root.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],weight=1,minsize=1,pad=10)

#name = tk.Label(text=pokemon.name)
#age = tk.Label(text=str(pokemon.age))
#sex = tk.Label(text=pokemon.sex)
#rank = tk.Label(text=pokemon.rank)
#name.grid(row=0,column=0)
#age.grid(row=0,column=1)
#sex.grid(row=0,column=2)
#rank.grid(row=0,column=3)

# ATTRIBUTES    

str_text = tk.Label(text="Strength")
dex_text = tk.Label(text="Dexterity")
vit_text = tk.Label(text="Vitality")
spe_text = tk.Label(text="Special")
ins_text = tk.Label(text="Insight")
str_val = tk.Label(text=str(pokemon.attributes.strength))
dex_val = tk.Label(text=str(pokemon.attributes.dexterity))
vit_val = tk.Label(text=str(pokemon.attributes.vitality))
spe_val = tk.Label(text=str(pokemon.attributes.special))
ins_val = tk.Label(text=str(pokemon.attributes.insight))

att_left_text = tk.Label(text="Att. points:")
att_left_num = tk.Label(text=str(pokemon.base_total + pokemon.abase - sum(list(vars(pokemon.attributes).values()))))

def update_stats():
    str_val["text"] = str(pokemon.attributes.strength)
    dex_val["text"] = str(pokemon.attributes.dexterity)
    vit_val["text"] = str(pokemon.attributes.vitality)
    spe_val["text"] = str(pokemon.attributes.special)
    ins_val["text"] = str(pokemon.attributes.insight)
    att_left_num["text"] = str((pokemon.base_total + pokemon.abase) - sum(list(vars(pokemon.attributes).values())))

def change(stat, inc):
    stat_val = getattr(pokemon.attributes, stat)
    new_stat = stat_val + inc
    
    low_lim = new_stat >= getattr(pokemon.base_att, stat)
    upp_lim = new_stat <= getattr(pokemon.limits, stat)
    tot_lim = sum(list(vars(pokemon.attributes).values())) + inc <= pokemon.base_total + pokemon.abase
    
    if low_lim and upp_lim and tot_lim:
        setattr(pokemon.attributes, stat, new_stat)
    update_stats()
    
str_inc = tk.Button(text="+", command=lambda:change("strength", 1))
dex_inc = tk.Button(text="+", command=lambda:change("dexterity", 1))
vit_inc = tk.Button(text="+", command=lambda:change("vitality", 1))
spe_inc = tk.Button(text="+", command=lambda:change("special", 1))
ins_inc = tk.Button(text="+", command=lambda:change("insight", 1))
str_dec = tk.Button(text="-", command=lambda:change("strength", -1))
dex_dec = tk.Button(text="-", command=lambda:change("dexterity", -1))
vit_dec = tk.Button(text="-", command=lambda:change("vitality", -1))
spe_dec = tk.Button(text="-", command=lambda:change("special", -1))
ins_dec = tk.Button(text="-", command=lambda:change("insight", -1))

str_text.grid(row=1,column=0)
dex_text.grid(row=2,column=0)
vit_text.grid(row=3,column=0)
spe_text.grid(row=4,column=0)
ins_text.grid(row=5,column=0)
str_dec.grid(row=1,column=1)
dex_dec.grid(row=2,column=1)
vit_dec.grid(row=3,column=1)
spe_dec.grid(row=4,column=1)
ins_dec.grid(row=5,column=1)
str_val.grid(row=1,column=2)
dex_val.grid(row=2,column=2)
vit_val.grid(row=3,column=2)
spe_val.grid(row=4,column=2)
ins_val.grid(row=5,column=2)
str_inc.grid(row=1,column=3)
dex_inc.grid(row=2,column=3)
vit_inc.grid(row=3,column=3)
spe_inc.grid(row=4,column=3)
ins_inc.grid(row=5,column=3)

att_left_text.grid(row=8,column=0)
att_left_num.grid(row=8,column=2)

# SOCIAL ATTRIBUTES

tou_text = tk.Label(text="Tough")
bea_text = tk.Label(text="Beauty")
coo_text = tk.Label(text="Cool")
cut_text = tk.Label(text="Cute")
cle_text = tk.Label(text="Clever")
tou_val = tk.Label(text=str(pokemon.social_att.tough))
bea_val = tk.Label(text=str(pokemon.social_att.beauty))
coo_val = tk.Label(text=str(pokemon.social_att.cool))
cut_val = tk.Label(text=str(pokemon.social_att.cute))
cle_val = tk.Label(text=str(pokemon.social_att.clever))

satt_left_text = tk.Label(text="Soc. Att. points:")
satt_left_num = tk.Label(text=str(5 + pokemon.sbase - sum(list(vars(pokemon.social_att).values()))))

def update_sstats():
    tou_val["text"] = str(pokemon.social_att.tough)
    bea_val["text"] = str(pokemon.social_att.beauty)
    coo_val["text"] = str(pokemon.social_att.cool)
    cut_val["text"] = str(pokemon.social_att.cute)
    cle_val["text"] = str(pokemon.social_att.clever)
    satt_left_num["text"] = str((5 + pokemon.sbase) - sum(list(vars(pokemon.social_att).values())))

def schange(stat, inc):
    stat_val = getattr(pokemon.social_att, stat)
    new_stat = stat_val + inc
    if new_stat <= 5 and new_stat >= 1 and sum(list(vars(pokemon.social_att).values())) + inc <= 5 + pokemon.sbase:
        setattr(pokemon.social_att, stat, new_stat)
    update_sstats()
    
tou_inc = tk.Button(text="+", command=lambda:schange("tough", 1))
bea_inc = tk.Button(text="+", command=lambda:schange("beauty", 1))
coo_inc = tk.Button(text="+", command=lambda:schange("cool", 1))
cut_inc = tk.Button(text="+", command=lambda:schange("cute", 1))
cle_inc = tk.Button(text="+", command=lambda:schange("clever", 1))
tou_dec = tk.Button(text="-", command=lambda:schange("tough", -1))
bea_dec = tk.Button(text="-", command=lambda:schange("beauty", -1))
coo_dec = tk.Button(text="-", command=lambda:schange("cool", -1))
cut_dec = tk.Button(text="-", command=lambda:schange("cute", -1))
cle_dec = tk.Button(text="-", command=lambda:schange("clever", -1))

tou_text.grid(row=1,column=4)
bea_text.grid(row=2,column=4)
coo_text.grid(row=3,column=4)
cut_text.grid(row=4,column=4)
cle_text.grid(row=5,column=4)
tou_dec.grid(row=1,column=5)
bea_dec.grid(row=2,column=5)
coo_dec.grid(row=3,column=5)
cut_dec.grid(row=4,column=5)
cle_dec.grid(row=5,column=5)
tou_val.grid(row=1,column=6)
bea_val.grid(row=2,column=6)
coo_val.grid(row=3,column=6)
cut_val.grid(row=4,column=6)
cle_val.grid(row=5,column=6)
tou_inc.grid(row=1,column=7)
bea_inc.grid(row=2,column=7)
coo_inc.grid(row=3,column=7)
cut_inc.grid(row=4,column=7)
cle_inc.grid(row=5,column=7)

satt_left_text.grid(row=9,column=0)
satt_left_num.grid(row=9,column=2)

# SKILLS

bra_text = tk.Label(text="Brawl")
cha_text = tk.Label(text="Channel")
cla_text = tk.Label(text="Clash")
eva_text = tk.Label(text="Evasion")
ale_text = tk.Label(text="Alert")
ath_text = tk.Label(text="Athletic")
nat_text = tk.Label(text="Nature")
ste_text = tk.Label(text="Stealth")
all_text = tk.Label(text="Allure")
eti_text = tk.Label(text="Etiquette")
int_text = tk.Label(text="Intimidate")
per_text = tk.Label(text="Perform")
bra_val = tk.Label(text=str(pokemon.skills.brawl))
cha_val = tk.Label(text=str(pokemon.skills.channel))
cla_val = tk.Label(text=str(pokemon.skills.clash))
eva_val = tk.Label(text=str(pokemon.skills.evasion))
ale_val = tk.Label(text=str(pokemon.skills.alert))
ath_val = tk.Label(text=str(pokemon.skills.athletic))
nat_val = tk.Label(text=str(pokemon.skills.nature))
ste_val = tk.Label(text=str(pokemon.skills.stealth))
all_val = tk.Label(text=str(pokemon.skills.allure))
eti_val = tk.Label(text=str(pokemon.skills.etiquette))
int_val = tk.Label(text=str(pokemon.skills.intimidate))
per_val = tk.Label(text=str(pokemon.skills.perform))

katt_left_text = tk.Label(text="Skill points:")
katt_left_num = tk.Label(text=str(pokemon.kbase - sum(list(vars(pokemon.skills).values()))))

def update_skills():
    bra_val["text"] = str(pokemon.skills.brawl)
    cha_val["text"] = str(pokemon.skills.channel)
    cla_val["text"] = str(pokemon.skills.clash)
    eva_val["text"] = str(pokemon.skills.evasion)
    ale_val["text"] = str(pokemon.skills.alert)
    ath_val["text"] = str(pokemon.skills.athletic)
    nat_val["text"] = str(pokemon.skills.nature)
    ste_val["text"] = str(pokemon.skills.stealth)
    all_val["text"] = str(pokemon.skills.allure)
    eti_val["text"] = str(pokemon.skills.etiquette)
    int_val["text"] = str(pokemon.skills.intimidate)
    per_val["text"] = str(pokemon.skills.perform)
    katt_left_num["text"] = str((pokemon.kbase) - sum(list(vars(pokemon.skills).values())))

def kchange(stat, inc):
    stat_val = getattr(pokemon.skills, stat)
    new_stat = stat_val + inc
    if new_stat <= pokemon.klim and new_stat >= 0 and sum(list(vars(pokemon.skills).values())) + inc <= pokemon.kbase:
        setattr(pokemon.skills, stat, new_stat)
    update_skills()
    
bra_inc = tk.Button(text="+", command=lambda:kchange("brawl", 1))
cha_inc = tk.Button(text="+", command=lambda:kchange("channel", 1))
cla_inc = tk.Button(text="+", command=lambda:kchange("clash", 1))
eva_inc = tk.Button(text="+", command=lambda:kchange("evasion", 1))
ale_inc = tk.Button(text="+", command=lambda:kchange("alert", 1))
ath_inc = tk.Button(text="+", command=lambda:kchange("athletic", 1))
nat_inc = tk.Button(text="+", command=lambda:kchange("nature", 1))
ste_inc = tk.Button(text="+", command=lambda:kchange("stealth", 1))
all_inc = tk.Button(text="+", command=lambda:kchange("allure", 1))
eti_inc = tk.Button(text="+", command=lambda:kchange("etiquette", 1))
int_inc = tk.Button(text="+", command=lambda:kchange("intimidate", 1))
per_inc = tk.Button(text="+", command=lambda:kchange("perform", 1))
bra_dec = tk.Button(text="-", command=lambda:kchange("brawl", -1))
cha_dec = tk.Button(text="-", command=lambda:kchange("channel", -1))
cla_dec = tk.Button(text="-", command=lambda:kchange("clash", -1))
eva_dec = tk.Button(text="-", command=lambda:kchange("evasion", -1))
ale_dec = tk.Button(text="-", command=lambda:kchange("alert", -1))
ath_dec = tk.Button(text="-", command=lambda:kchange("athletic", -1))
nat_dec = tk.Button(text="-", command=lambda:kchange("nature", -1))
ste_dec = tk.Button(text="-", command=lambda:kchange("stealth", -1))
all_dec = tk.Button(text="-", command=lambda:kchange("allure", -1))
eti_dec = tk.Button(text="-", command=lambda:kchange("etiquette", -1))
int_dec = tk.Button(text="-", command=lambda:kchange("intimidate", -1))
per_dec = tk.Button(text="-", command=lambda:kchange("perform", -1))

bra_text.grid(row=1,column=8)
cha_text.grid(row=2,column=8)
cla_text.grid(row=3,column=8)
eva_text.grid(row=4,column=8)
ale_text.grid(row=5,column=8)
ath_text.grid(row=6,column=8)
nat_text.grid(row=7,column=8)
ste_text.grid(row=8,column=8)
all_text.grid(row=9,column=8)
eti_text.grid(row=10,column=8)
int_text.grid(row=11,column=8)
per_text.grid(row=12,column=8)
bra_dec.grid(row=1,column=9)
cha_dec.grid(row=2,column=9)
cla_dec.grid(row=3,column=9)
eva_dec.grid(row=4,column=9)
ale_dec.grid(row=5,column=9)
ath_dec.grid(row=6,column=9)
nat_dec.grid(row=7,column=9)
ste_dec.grid(row=8,column=9)
all_dec.grid(row=9,column=9)
eti_dec.grid(row=10,column=9)
int_dec.grid(row=11,column=9)
per_dec.grid(row=12,column=9)
bra_val.grid(row=1,column=10)
cha_val.grid(row=2,column=10)
cla_val.grid(row=3,column=10)
eva_val.grid(row=4,column=10)
ale_val.grid(row=5,column=10)
ath_val.grid(row=6,column=10)
nat_val.grid(row=7,column=10)
ste_val.grid(row=8,column=10)
all_val.grid(row=9,column=10)
eti_val.grid(row=10,column=10)
int_val.grid(row=11,column=10)
per_val.grid(row=12,column=10)
bra_inc.grid(row=1,column=11)
cha_inc.grid(row=2,column=11)
cla_inc.grid(row=3,column=11)
eva_inc.grid(row=4,column=11)
ale_inc.grid(row=5,column=11)
ath_inc.grid(row=6,column=11)
nat_inc.grid(row=7,column=11)
ste_inc.grid(row=8,column=11)
all_inc.grid(row=9,column=11)
eti_inc.grid(row=10,column=11)
int_inc.grid(row=11,column=11)
per_inc.grid(row=12,column=11)

katt_left_text.grid(row=10,column=0)
katt_left_num.grid(row=10,column=2)

def OK_end2():
    root.destroy()
    
OK_but = tk.Button(text="OK", command=OK_end2)
OK_but.grid(row=17,column=8)

root.mainloop()

#%% MOVES

mroot = tk.Tk()

pos_moves = pokemon.get_move_lst()

rem_moves = min([pokemon.attributes.insight + 2, len(pos_moves)])

mroot.columnconfigure([0,1],weight=1,minsize=1,pad=10)
mroot.rowconfigure(list(range(rem_moves+1)),weight=1,minsize=1,pad=2)

menu = {}

for i in range(rem_moves):
    move_text = tk.Label(text="Move #"+str(i+1))
    move_var = tk.StringVar(mroot)
    if len(pokemon.moves) == 0:
        move_var.set(pos_moves[i])
    else:
        move_var.set(pokemon.moves[i].split(";")[0])
    move_menu = tk.OptionMenu(mroot, move_var, *pos_moves)
    move_text.grid(row=i,column=0)
    move_menu.grid(row=i,column=1)
    menu["move{0}".format(i)] = move_var
    
def OK_end3():
    pokemon.moves = []
    for j in range(len(menu)):
        pokemon.moves.append(menu["move{0}".format(j)].get())
    pokemon.update()
    gp.print_pokemon(pkmn_info.name,pokemon)
    mroot.destroy()
    
OK_but2 = tk.Button(text="OK", command=OK_end3)
OK_but2.grid(row=rem_moves,column=1)
    
 
mroot.mainloop()