#Collecte des donnees
students=[]
def build_list():
    liste = []
    nouveau=int(input("Nouveau etudiant 1=oui/0=non"))
    while(nouveau==1):
        name = input("Nom: ")
        age = input("lAge : ")
        liste.append((name, age))
        nouveau=int(input("Nouveau etudiant 1=oui/0=non"))
    return liste


# Permutte deu element de la liste
def switch(liste, i, j):
    #liste[i],  liste[j] = liste[j],  liste[i] 
    temp = liste[i] 
    liste[i] = liste[j]
    liste[j] = temp
    return liste

#Trie selection selon la note 1
def selection_sort_by_note(liste):
    print("TRI SELECTION")
    n = len(liste)
    for i in range(n):
        # Attribu le minimum au premier element
        index_mini = i
        # parcourt les elements non ordonnes
        for j in range(i + 1, n):
            if liste[j][1] < liste[index_mini][1]:
                index_mini = j
        # permute l'element minimum trouvé avec le premier element 
        switch(liste, i, index_mini)
        print(liste)
    return liste


#Trie bulle selon la note 2
def bubbleSort(liste):
    print("TRI BULLES")
    nbPermut = 1
    while(nbPermut>0):
        nbPermut=0
        print(liste)
        for i in range(len(liste)-1):
            if(liste[i][0] > liste[i+1][0]):
                nbPermut+=1
                liste=switch(liste,i, i+1)
    #for i in range(len(liste)):
    #    for j in range(0, n - i - 1):
    #        if liste[j][0] > liste[j + 1][0]:
    #            liste=switch(liste,j, j+1)
    #    print(liste)
    return liste

#Trie bulrapide le selon le nom
def quick_sort_by_name(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab.pop()
    petit = []
    grand = []
    for val in tab:
        if val < pivot[0]:
            petit.append(val)
        else:
            grand.append(val)

    return quickSort(petit) + [pivot] + quickSort(grand)
        
        
students = [("Viny", 34), ("Ryan", 43),("Tity", 31),("Antony", 27),("Calvin", 39),("Lilian", 27) ]
#print("Liste complete non triee:  ", students)
#students_sorted_by_selection = selection_sort_by_note(students)
#print("Trie bulle selon les noms: ", students)
#students_sorted_by_bubble = bubbleSort(students)

bubbleSort(students)
#students = selection_sort_by_note1(students)
#print("Trie selection selon la note 1: ", students)
#students = bubble_sort_by_note2(students)
#print("Trie bulle selon la note 2: ", students)
#students = quick_sort_by_name(students)
#print("Trie rapide selon le nom : ", students)

        
    
