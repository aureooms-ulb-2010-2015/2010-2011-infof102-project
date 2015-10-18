# -*- coding: utf-8 -*-
from os import system

#pour créer la mémoire

M= [0]*100

#L1Data:donnee en memoire

L1Data = [0] * 10

#L1Addr:adresse de la donnee coresspondante

L1Addr = ['NaN'] * 10

#L1Dirt:vrai si il faut réécrire en mémoire faux si déjà fait

L1Dirt = [False] * 10

#donnée la plus vieille = valeur data[i] où lastuse[i] est le plus petit

LastUse = [0] * 10

#nouvelle valeur pour la donnée la plus récente

genCounter = 1

#ch/cm

cacheHits = 0
cacheMiss = 0

end = False
system('clear')

while not end:
    
    cmd = raw_input("Available options:\n1==>Print\n2==>W/R\n3==>End\n\n")
    system('clear')
    while not (cmd in {'1':None,'2':None,'3':None}):
	
        cmd = raw_input("Available options:\n1==>Print\n2==>W/R\n3==>End\n\n")
        system('clear')

    if cmd == '1':
        print 'M =',M
        print 'L1Data =',L1Data
        print 'L1Addr =',L1Addr
        print 'L1Dirt =',L1Dirt
        print 'LastUse =',LastUse
        print 'cache hits =',cacheHits
        print 'cache miss =',cacheMiss
	raw_input("PRESS RETURN")
	system('clear')
        
    elif cmd == '2':
        toDo = raw_input("Write = 'W Addr Data'\tRead = 'R Addr'\n\n")
	print ''
        listToDo = toDo.split()
        correctCMD = True


        
        if (listToDo[0]!='W' and listToDo[0]!='R'):
            correctCMD = False
            print "CMD ERROR #0: CMD MUST BEGIN WITH INSTRUCTION W OR R"

        elementIndex = 0    
        while elementIndex < len(listToDo) and correctCMD:
            if (not(listToDo[elementIndex].isdigit())) and listToDo[elementIndex] != 'W' and listToDo[elementIndex] != 'R':
                correctCMD = False
                print "CMD ERROR #1: INCORRECT CHARACTER FOUND IN CMD at place",elementIndex
                
            else:    
                if listToDo[elementIndex] == 'W':
                
                    if elementIndex > len(listToDo) - 3:
                        correctCMD = False
                        print "CMD ERROR #2: W at place",elementIndex,"without enough arguments"
                    
                    elif (not(listToDo[elementIndex+1].isdigit())) or (not(listToDo[elementIndex+2].isdigit())):
                        correctCMD = False
                        print "CMD ERROR #2: W at place",elementIndex,"without enough arguments"

		    elif not(int(listToDo[elementIndex+2])<100):
			correctCMD = False
                        print "CMD ERROR #6: W at place",elementIndex,"with index argument too big (>99)"
                    
                    if elementIndex < len(listToDo) - 3:
                        if listToDo[elementIndex+3].isdigit():
                            correctCMD = False
                            print "CMD ERROR #3: W at place",elementIndex,"with too many arguments"

                if listToDo[elementIndex] == 'R':

                    if elementIndex > len(listToDo) - 2:
                        correctCMD = False
                        print "CMD ERROR #4: R at place",elementIndex,"without enough arguments"
                    
                    elif not(listToDo[elementIndex+1].isdigit()):
                        correctCMD = False
                        print "CMD ERROR #4: R at place",elementIndex,"without enough arguments"

		    elif not(int(listToDo[elementIndex+1])<100):
			correctCMD = False
                        print "CMD ERROR #7: R at place",elementIndex,"with index argument too big (>99)"
                    
                    if elementIndex < len(listToDo) - 2:
                        if listToDo[elementIndex+2].isdigit():
                            correctCMD = False
                            print "CMD ERROR #5: R at place",elementIndex,"with too many arguments"

            elementIndex += 1

            
        if correctCMD:
            elementIndex = 0
            while elementIndex < len(listToDo):
                if listToDo[elementIndex] == 'R':       #read

                    
                    i = int(listToDo[elementIndex+1])

                    if i in L1Addr:                         #cache hit
                        cacheHits += 1
                        k = L1Addr.index(i)
                        v = L1Data[k]
        
                    else:                                   #cache miss
                        cacheMiss += 1
                        v = M[i]
                        k = LastUse.index(min(LastUse))         #victime
                        if L1Dirt[k]:                           #si non actuel, écrire en mémoire
                            M[L1Addr[k]] = L1Data[k]
                        L1Addr[k] = i
                        L1Data[k] = v
                        L1Dirt[k] = False
        
                    LastUse[k] = genCounter
                    genCounter += 1
                    elementIndex += 2
		    print "The value in addres",i,"is",v

                    
                elif listToDo[elementIndex] == 'W':     #write


                    v,i =int(listToDo[elementIndex+1]),int(listToDo[elementIndex+2])
                    
                    if i in L1Addr:                         #cache hit
                        cacheHits += 1
                        k = L1Addr.index(i)
                        L1Data[k] = v
                        L1Dirt[k] = True
        
                    else:                                   #cache miss
                        cacheMiss += 1
                        M[i] = v
                        k = LastUse.index(min(LastUse))         #victime
                        if L1Dirt[k]:                           #si non actuel, écrire en mémoire
                            M[L1Addr[k]] = L1Data[k]
                        L1Addr[k] = i
                        L1Data[k] = v
                        L1Dirt[k] = False
        
                    LastUse[k] = genCounter
                    genCounter += 1                    
                    elementIndex += 3

	raw_input("PRESS RETURN")
	system('clear')

    elif cmd == '3':
	print "SEE YOU LATER"
        end = True
            
