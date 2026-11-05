

class Compte():
    def __init__(self):
        self.solde = 0 #J'initie le compte'
        self.depot = 0
        retrait = 0
        
    @property
    def depot(self):
        return self._depot
        
    @depot.setter
    def depot(self, montant):
        if montant < 0:
            raise ValueError("La somme déposée doit etre positive")
            
        else :
          #  self._montant = montant
            self._depot= montant
            self.solde += self._depot
    #    return self.solde

    @property
    def retrait(self):
        return self._retrait
        
    @retrait.setter
    def retrait(self, montant):
        if montant >= 0:
            if self.solde > montant:
                self._retrait = montant
                self.solde -= self._retrait
                print(f'Retrait effectué. \nVous avez retiré {montant} dans votre solde. Il vous reste encore {self.solde}.')
            else:
                print(f'Votre solde est insuffisant. \nVous ne pouvez pas retirer {montant} dans votre solde. Il ne vous reste que {self.solde}.')
        elif montant < 0:
            raise ValueError("Le montant à rétirer doit être positif")
       
            
                
        


s = Compte()

s.depot = 20000
s.retrait = 411500
#print(s.solde)


#b = Compte()
#print(b.depot(50500))