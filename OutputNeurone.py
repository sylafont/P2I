from dependency import math
from Neurone import Neurone

class OutputNeurone(Neurone) :

    def __init__(self, couche, rang):
        #Se renseigner sur comment passer les attribus hérité en python
        super().__init__(couche,rang)
        #self.print()
    
    def Compute_Activation(self, Neurones_Antecedent):
        #On va créer une classe input layer et override cette méthode dedans pour dire input = activation
        somme = self.biais
        for neurone in Neurones_Antecedent:
            activation_neurone_precedent = neurone.activation
            poids = neurone.Poids_des_Connexions_avant[self.numero_rang]
            somme = activation_neurone_precedent*poids + somme
        somme = somme /18
        self.activation = 1/(1 + math.exp(-somme))

    def print(self):
        print("Type Neurone : Output Neurone, Rang : ", self.numero_rang, " Couche : ", self.numero_couche)