from dependency import pickle
from InputNeurone import InputNeurone
from HiddenNeurone import HiddenNeurone
from OutputNeurone import OutputNeurone
from AccesBaseDeDonnes import Get_image
#peut etre faire matrice np à la place de liste de neurone pour chaque couche, comme ca on a autant de couche qu'on veut
class Reseau :
    
    def __init__(self, list_nb_neurone_par_couche):
        self.nb_couche = len(list_nb_neurone_par_couche)
        #self.nb_hidden_neurone = hidden_neurone
        #self.nb_output_neurone = output_neurone
        #self.nb_input_neurone = input_neurone
        self.list_nb_neurone_par_couche = list_nb_neurone_par_couche.copy()

        self.Initialise_Network()


    def Initialise_Network(self):
        #self.network = np.empty(self.nb_couche,)
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

            #self.network[i]= self.uneCouchedeNeurone.copy()
            self.network.append(uneCouchedeNeurone)
        #print("Shape du réseau : ", np.shape(self.network))



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
        for i in range(10):
            print(self.network[self.nb_couche-1][i].activation)
        

    def Compute_Loss_Function():
        pass

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


image = Get_image()
#testreseau1 = Reseau([784,17, 10])
testreseau1 = Reseau.Load_Network()
testreseau1.Compute_All_Activation(image)
#testreseau1.Save_Network()
