pyth_0 = {"pyth_0": "#python #programming #coding #java #javascript #programmer #snake #developer #code #machinelearning #html #datascience #reptile #ballpython #coder #reptilesofinstagram #pythonprogramming #snakes #snakesofinstagram #reptiles #computerscience #technology #php #linux #css #artificialintelligence #pythonsofinstagram #tech #webdeveloper #bhfyp"}
pyth_1 = {"pyth_1": "#software #ai #webdevelopment #hacker #pythons #deeplearning #codinglife #cybersecurity #ballpythons #c #ballpythonsofinstagram #softwaredeveloper #programmingmemes #computer #programminglife #programmers #pythoncode #data #webdesign #royalpython #kalilinux #development #softwareengineer #dataanalytics #reptilelover #pythonregius #android #bhfyp #datascientist #bigdata"}
prog_0 = {"prog_0": "#programmer #programming #coding #developer #coder #code #python #javascript #java #webdeveloper #html #computerscience #codinglife #technology #software #css #webdevelopment #softwaredeveloper #programmers #tech #php #linux #programmerlife #softwareengineer #programminglife #development #hacker #hacking #webdesign #bhfyp"}
prog_1 = {"prog_1": "#programmingmemes #computer #developers #programmerhumor #cybersecurity #android #developerlife #coders #daysofcode #dev #pythonprogramming #coderlife #web #machinelearning #webdev #codingisfun #hackers #kalilinux #peoplewhocode #devlife #geek #learntocode #frontend #raspberrypi #c #design #artificialintelligence #softwaredevelopment #programmerrepublic #codingmemes"}
game_0 = {"game_0": "#gaming #gamer #ps #videogames #game #playstation #xbox #games #fortnite #twitch #pc #memes #xboxone #gamers #pcgaming #youtube #gta #gamergirl #nintendo #gamingcommunity #pubg #callofduty #streamer #meme #follow #esports #videogame #instagaming #k #bhfyp"}
game_1 = {"game_1": "#instagamer #like #cod #gaminglife #funny #art #pcgamer #bhfyp #twitchstreamer #nintendoswitch #gamingmemes #anime #gameplay #fortniteclips #gamerlife #online #csgo #retrogaming #modernwarfare #pro #youtuber #destiny #minecraft #pubgmobile #apexlegends #lol #gamingsetup #photography #battleroyale #cosplay"}
tech_0 = {"tech_0": "#technology #tech #innovation #engineering #business #iphone #science #design #apple #electronics #technews #gadgets #smartphone #android #instagood #pro #software #programming #computer #samsung #instatech #bhfyp #gadget #security #mobile #coding #education #techie #future #bhfyp"}
tech_1 = {"tech_1": "#ai #artificialintelligence #startup #cybersecurity #digital #robotics #techno #engineer #covid #iot #marketing #technologynews #instagram #oneplus #tecnologia #it #india #d #love #s #computerscience #internet #follow #entrepreneur #photooftheday #geek #google #automation #news #g"}
devs_0 = {"devs_0": "#development #developer #design #programming #business #construction #coding #realestate #programmer #technology #software #webdevelopment #architecture #javascript #webdesign #code #growth #training #education #learning #love #html #python #webdeveloper #property #motivation #java #tech #website #bhfyp"}
devs_1 = {"devs_1": "#leadership #css #entrepreneur #marketing #coder #covid #building #web #php #inspiration #community #android #developers #india #engineering #project #codinglife #investment #innovation #softwaredeveloper #life #programmers #goals #computerscience #branding #instagood #coaching #photography #dev #skills"}
engi_0 = {"engi_0": "#engineering #engineer #technology #construction #design #architecture #science #civilengineering #engineers #mechanicalengineering #memes #manufacturing #innovation #tech #mechanical #engineeringlife #engineeringmemes #electronics #education #robotics #civil #electricalengineering #building #d #electrical #engineeringstudent #cnc #bhfyp #industrial #bhfyp"}
engi_1 = {"engi_1": "#college #civilengineer #machining #m #stem #art #automation #india #industry #love #physics #business #i #machine #student #o #concrete #instagood #photography #fabrication #engenhariacivil #covid #life #instagram #work #welding #mechanic #steel #programming #project"}
comp_0 = {"comp_0": "#computerscience #coding #programming #technology #programmer #python #computer #tech #developer #coder #java #code #javascript #webdeveloper #codinglife #engineering #softwareengineer #machinelearning #softwaredeveloper #computerengineering #linux #artificialintelligence #cybersecurity #software #html #programmers #hacking #programmingmemes #informationtechnology #bhfyp"}
comp_1 = {"comp_1": "#programminglife #webdevelopment #hacker #science #php #css #pythonprogramming #ai #programmerlife #computers #codingmemes #developerlife #webdesign #deeplearning #kalilinux #developers #codingisfun #coderlife #ethicalhacking #programmerhumor #geek #computerprogramming #development #security #softwareengineering #memes #c #softwaredevelopment #learntocode #hackers"}


import random, sys

class Tag_Generator(object):
    def __init__(self):
        self.tags = [pyth_0, pyth_1, prog_0, prog_1, game_0, game_1, tech_0, 
                     tech_1, devs_0, devs_1, engi_0, engi_1, comp_0, comp_1]
        self.unique_tags = self.counter()[0]          # Amount of unique tags.
        self.total_tags  = self.counter()[1]          # Amount of total tags.
        self.subjects    = self.counter()[2]          # Different subject tags.
        self.mixed_tags  = self.mixer()               # Mixed tags.
        self.rdm_choice  = random.choice(self.tags)   # Random subject tags.
        

    def counter(self):
        unique_tags = []
        subjects = []
        total_tags = 0
        for key, value in self.tags:
            subjects.append(key)
            for tag in value:
                if tag not in unique_tags:
                    unique_tags.append(tag)
                count += 1
        return unique_tags, total_tags, subjects 
    
    def mixer(self):
        mixed = []
        while len(mixed) < 30:
            tag = random.choice(self.unique_tags)
            if tag not in mixed:
                mixed.append(tag)
        return mixed
    
    def __repr__(self):
        print("[Tag Generator]"
              "[1] Total Tags."
              "[2] Random Category."
              "[3] Mixed Tags.")

        while True:
            try:
                choice = int(input("-> "))
                if choice == 1:
                    return str(f"Total: {self.total_tags}\nUnique: {len(self.unique_tags)}")
                elif choice == 2:
                    return str(f"Category: {self.random_choice}")
                elif choice == 3:
                    mixed_tags = ' '.join([tag for tag in self.mixed_tags]) 
                    return mixed_tags
                else:
                    continue
            except:
                continue


if __name__ == "__main__":
    print(Tag_Generator())
