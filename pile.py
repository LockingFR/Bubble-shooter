class Cellule:
    
    def __init__ (self,v,s):
        self.valeur=v
        self.suivante=s   # qui sera une cellule ou None

class Pile:
    def __init__ (self):
        self.tete=None

       
    
    def est_vide(self):
        return self.tete is None
    
    def donner_tete (self):
        assert not self.est_vide() , " Une pile vide n'a pas de tete"
        return self.tete.valeur
    
    
    def empiler(self,val):
        if self.est_vide() :
            c=Cellule(val,None)
            self.tete=c
        else :
            c= Cellule(val,self.tete)
            self.tete = c
            
    
    def depiler(self):
        assert not self.est_vide() , " Impossible de defiler une pile vide"
        
        v=self.tete.valeur
        self.tete=self.tete.suivante
        # Si la pile ne contenait qu'un element 
        return v
  
    
    def longueur(self):
        if self.est_vide():
            return 0
        else : 
            pile_tmp=Pile()
            pile_tmp.tete=self.tete.suivante
            return 1+ pile_tmp.longueur()     