# Exercice 2
# creation de la fonction build_list
def build_list():
    Liste = []

    while True:
        # Saisie des informations de l'étudiant
        
        nom = str(input("veuiller entrez le nom de l'étudiant : "))
        age = int(input("veuiller entrez l'âge de l'étudiant : "))
        
        # Methode pour creer des sous ensemble
        Liste.append([nom, age])
        
         # Methode permettant a l'utilisateur de continuer ou pas 
        reponse = input("veuiller saisir le 1 si voulez continuer ou 0 si vous voulez quitter: ")
        if reponse == '1':
            continue
        else:
            break
        
    return Liste

# methode permettant d'afficher la solution(apple et affichage)
liste= build_list()
print("Liste non trié est :", liste)

# Exercice 3
#Creation de la methodes de permutation "switch"
def switch(liste,i, j):
     temp = list[j]
     liste[j] = [i]
     liste[i] = temp

# Creation de la fonction bubbleSort(liste) 
def bubbleSort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j][0] > liste[j+1][0]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

trie_noms = bubbleSort(liste.copy())
print("liste trié par noms est :", trie_noms)
            
# Creation de la fonction selectionSort(liste) 

def selectionSort(liste) :
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[min_idx], liste[i] = liste[i], liste[min_idx] 
    return liste

trie_taille= selectionSort(liste.copy())
print("liste trie par nombre:", trie_taille)

     


