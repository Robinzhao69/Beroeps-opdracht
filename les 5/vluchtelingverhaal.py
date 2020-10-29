
naam = input("Hallo wie ben jij ")
print("Hallo " + naam)
print("Oke " + naam + " Je woont al 20 jaar in Iran.")
print("Je ziet op het nieuws dat de terroristische organizatie ISIS weer naar boven komt in jou land.")
print("Je zit nu te twijfelen of je zou vluchten of blijven.")

print("-------------------------------------------------------------------------------------------------------------------------")
keuze1 = input("Wat ga je doen? \nA.vluchten \nB.blijven \nantwoord: ")
if keuze1 == "a" or keuze1 == "A":
    print("\n")
    print("Je pakt je benodigde spullen in en je bent bereid om morgen te vertrekken.")
    print("\n")

    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Oke het is vandaag de dag om te vertrekken.")
    print("Je belt je vriend Achmed die werkt in de transport")
    print("Je vraagt hem of je met hem mee kan gaan, maar hij zegt nee.")

    print("--------------------------------------------------------------------------------------------------------------------------")
    vluchten1 = input("Wat ga je doen? \nA.door smeken \nB.het accepteren \nantwoord: ")
    if vluchten1 == "a" or vluchten1 == "A":
        print("\n")
        print("Na een tijdje smeken, komt je vriend toch op de conclusie om je mee te nemen.")
        print("\n")

        print("Je hebt met je vriend af gesproken om te verzamelen bij Mosul en in de nacht te gaan vertrekken.")
        print("Na een tijdje liften met een taxi ben je er eindelijk")
        
        print("--------------------------------------------------------------------------------------------------------------------------")
        vluchten2 = input("Je bent een beetje wagenziek. \nA.zeg niks  \nB.informeer Achmed    \nantwoord: ")
        if vluchten2 == "a" or vluchten2 == "A":
            print("\n")
            print("Je blijft still en zeg niks.")
            print("Je stapt nu de truck in met meerdere vluchtelingen.")
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------------------")
            
            print("Je zit nu al 3 uur in de truck. Onderweg naar Turkije.")
            print("Je begint een beetje misselijk te voelen.")
            subvluchten1 = input("Wat ga je doen? \nA.proberen in te houden \nB.spugen \nantwoord: ")
            if subvluchten1 == "a" or subvluchten1 == "A" or subvluchten1 == "b" or subvluchten1 == "B":
                print("\n")
                print("Je spuugt.")
                print("\n")
                print("--------------------------------------------------------------------------------------------------------------------------")

                print("de truck stinkt nu heel erg en de vluchteling moeten ook spugen van de stank")
                print("Na een hele moeizame reis ben je eindelijk in Turkije.")
                print("Je bent wel illegaal in Turkije zo je moet wel uitkijken.")
                print("Nou sinds je nu toch in turkije bent, start vanaf hier een nieuw verhaal.")
                print("Je zit te twijfelen of je in Turkije wilt blijven of naar Nederland wilt door vluchten.")

                print("--------------------------------------------------------------------------------------------------------------------------")
                keuze2 = input("wat ga je kiezen? \nA.in Turkije blijven  \nB.naar Nederland gaan  \nantwoord: ")
                if keuze2 == "a" or keuze2 == "A":
                    print("\n")
                    print("Je blijft in Turkije.")
                    print("\n")
                    print("--------------------------------------------------------------------------------------------------------------------------")

                    print("Je blijft in Turkije.")
                    print("Je hebt geen geld bij je.")
                    print("Je denkt aan twee dingen, dat zijn werk zoeken of op straat leven.")
                    print("--------------------------------------------------------------------------------------------------------------------------")
                    turkije1 = input("Wat kies jij om te doen? \nA.werk zoeken \nB.op straat leven \nantwoord: ")
                    if turkije1 == "a" or turkije1 == "A":
                        print("\n")
                        print("Je gaat werk zoeken.")
                        print("\n")
                        print("--------------------------------------------------------------------------------------------------------------------------")

                        print("na een tijdje zoeken heb je eindelijk iets gevonden.")
                        print("Er is een hotel dat personeel zoekt.")
                        print("--------------------------------------------------------------------------------------------------------------------------")
                        werk1 = input("Wat ga je doen? \nA.Naar binnen lopen \nB.door zoeken \nantwoord: ")
                        if werk1 == "a" or werk1 == "A":
                            print("\n")
                            print("Je gaat solliciteren bij de hotel.")
                            print("\n")
                            print("--------------------------------------------------------------------------------------------------------------------------")

                            print("je solliciteert nu bij de hotel.")
                            print("Je legt de baas uit wat er allemaal is gebeurd.")
                            print("De baas begrijpt het en houd jou idedentiteit geheim")
                            print("je bent aan genomen")
                            print("je begint nu met je eerste week")
                            print("--------------------------------------------------------------------------------------------------------------------------")
                            werk2 = input("Je hebt de keuze om hard te werken of niet. Wat kies je? \nA.hard werken  \nB.slecht je werk doen  \nantwoord: ")
                            if werk2 == "a" or werk2 == "A":
                                print("\n")
                                print("Je werkt hard.")
                                print("\n")
                                print("--------------------------------------------------------------------------------------------------------------------------")

                                print("Je wordt nu beloond met een hoger loon.")
                                print("Je werkt nu al een tijdje bij de hotel en de baas heeft je geholpen om legaal in Turkije te blijven.")
                                print("Je leeft nu een gezond en veilig leven in Turkije")
                            else:
                                print("\n")
                                print("Je werkt slecht en wordt ontslagen.")
                                print("\n")
                                print("--------------------------------------------------------------------------------------------------------------------------")
                                ontslagen1 = input("Wat ga je nu doen \nA.verder zoeken \nB.op straat leven \nantwoord: ")
                                if ontslagen1 == "a" or ontslagen1 == "A":
                                    print("\n")
                                    print("Je gaat verder zoeken naar werk.")
                                    print("\n")
                                    print("--------------------------------------------------------------------------------------------------------------------------")
                                    
                                    print("Je zoekt al een lange tijd, maar hebt nogsteeds geen werk gevonden.")
                                    print("Je geeft op.")
                                    print("Je denkt eraan om naar Nederland te gaan")
                                    
                                    print("--------------------------------------------------------------------------------------------------------------------------")
                                    keuze3 = input("Wat ga je doen \nA.Naar Nederland \nB.hier op straat leven \nantwoord: ")
                                    if keuze3 == "a" or keuze3 == "A":
                                        print("\n")
                                        print("Je maakt een plan om naar Nederland te gaan.")
                                        print("\n")
                                    else:
                                        print("\n")
                                        print("Je leeft nu op straat in Turkije.")
                                        print("\n")
                                        print("--------------------------------------------------------------------------------------------------------------------------")

                                        print("Je woont al een tijdje op straat in Turkije.")
                                        print("je denkt eraan om te gaan stelen.")
                                        print("--------------------------------------------------------------------------------------------------------------------------")
                                        stelen1 = input("Wat ga je doen \nA.stelen \nB.niet stelen \nantwoord: ")
                                        if stelen1 == "a" or stelen1 == "A":
                                            print("\n")
                                            print("Je gaat nu proberen te stelen.")
                                            print("\n")
                                            print("--------------------------------------------------------------------------------------------------------------------------")

                                            print("Je hebt iets gevonden om te stelen. iemand ziet dat je iets steelt.")
                                            print("De politie is gebeld.")
                                            print("De politie probeert je aan te houden. Jij probeert er tegen in te gaan.")
                                            print("--------------------------------------------------------------------------------------------------------------------------")
                                            gevangenis1 = input("Wat ga je doen \nA.agressiever zijn \nB.niks doen \nantwoord: ")
                                            if gevangenis1 == "a" or gevangenis1 == "A" or gevangenis1 == "b" or gevangenis1 == "B":
                                                print("\n")
                                                print("Je wordt neergehaald en opgepakt.")
                                                print("\n")
                                                print("--------------------------------------------------------------------------------------------------------------------------")

                                                print("Je wordt naar de gevangenis gebracht. Je zal daar nu 20 jaar van je leven in blijven.")
                                            
                                           
                                        else:
                                            print("\n")
                                            print("Je gaat niet stelen.")
                                            print("\n")
                                            print("--------------------------------------------------------------------------------------------------------------------------")

                                            print("Je leeft nu heel je leven dakloos op straat.")

                                else:
                                    print("\n")
                                    print("Je gaat nu op straat leven.")
                                    print("\n")
                                    print("--------------------------------------------------------------------------------------------------------------------------")

                        else:
                            print("\n")
                            print("Je gaat door zoeken naar werk.")
                            print("\n")

                    else:
                        print("\n")
                        print("Je gaat op straat leven.")
                        print("\n")

                   
                else:
                    print("\n")
                    print("Je gaat naar Nederland.")
                    print("\n")

            
        else:
            print("\n")
            print("Achmed is aardig en geeft je een pil.")
            print("Je stapt nu de truck in met meerdere vluchtelingen.")
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------------------")

    else:
        print("\n")
        print("Vluchten kan niet meer, omdat je geen vervoer hebt")
        print("Je blijft nu thuis")
        print("\n")

else:
    print("\n")
    print("je kies ervoor om thuis te blijven. Je belt vervolgens je vriend, om te vertellen dat je niet gaat vluchten")
    print("\n")

    

    
