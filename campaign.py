import random

Const_Linear = "linear"
Const_Semi_Linear = "semi_linear"
Const_Openworld = "openworld"

Const_Env_Plains = "plains"
Const_Env_Snowy = "snowy"
Const_Env_Jungle = "jungle"
Const_Env_Town = "town"
Const_Env_List = [Const_Env_Plains, Const_Env_Snowy, Const_Env_Jungle, Const_Env_Town]


class campaign:

    def __init__(self, type):
        self.type = type
        self.stageList = []  # only for linear
        self.sideStage = 0 # only for semi_linear
        self.quest = "" # only for openworld
        self.environment = Const_Env_Plains
        if type == Const_Linear:
            self.linear()
        elif type == Const_Semi_Linear:
            self.semi_linear()
        else: # open world
            self.openworld()

    def linear(self):
        print("Playing linear campaign")
        print("Generating map")
        count = 1
        while(count <= 5):
            self.stageList.append(Const_Env_List[random.randint(0, len(Const_Env_List)-1)])
            # print(f"Stage {count} : {self.stageList[count-1]}")
            count = count + 1


    def semi_linear(self):
        print("Playing semi_linear campaign")

    def openworld(self):
        print("Playing open world campaign")