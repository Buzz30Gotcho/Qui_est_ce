from project.src.generateur.perso import Perso
from project.src.generateur.attribut import Attribut 
import os

"""
TODO :
    -> charger un fichier json
"""


class Generateur:
    def __init__(self,path:str=""):
        self.all_attributs=[]
        self.liste_perso=[]
        
        self.nbLignes = 1
        
        
        self.largeurImage = 0
        self.hauteurImage = 0

        self.espacementPhoto= 0
        self.tailleImage= 100
        
        self.path = path
        if not path == "":
            for i in os.listdir(path):
                    p=Perso(i,i.split(".")[0])
                    # print(i.split(".")[0])
                    
                    self.liste_perso.append(p)
        self.nbColonnes = len(self.liste_perso)

    
    def get_perso_similaire(self):
        perso_identique=[]
        nb_attribut_identique = 0
        
        for p1 in self.liste_perso:
            for p2 in self.liste_perso:
                
                if not p1 is p2:
                    nb_attribut_identique = 0
                    for un_attribut in self.all_attributs:
                        if un_attribut.nom in p1.description and un_attribut.nom in p2.description:
                            if p1.description[un_attribut.nom] == p2.description[un_attribut.nom]:
                                nb_attribut_identique += 1
                    if nb_attribut_identique == len(self.all_attributs):
                        if not p1 in perso_identique:
                            perso_identique.append(p1)
                        if not p2 in perso_identique:
                            perso_identique.append(p2)
        
        return perso_identique
    
    def verif_nom(self, nom:str):
        for attr in self.all_attributs:
            if attr.nom == nom:
                raise NameError("nom déjà utilisé")
    
    def creer_nouvelle_attribut(self, nom:str, choix_multiple):
        """Renvoie une erreur si un autre attribut a déjà le même nom"""
        
        self.verif_nom(nom)
        
        new_attr = Attribut(nom, choix_multiple)
        self.all_attributs.append(new_attr)
        
        
        for p in self.liste_perso:
            p.ajouter_attribut(nom)
            
    def modif_attribut(self, nouveau_nom:str, un_attribut:Attribut):
        """Change le nom d'un attribut par l'argument nouveau_nom. Le nom de l'attribut est aussi modifié pour les perso dans self.liste_perso.
        
        Requis : un_attribut doit être dans self.all_atributs, sinon renvoie une erreur"""
        
        self.verif_nom(nouveau_nom)
        
        #sauvegarde
        vieux_nom = un_attribut.nom
        
        #modif dans attribut
        un_attribut.nom = nouveau_nom
        
        #modif dans perso
        for p in self.liste_perso:
            sauvegarde_valeur = p.description[vieux_nom]    #sauvegarde
            p.description.pop(vieux_nom)                    #effaçage
            p.description[nouveau_nom] = sauvegarde_valeur  #remplacement
            
    def modif_valeur(self, ancien_val:str, nouvelle_val:str, un_attribut:Attribut):
        """Remplace l'ancien_val par nouvelle_val pour l'attribut un_attribut. La valeur est aussi modifié pour les perso dans self.liste_perso.
        N'ajoute rien si la nouvelle_val est déjà dans le domaine de valeur car set.
        
        Requis : ancien_val doit être dans un_attribut.domaine_valeur, renvoie KeyError à cause de remove() sinon"""
        

        
        #modif dans attribut
        un_attribut.domaine_valeur.remove(ancien_val)    
        un_attribut.add_valeur(nouvelle_val)
        
        #modif dans perso
        for p in self.liste_perso:
            if ancien_val in p.description[un_attribut.nom]:
                p.description[un_attribut.nom].remove(ancien_val)
                p.description[un_attribut.nom].add(nouvelle_val)
                
    def supp_attribut(self, un_attribut:Attribut):
        """Efface un_attribut donné dans self.all_attributs. L'a clé (dans Perso.description) correspondante a l'argument est aussi supprimé pour tous les perso.
        
        Requis : un_attribut doit être dans self.all_atributs, sinon supprime le dernier element dans all_atributs et renvoie proablement une erreur"""
        
        #recherche de l'indice de un_attribut dans la liste all_attributs
        for i in range(len(self.all_attributs)):
            if self.all_attributs[i] is un_attribut:
                break
        
        #modif dans attribut    
        self.all_attributs.pop(i)
        
        #suppression de l'attribut pour tout les perso        
        for p in self.liste_perso:
            p.description.pop(un_attribut.nom)
            
    def supp_valeur(self, val:str, un_attribut:Attribut):
        """Efface la valeur val dans l'attribut un_attribut. Si un perso est décrit par cette valeur, la valeur est supprimé de sa description.
        
        Requis : val doit être dans un_attribut, renvoie KeyError à cause de remove() sinon
        
        /!\ Si l'attribut possède 2 valeurs, cette méthode supprime définitivement l'attribut"""
        
        #l'attribut possèdera + de 1 seul attribut même après suppression
        if len(un_attribut.domaine_valeur) > 2:
            #modif dans attribut
            un_attribut.domaine_valeur.remove(val)
            
            #modif dans perso
            for p in self.liste_perso:
                p.description[un_attribut.nom].discard(val)
        
        #l'attribut possèdera 1 seule valeur, on le supprime
        else:
            self.supp_attribut(un_attribut)

            
    def a_bonne_taille(self):
        taille = len(self.liste_perso)
        
        if (taille > (self.nbLignes-1)*self.nbColonnes)\
        and (taille <= self.nbLignes*self.nbColonnes):
            return 0
            
        return len(self.liste_perso)  


    def supp_attr_dans_perso_qui_ont_une_seul_valeur(self) -> None:
        """Supprime les clés dans la description des perso, correspondant à des attributs, qui sont associés à un ensemble identique entre tous 
        les perso pour cet attribut. Exemple : tous les perso ont les cheveux noirs et blancs. On supprime l'attribut cheveux."""
        
        liste_attr_a_supp = []
        
        for a in self.all_attributs:
            val = self.liste_perso[0].description[a.nom]
            attr_qui_donne_une_seul_valeur_pour_tous_les_perso = True
            
            for p in self.liste_perso:
                if not val == p.description[a.nom]:
                    attr_qui_donne_une_seul_valeur_pour_tous_les_perso = False
            #End for
            
            if attr_qui_donne_une_seul_valeur_pour_tous_les_perso:
                liste_attr_a_supp.append(a.nom)
            #End if
        #End for
        
        for nom_attribut in liste_attr_a_supp:
            for p in self.liste_perso:
                p.description.pop(nom_attribut)
                
        return liste_attr_a_supp


        
    def nb_perso_max(self):
        """Renvoie le nombre théorique maximal de personnage unique que l'ensemble des attributs avec leurs valeurs associés peuvent supporter."""
        
        res = 1
        
        for a in self.all_attributs:
            res = res*a.possibilites()
            
        return res

    def generer_fichier_json(self):
        print(self.path)
        # print(self.path)
        print("test" ,self.path.split('/', -1)[-2])
        nom = self.path.split('/', -1)[-2]
        # p = f"./ressources/JSON/{self.path.rsplit('/', 1)[-2]}.json"
        p = f"./ressources/JSON/{nom}.json"
        print("p", p)
        file_descriptor = open(p,"wt") #write text
        
        file_descriptor.write("{\n")
        
        string_meta = "    \"metadonnees\": {\n"
        string_meta += f"        \"images\": \"{self.path}\",\n"
        string_meta += f"        \"ligne\": {self.nbLignes},\n"
        string_meta += f"        \"colonne\": {self.nbColonnes},\n"
        string_meta += f"        \"largeurImage\": {self.largeurImage},\n"
        string_meta += f"        \"hauteurImage\": {self.hauteurImage},\n"
        string_meta += f"        \"espacementPhoto\": {self.espacementPhoto},\n"
        string_meta += f"        \"tailleMaxHauteurImage\": {self.tailleImage}\n"
        string_meta += "    },\n"   
        
        file_descriptor.write(string_meta)
        
        string_possibilites = "    \"possibilites\": {\n"
        for i in range (len(self.liste_perso)):

            string_possibilites += f"        \"{i}\":" + "{\n"
            string_possibilites += "            \"fichier\":" + "[\"" + self.liste_perso[i].fichier + "\"],\n"
            string_possibilites += "            \"nom\":" + "[\"" + self.liste_perso[i].nom + "\"],\n" 
            for key,value in self.liste_perso[i].description.items():
                string_possibilites += "            \"" + key + "\":[" 
                for valeur in value :
                    string_possibilites += "\"" + valeur + "\","
                string_possibilites = string_possibilites[:-1] + "],\n"
            string_possibilites = string_possibilites[:-2] + "\n        },\n"
            
        string_possibilites = string_possibilites[:-2] + "\n    },\n" 
        file_descriptor.write(string_possibilites)


        string_attributs = "    \"attributs\": {\n"
        for attribut in self.all_attributs:
            string_attributs += f"       \"{attribut.nom}\" : ["
            string_attributs += f"\"{attribut.choix_multiple}\", "
            for valeur in attribut.domaine_valeur:
                string_attributs += f"\"{valeur}\","
            string_attributs = string_attributs[:-1] + "],\n"
        string_attributs = string_attributs[:-2] + "\n      }\n}"
        file_descriptor.write(string_attributs)

    

    def charge_Fichier_Json(self, DicoJson):
        
        
        #ajout des metadonnees, jsp
        self.nbLignes = DicoJson["metadonnees"]["ligne"]
        self.nbColonnes = DicoJson["metadonnees"]["colonne"]
        
        
        self.largeurImage = DicoJson["metadonnees"]["largeurImage"]
        self.hauteurImage = DicoJson["metadonnees"]["hauteurImage"]

        self.espacementPhoto= DicoJson["metadonnees"]["espacementPhoto"]
        self.tailleImage= DicoJson["metadonnees"]["tailleMaxHauteurImage"]


        #ajout de tous les attributs dans "all_attributs"
        for attribut, valeurs in DicoJson["attributs"].items():
            choix_multiple = True if valeurs[0] == "True" else False
            self.creer_nouvelle_attribut(attribut, choix_multiple)

            for valeur in valeurs[1:]:
                self.all_attributs[-1].add_valeur(valeur)

        

        #pour tous les perso, ajout de leurs caractéristiques
        

        for dicoPerso in list(DicoJson["possibilites"].values()):
            del(dicoPerso["nom"])

            for persoExistant in self.liste_perso:
                if dicoPerso["fichier"][0] == persoExistant.fichier:
                    del(dicoPerso["fichier"])

                    for nomAttr, listeValeurs in dicoPerso.items():
                        persoExistant.ajouter(nomAttr, set(listeValeurs))
                    break
                
        
        


    def comparer_perso_aux_restes(self, un_perso:Perso):
        """Retourne une liste contenant les perso qui ont la même description"""
        
        res = []
        
        for p in self.liste_perso:
            if p is not un_perso:
                if un_perso.comparaison(p):
                    res.append(p)
        
        return res
        
        
        
        
        
        
        
        
