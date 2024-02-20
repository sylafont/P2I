from dependency import math, random
from Neurone import Neurone

class HiddenNeurone(Neurone) :

    def __init__(self, couche, rang, nb_connexion):
        #Se renseigner sur comment passer les attribus hérité en python
        super().__init__(couche,rang)
        self.nb_connexion = nb_connexion
        self.Poids_des_Connexions_avant = []
        self.initialise_connexion_weight()
        #self.print()
    
    def initialise_connexion_weight(self):
        #utiliser random.random() sur le bon interval
        for i in range(self.nb_connexion):
            self.Poids_des_Connexions_avant.append(random.uniform(-1,1))

    def Compute_Activation(self, Neurones_Antecedent):
        #On va créer une classe input layer et override cette méthode dedans pour dire input = activation
        somme = self.biais
        for neurone in Neurones_Antecedent:
            activation_neurone_precedent = neurone.activation
            poids = neurone.Poids_des_Connexions_avant[self.numero_rang]
            somme = activation_neurone_precedent*poids + somme
        somme = somme/785
        self.activation = 1/(1 + math.exp(-somme))

    def print(self):
        print("Type Neurone : Hidden Neurone, Rang : ", self.numero_rang, " Couche : ", self.numero_couche)