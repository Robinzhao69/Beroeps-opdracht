import time, os, sys


os.system("cls")
#dit is een text-based game waarbij je meerdere keuzes hebt.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je blijft op straat leven.
def straatleven(): 
     os.system("cls")
     message = "Je gaat toch niet stelen. \nJe voor nu op straat leven, maar misschien gebeurd er iets onverwachts."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat de gevangenis in.
def gevangenis2():
     os.system("cls")
     message = "Je wordt naar de gevangenis gebracht. \nJe zal daar nu 20 jaar van je leven in blijven."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat stelen.
def gevangenis1():
     os.system("cls")
     print("Je hebt iets gevonden om te stelen. iemand ziet dat je iets steelt. \nDe politie is gebeld. \nDe politie probeert je aan te houden. Jij probeert er tegen in te gaan. ")
     gevangenis1 = input("\nWat ga je doen \n-------------------------------------------- \nA.agressiever zijn \nB.niks doen \nantwoord: ")
     if gevangenis1.lower() == "a":
          print("Je wordt neergehaald en krijgt een stoot.")
          gevangenis2()
     else:
          print("Je wordt neergehaald.")
          gevangenis2()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat stelen
def stelen():
     os.system("cls")
     print("Je leeft nu al een tijdje op straat. \nJe denkt er aan om te gaan stelen, omdat je honger hebt. ")
     stelen = input("\nWat ga je doen?  \n-------------------------------------------- \nA.Je gaat stelen \nB.Je doet niks \n antwoord: ")
     if stelen.lower() == "a":
          print("Je probeert nu te stelen.")
          gevangenis1()
     else:
          print("Je gaat toch niet stelen.")
          straatleven()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je bent onslagen.
def ontslagen():
     os.system("cls")
     print("Je werkt slecht en nu ben je ontslagen. \nJe voel dat het geen zin meer heeft om naar werk te gaan zoeken. \nJe kiest ervoor om op straat te leven.")
     stelen()
     
     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je hebt nu een baan.
def werk2():
     os.system("cls")
     print("Je solliciteert nu bij de hotel. \nJe legt de baas uit wat er allemaal is gebeurd. \nDe baas begrijpt het en houd jou identiteit geheim. \nJe bent aangenomen. \nJe begint nu met je eerste week.")
     werk2 = input("\nJe hebt de keuze om hard te werken of niet. Wat kies je? \n-------------------------------------------- \nA.hard werken \nB.slecht je werk doen \nantwoord: ")
     if werk2.lower() == "a": 
          message = "Je werkt hard. \nJe wordt nu beloond met een hoger loon. \nJe werkt nu al een tijdje bij de hotel en de baas heeft je geholpen om legaal in Turkije te blijven. \nJe leeft nu een gezond en veilig leven in Turkije. \nJe hebt het werken in turkije einde bereikt."
          for char in message:
               sys.stdout.write(char)
               sys.stdout.flush()
               time.sleep(0.07)
     else: 
          print("Je werkt slecht.")
          ontslagen()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je zoekt werk.
def werk1():
     os.system("cls")
     print("Je zit nu als uren te zoeken naar een baantje. \nNa een tijdje zoeken heb je eindelijk iets gevonden. \nje ziet dat er is een hotel dat personeel zoekt.")
     werk1 = input("\nWat ga je doen? \n-------------------------------------------- \nA.Naar binnen lopen \nB.door zoeken \nantwoord: ")
     if werk1.lower() == "a":
          print("Je gaat solliciteren bij de hotel.")
          werk2()
     else: 
          print("Je gaat door zoeken naar werk.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je bent in Turkije aangekomen. 
def turkije1():
     os.system("cls")
     print("Je blijft in Turkije. \nJe hebt geen geld op zak. \nJe denkt nu aan twee dingen, dat zijn werk zoeken of op straat leven.")
     turkije1 = input("\nWat kies jij om te doen? \n-------------------------------------------- \nA.werk zoeken \nB.op straat leven \nantwoord: ") 
     if turkije1.lower() == "a": 
          print("Je gaat werk zoeken.")
          werk1()
     else: 
          print("Je gaat op straat leven.")
          stelen()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat naar het azielzoekerscentrum.
def nederland5():
     os.system

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je bent in Nederland
def nederland4():
     os.system("cls")
     message = "Je bent eindelijk in Nederland. \nJe moet naar een azielzoekerscentrum om een verblijfsvergunning te krijgen. \nJe wordt er nu naar toe gebracht."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)

     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat reizen naar Nederland.
