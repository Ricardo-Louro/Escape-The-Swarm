from Functions import *


#--------------------------UNIT TYPES---------------------------------------------------------------------------------------

class Attack_Unit:
    Name = "DEFAULT ATTACK UNIT NAME"
    HP = 0
    AP = 0
    Type = "DEFAULT ATTACK UNIT TYPE"
    Cost = 0
    
class Defense_Unit:
    Name = "DEFAULT DEFENSE UNIT NAME"
    Cost = 0
    def Effect(self, Defense_List, Target_List):
        return

#------------------------------ATTACK UNITS---------------------------------------------------------------------------------------

class Swarmling(Attack_Unit):
    Name = "Swarmling"
    HP = 1
    AP = 2
    Type = "Grounded"
    Cost = 1
    
class Mutahisk(Attack_Unit):
    Name = "Mutahisk"
    HP = 1
    AP = 2
    Type = "Flying"
    Cost = 2

class Ravager(Attack_Unit):
    Name = "Ravager"
    HP = 3
    AP = 5
    Type = "Grounded"
    Cost = 3
    
class Hydrahisk(Attack_Unit):
    Name = "Hydrahisk"
    HP = 5
    AP = 10
    Type = "Grounded"
    Cost = 5

class Banehing(Attack_Unit):
    Name = "Banehing"
    HP = 1
    AP = 15
    Type = "Grounded"
    Cost = 5
    
class Ultrahisk(Attack_Unit):
    Name = "Ultrahisk"
    HP = 10
    AP = 20
    Type = "Grounded"
    Cost = 10

class Swarm_Lord(Attack_Unit):
    Name = "Swarm Lord"
    HP = 5
    AP = 15
    Type = "Flying"
    Cost = 10
    
#------------------------------DEFENSE UNITS---------------------------------------------------------------------------------------

class Machine_Gun_Squad(Defense_Unit):
    Name = "Machine Gun Squad"
    Cost = 2
    
    def Effect(self, Defense_List, Target_List):
            Counter = 4
            for Target in Target_List:
                if Counter == 0:
                    break
                if Target.Type == "Grounded":
                    Counter -= 1
                    Target.HP -= 1
            Destroy_Unit(Defense_List, self)
                

class Spiked_Wall(Defense_Unit):
    Name = "Spiked Wall"
    Cost = 3
    
    def Effect(self, Defense_List, Target_List):
        for Target in Target_List:
            if Target.Type == "Grounded" and Target.AP > 5:
                Destroy_Unit(Target_List, Target)
            else:
                Destroy_Unit(Defense_List, self)
                break