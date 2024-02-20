from dependency import pickle
from InputNeurone import InputNeurone
from HiddenNeurone import HiddenNeurone
from OutputNeurone import OutputNeurone
from AccesBaseDeDonnes import Get_image_And_Label

class Reseau :
    
    def __init__(self, list_nb_neurone_par_couche):
        self.nb_couche = len(list_nb_neurone_par_couche)
        self.list_nb_neurone_par_couche = list_nb_neurone_par_couche.copy()
        self.nb_output_neurone = list_nb_neurone_par_couche[self.nb_couche -1]
        self.cost = 0
        self.Initialise_Network()
        self.y_predicted = list(0 for i in range(0, self.nb_output_neurone))


    def Initialise_Network(self):
        self.network = []

        for i in range(self.nb_couche):
            uneCouchedeNeurone = []
            for j in range(self.list_nb_neurone_par_couche[i]):
                if(i==0):
                    nb_neurone_couche_suivante = self.list_nb_neurone_par_couche[i+1]
                    neurone = InputNeurone(i, j,nb_neurone_couche_suivante )
                elif(i!= self.nb_couche -1) :#rajouter un elif si on change et qu'on met aussi un output neurone
                    nb_neurone_couche_suivante = self.list_nb_neurone_par_couche[i+1]
                    neurone = HiddenNeurone(i,j, nb_neurone_couche_suivante)
                else :
                    neurone = OutputNeurone(i,j)
                uneCouchedeNeurone.append(neurone)
            self.network.append(uneCouchedeNeurone)

    def Compute_All_Activation(self, pixel_image):
        for i, coucheDeNeurone in enumerate(self.network):
            if(i==0): #Il s'agit de la couche inputNeurone
                for j,input_neurone in enumerate(coucheDeNeurone) :
                    input_neurone.feedInput(pixel_image[j])
            else :
                couchePrecedente = self.network[i-1]
                for j, neurone in enumerate(coucheDeNeurone) :
                    neurone.Compute_Activation(couchePrecedente)
        print("Activation output layer :")
        for i in range(10): #On affiche les activations et on les mets dans un vecteur pour y_predicted
            print(self.network[self.nb_couche-1][i].activation)
            self.y_predicted[i] = self.network[self.nb_couche-1][i].activation


    
    def Transform_Label_To_Vector(self, y_label):
        y_real = list(0 for i in range(0, self.nb_output_neurone))
        y_real[int(y_label)] = 1
        return y_real
        
    
    def Compute_Loss_Function(self, y_label):
        y_real = self.Transform_Label_To_Vector(y_label)
        """Fonction à changer si on veut pouvoir calculer le cout après le passage de plusieurs image"""
        somme =0
        for i, value in enumerate(y_real):
            somme = somme + (value - self.y_predicted[i])**2
        self.cost = somme 
        print("Cout de la fonction : ", self.cost)


    def Save_Network(self):
        try:
            with open("network.pickle", "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)#Warning with highest protocol peut être incompatible avec certaines version de python
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    @classmethod 
    def Load_Network(cls) :
        try:
            with open("network.pickle", "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)


image, label = Get_image_And_Label(1)
#testreseau1 = Reseau([784,17, 10])
testreseau1 = Reseau.Load_Network()
testreseau1.Compute_All_Activation(image)
testreseau1.Compute_Loss_Function(label)
testreseau1.Save_Network()
