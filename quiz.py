print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2022')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de Black Clover Quiz 2022 beginnen!!\nGeef bij iedere vraag een duidelijk antwoord.\n\n')

    antwoord=input('Vraag 1: Wie is de protagonist? \n A. Asta \n B. Yuno \n C. Nizar \n')
    if antwoord.lower()=='a':
        punten += 1
        def my_function(a, b, c):
            print("goed, het antwoord is inderdaad " + a + ".")
        my_function(a = "Asta", b = "Yuno", c = "Nizar")
    else:
        print("fout!")
    
    antwoord=input('Vraag 2: Wie is de antagonist? ')
    if antwoord.lower()=='licht' or antwoord.lower()=='lucius' or antwoord.lower()=='lucifero':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 3: Wie is de vice kapitein van de Black Bulls? ')
    if antwoord.lower()=='nacht':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 4: Wie is de vice kapitein van de Golden Dawn?  ')
    if antwoord.lower()=='yuno':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 5: Waar of niet waar: Julius is de koning. \nWaar \nNiet waar\n')
    if antwoord.lower()=='niet waar' or antwoord.lower()=='niet':
        punten += 1
        def my_function(a, b):
            print("goed, het is inderdaad " + b + ". Julius is de tovenaar koning.")
        my_function(a = "waar", b = "niet waar")
    else:
        print("fout!")        

    antwoord=input('Vraag 6: Wie is de oudste dark triad? ')
    if antwoord.lower()=='dante' or antwoord.lower()=='danté':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 7: Wie is de sterkste duivel? ')
    if antwoord.lower()=='lucius' or antwoord.lower()=='lucifero':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 8: Wat zijn Julius zijn krachten?  ')
    if antwoord.lower()=='tijd' or antwoord.lower()=='zwaartekracht':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 9: Waar komen Asta & Yuno vandaan? ')
    if antwoord.lower()=='hage' or antwoord.lower()=='boonies':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 10: Welke spirit is in Yuno zijn bezit? \n A. Salamander \n B. Sylph \n C. Undine \n')
    if antwoord.lower()=='b':
        punten += 1
        def my_function(a, b, c):
            print("goed, het antwoord is inderdaad " + b + ".")
        my_function(a = "Salamander", b = "Sylph", c = "Undine")

    else:
        print("fout!")

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')


#print
#input
#/n
#aantal_vragen=3 (voorbeeld)
#if/elif/else in die volgorde
#int()/float()/str()
#round()
#lower()
#exp1 or exp2

#def is_valide_studentnaam(studentnaam):
#    namen = ['stijn','prosper','mohamed','max','charlotte','thijs','julian','rowan','nizar','cas','quinten','sean','sander','thomas','jason','johan','ryan','danny','jeffrey','romano','daan','nick','michael','tygo']
#    for naam in namen:
#        if naam==studentnaam.lower(): 
#            return True
#    return False