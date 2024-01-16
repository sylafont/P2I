class Neurone :
    def __init__(self, liste_Neurones, couche,rang, liste_Poids  ):
        self.numero_couche = couche #va permettre à l'initialisation du neurone de savoir combien de weight initialiser
        self.numero_rang = rang #va permettre de savoir quel weight prendre lorsqu'on calcule le cout total
        self.Neurones_Antecedent = liste_Neurones.copy()#Vérifier qu'on passe bien la référence de la liste et non juste les valeurs
        self.Poids_des_Connexions_avant = liste_Poids.copy()
        
    
