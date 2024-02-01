import random
class Neurone :
    def __init__(self, liste_Neurones_Antecedent, liste_Neurones_Suivant, couche,rang, liste_Poids):
        self.numero_couche = couche #va permettre à l'initialisation du neurone de savoir combien de weight initialiser
        self.numero_rang = rang #va permettre de savoir quel weight prendre lorsqu'on calcule le cout total
        self.Neurones_Antecedent = liste_Neurones_Antecedent.copy()#Vérifier qu'on passe bien la référence de la liste et non juste les valeurs
        self.Neurones_Suivants = liste_Neurones_Suivant.copy()
        self.Poids_des_Connexions_avant = liste_Poids.copy()
        self.Liste_Gradient_Weight = liste_Poids.copy()#Potentiellement faire liste tuple pour combiner le gradient et son poids
        self.biais = random.random()#Se renseigner pour voir quel interval donner à la fonction random ici
        self.activation = 0
        self.GradientBiais = 0
        

    def Compute_Activation(self, activation):
        pass

    def Compute_GradientBiais(self, biais):#fonction qui doit être override pour les neurones de l'outpout layer
        pass

    def Compute_GradientWeights(self, biais, Neurones_Suivants, ):
        pass #
    
    def Compute_New_Weights(self, Poids_des_Connexions_avant, GradientBiais):
        pass

    def Compute_New_Biais(self, biais):
        pass

    
#Note : Ne pas implémenter de class weigth, ajouter une fonction de class iteration reseaux

    

