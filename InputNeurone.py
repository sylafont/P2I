from Neurone import Neurone
from dependency import math, random

class InputNeurone(Neurone) :
    
    def __init__(self, couche, rang, nb_connexion):#voir si liste poids est vraiment à passer en paramètre ou pas
        self.activation =0
        self.Poids_des_Connexions_avant = []
        super().__init__(couche,rang)
        self.nb_connexion = nb_connexion
        self.initialise_connexion_weight()

    def initialise_connexion_weight(self):
        #utiliser random.random() sur le bon interval
        for i in range(self.nb_connexion):
            self.Poids_des_Connexions_avant.append(random.random())


    def feedInput(self, valeur_pixel):
        self.activation = valeur_pixel