def nederland3():
     os.system("cls")
     print("Je zit nu al een tijdje te reizen. \nJe hebt heel veel honger.")
     nederland3 = input("\nWat ga je doen? \n-------------------------------------------- \nA.vragen of iemand wat eten heeft \nB.niks doen \nantwoord: ")
     if nederland3.lower() == "a":
          print("Iemand heeft wat te eten voor je. Je bedankt die gene en eet.")
     else:
          print("Je hebt heel veel honger.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat naar de meeting point.
def nederland2():
     os.system("cls")
     print("Achmed brengt je naar de pit stop. \nJullie zijn aan gekomen bij de meeting point. \nAchmed regelt alles voor je en vertelt om wat eten te gaan halen. ")
     nederland2 = input("\nWat ga je doen \n-------------------------------------------- \nA.eten halen \nB.niks halen \nantwoord: ")
     if nederland2.lower() == "a":
          print("Je gaat eten halen.")
          nederland3()
     else:
          print("Je haalt niks. Je hebt honger.")
          nederland3()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Op naar Nederland.
def nederland1():
     os.system("cls")
     message = "Je vraagt aan je vriend of hij naar Nederland gaat. \nHij zegt: 'nee' \nAchmed verwijst je wel naar iemand die wel naar Nederland gaat, maar de reis duurt heel lang. \nJe vriend Achmed brengt je wel naar hem toe, sinds ze toch naar de zelfde plek moeten om een pit stop te maken"
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je bent in Turkije aangekomen. Hier ga een keuze maken van wat je verder wilt gaan doen.
def vluchten4():
     os.system("cls")
     print("Na een hele moeizame reis ben je eindelijk in Turkije. \nJe bent wel illegaal in Turkije zo je moet wel uitkijken. \nNou sinds je nu toch in turkije bent, start vanaf hier een nieuw verhaal. \nJe zit te twijfelen of je in Turkije wilt blijven of naar Nederland wilt door vluchten.")
     vluchten4 = input("\nWat ga je kiezen? \n-------------------------------------------- \nA.in Turkije blijven \nB.naar Nederland gaan \nantwoord: ")
     if vluchten4.lower() == "a":
          print("Je blijft in Turkije.")
          turkije1()
     else:
          print("Je gaat naar Nederland.") 
          nederland1()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#hier probeer je je spuug in te houden
def subvluchten1():
     os.system("cls")
     print("Je zit nu al 3 uur in de truck. Onderweg naar Turkije. \nJe begint een beetje misselijk te voelen. ")
     subvluchten1 = input("\nWat ga je doen? \n-------------------------------------------- \nA.proberen in te houden \nB.spugen \nantwoord: ")
     if subvluchten1.lower() == "a":
          print("Je spuugt nog steeds. \nDe truck stinkt nu heel erg en de vluchteling moeten ook spugen van de stank.")
          vluchten4()
     else:
          print("Je spuugt. \nDe truck stinkt nu heel erg en de vluchteling moeten ook spugen van de stank.")
          vluchten4()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Achmed had je een pil gegeven en nou voel je je wat beter.
def vluchten3():
     os.system("cls")
     print("Je zit nu al een tijdje in de truck. \nOok al zit je niet comfortabel, dankzij die pil dat Achmed je had gegeven voel je je niet misselijk. \nJe hebt na een tijdje reizen honger. \nJe hebt een mueslireep in jou broekzak. \nEr zit een kind naast je en wilt ook graag een stukje. ")
     vluchten3 = input("Wat ga je doen ? \n-------------------------------------------- \nA.een stukje geven \nB.niks geven \nantwoord: ")
     if vluchten3.lower() == "a":
          print("Je geeft een stukje van je mueslireep.")
          vluchten4()
     else:
          print("Je geeft niks. \nDat kind haat je nu.")
          vluchten4()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
#hier ga je achmed vragen voor een pil of je blijft stil. dit heeft invloed op de reis.
def vluchten2():
     os.system("cls")
     print("Je hebt met je vriend Achmed af gesproken om te verzamelen bij Mosul en in de nacht te gaan vertrekken. \nNa een tijdje liften met een taxi ben je er eindelijk. ")
     vluchten2 = input("\nJe bent een beetje wagenziek. \n-------------------------------------------- \nA.zeg niks \nB.informeer Achmed \nantwoord:")
     if vluchten2.lower() == "a":
          print("Je blijft still en zeg niks. \nJe stapt nu de truck in met meerdere vluchtelingen.")
          subvluchten1()
     else:
          print("Achmed is aardig en geeft je een pil. \nJe stapt nu de truck in met meerdere vluchtelingen.")
          vluchten3()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat naar het slagveld.
def oorlog3():
     os.system("cls")
     message = "Je zit nu in een gepanserde auto met je ploeggenoten. \nJullie worden bekogeld door het Iraanse leger. \nZE schieten drie raketen op jullie af. \nDe bestuurder is dood... \njullie stapen de auto uit en vuren terug."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "Het heeft weinig effect. "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "Je merkt dat je ploeggenoten gewond zijn geraakt. \nJe jullie besluiten om terug te gaan trekken. \nJullie rollen terug, zodat het moeilijker is om geraakt te worden. \nTijdens het rollen heb je een kogel ontvangen in de maag. \nJe bloed heel veel... \nJe weet dat je het niet meer gaat halen, dus je geeft op en ligt stil op de grond... "


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je vermoord de leider.
def executie2():
     os.system("cls")
     message = "Iedereen in de zaal schrikt. \nJij probeert nog wat terroristen mee te nemen voordat je dood gaat. \nHet lukt je om nog 3 terroristen dood te schieten, maar je overal in de zaal..."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "BRRR, BRRR ,BRRR..."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#De leider gaat een toespraak houden.
def oorlog2():
     os.system("cls")
     print("Je zit nu in de zaal. \nDe leider staat daar voorbereid om zijn toespraak te houden. \nDe toespraak ging alleen maar over het plan van aanpak. \nJe wilt natuurlijk het liefst geen mensen dood maken. \nJe er nu over na te denken om de leider on-spot dood te schieten. ")
     oorlog2 = input("\nWat ga je doen? \n-------------------------------------------- \nA.Je wapen pakken en de leider schieten \nB.niks doen \nantwoord: ")
     if oorlog2.lower() == "a":
          print("Je pakt je wapen en schiet.")
          executie2()
     else:
          print("Je doet niks en gaat ten oorlog met de wereld.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat oorlog voeren
def oorlog1():
     os.system("cls")
     message = "Je hebt jezelf nu officieel aangesloten bij ISIS. \nDe leider vertel aan iedereen om morgen s' ochtends in de zaal te gaan verzamelen. \nHij heeft een toe spraak. "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "21 oktober 2020..."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     oorlog2()
     

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je wordt geexecuteert
def executie(): 
     os.system("cls")
     message = "De leider is boos. \nHij schreeuwt tegen zijn man om jou op te pakken en naar de kelder te gaan. "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "Paar minuten later... "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "Jullie zitten nu in de kelder. \nDe mannen houden je vast op de grond. \nDe leider pakt zijn wapen en richt vervolgens op jou."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     message = "Even later..."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(0.5)
     os.system("cls")
     message = "BENG, BENG!"
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je gaat nu de basis ban ISIS
def accept2():
     os.system("cls")
     message = "5 uur later..."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     os.system("cls")
     print("Jullie zijn aangekomen bij de basis. \nDaar ontmoet je de een van de leiders van ISIS. \nDe leider zegt: 'Voordat je bij ons kan aansluiten moet je eerst loyaliteit aan ons tonen' ")
     accept2 = input("\nWat ga je doen? \n-------------------------------------------- \nA.zweer dat je voor altijd loyaal blijft. \nB.spuug tegen hem aan \nantwoord: ")
     if accept2.lower() == "a":
          print()
          oorlog1()
     else:
          print("De leider is niet blij.")
          executie()

     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je accepteert het aanbod
def accept1():
     os.system("cls")
     message = "Vlak nadat jij het aanbod had geaccepteerd, vertelt hij je om met hem mee te gaan. \nJullie stappen in de auto en rijden vervolgens, naar de basis van ISIS."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     accept2()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je weigerd het aanbod.
def vriend3():
     os.system("cls")
     message = "Je vriend is heel erg teleurgesteld in je. Hij check eerst of zijn wapen het doet en richt vervolgens zijn wapen op je. \nPaar secondes later... "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
     message = "BANG!"
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Je kiest of je het aanbod accepteert of weigerd
def vriend2():
     os.system("cls")
     print("Je vriend is heel erg teleurgesteld in je. \nHij zucht en pakt vervolgens iets uit zijn tas. \nHet is een pistool! \nHij geeft je nog een kans.")
     vriend2 = input("\nWat ga je doen? \n-------------------------------------------- \nA.het aanbod toch accepteren \nB.toch weigeren \nantwoord: ")
     if vriend2.lower() == "a":
          print("Je accepteert het aanbod.")
     else:
          print("Je vriend richt zijn pistool op je.")
          vriend3()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
#Je vriend is er.
def vriend1():
     os.system("cls")
     print("Je vriend staat voor de deur. \nJe doet de deur voor hem open. \nJe vertelt hem om plaats te nemen en bied hem wat thee aan. \nJe vriend komt ineens met iets onverwachts. \nHij vertelt je dat hij zich bij ISIS heeft aangesloten. \nHij vraagt nu aan jou of je ook bij ISIS wilt aan sluiten. ")
     vriend1 = input("\nWat ga je doen. \n-------------------------------------------- \nA.het aanbod afwijzen \nB.aanbod accepteren \nantwoord: ")
     if vriend1.lower() == "a":
          print("Je vriend is teleurgesteld.")
          vriend2()
     else:
          print("Je accepteert het aanbod.")
          accept1()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
#Je vriend komt naar je toe
def  blijf2():
     os.system("cls")
     print("Het is vandaag de dag dat je vriend langskomt. \nJe bent net wakker. \nJe gaat tandenpoetsen. \nNa het tandenpoetsen ga je ontbijten, maar je hebt niet echt honger. ")
     blijf2 = input("\nWat ga je doen. \n-------------------------------------------- \nA.ontbijten \nB.niet ontbijten. \nantwoord: ")
     if blijf2.lower() == "a":
          print("Je gaat een broodje eten.")
          vriend1()
     else:
          print("Je eet geen ontbijt.")
          vriend1()



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
#hier kies je ervoor om thuis te blijven.
def  blijf1():
     os.system("cls")
     message = "je hebt ervoor gekozen om thuis te blijven. Je belt vervolgens je vriend, om te vertellen dat je niet gaat vluchten. \nJe vriend zegt vervolgens tegen je, dat hij morgen naar je toe zou komen."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)    
     blijf2()
         

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#hier probeer je Achmed over te halen, als dat niet lukt dan moet je blijven in Iran.
def vluchten1():
     os.system("cls")
     print("Oke het is vandaag de dag om te vertrekken. \nJe belt je vriend Achmed die werkt in het transport. \nJe vraagt hem of je met hem mee kan gaan, maar hij zegt nee.")
     vluchten1 = input("\nWat ga je doen? \n-------------------------------------------- \nA.door smeken \nB.het accepteren \nantwoord: ")
     if vluchten1.lower() == "a":
          print("Na een tijdje smeken, komt je vriend toch op de conclusie om je mee te nemen.")
          vluchten2()
     else:
          print("Vluchten kan niet meer, omdat je geen vervoer hebt. \nJe blijft nu thuis.")
          blijf1()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#hier start het verhaal
def begin():
     naam = input("Hallo wie ben jij? ")
     message = "Hallo " + naam + "."
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     message = "\nOke Je woont al 20 jaar in Iran.\nJe ziet op het nieuws dat de terroristische organisatie ISIS weer naar boven komt in jouw land.\nJe zit nu te twijfelen of je zou vluchten of blijven. "
     for char in message:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.07)
     time.sleep(2)
                               
     begin = input("\nWat ga je doen? \n-------------------------------------------- \nA.vluchten \nB.blijven \nantwoord: ")
     if begin.lower() == "a":
          print("Je pakt je benodigde spullen in en je bent bereid om morgen te vertrekken.")
          vluchten1()
     else: 
          print("je hebt ervoor gekozen om thuis te blijven. Je belt vervolgens je vriend, om te vertellen dat je niet gaat vluchten")
          blijf1()

begin()

