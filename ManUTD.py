class Trophy:
    def celebrate(self):
        print("Celebrating a trophy.....")
        
class PremierLeague(Trophy):
    def celebrate(self):
        print(" ManUnited is 20 Times PremierLeague Champions")
        
class ChampionsLeague(Trophy):
    def celebrate(self):
        print("ManUnited is 3 Times ChampionsLeague Champions")
        
class FACup(Trophy):
    def celebrate(self):
        print("ManUnited is 13 Times FA Cup Champions")  

class EFLCup(Trophy):
    def celebrate(self):
        print("ManUnited is 6 Times EFLCup Champions")
    
class ManchesterUnited:
    
    def __init__(self , strategy):
        self.strategy = strategy
    
    def win_trophy(self):
        self.strategy.celebrate()
        
pl_trophy = PremierLeague()
ucl_trophy = ChampionsLeague()
fa_trophy = FACup()
efl_trophy = EFLCup()
        
team = ManchesterUnited(pl_trophy)
team.win_trophy()

team = ManchesterUnited(ucl_trophy)
team.win_trophy()

team = ManchesterUnited(fa_trophy)
team.win_trophy()

team = ManchesterUnited(efl_trophy)
team.win_trophy()
