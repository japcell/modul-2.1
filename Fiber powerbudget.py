while True:
    sikkerhedsmargin = 3
    repartioner = 0.5

    output_power = float(input("Hvad er output power?")) # output power fra senderen
    recieve_sensitivity = float(input("Hvad er recieve sensitivity?")) # Recieve sensitivty på modtageren
    diff = output_power - recieve_sensitivity

    print() #mellemrum
    print("powerbudgettet er:",diff) # printer teksten "powerbudgettet er:" og derefter powerbudgettet i alt.

    if diff > 0:
        print("powerbudgettet er i orden.")
    elif diff == 0:
        print("powerbudgettet kan ikke være nul.")
        break
    else:
        print("powerbudgettet kan ikke være et minustal.")
        break

    print()

    konnekteringer = int(input("Antal konnekteringer?")) #Input for antal konnekteringer
    konnekteringer_ialt = konnekteringer * 0.5 #Antal konnekteringer ganget med 0.5

    splisninger = int(input("Antal splisninger?")) #Input for antal splisninger
    splisninger_ialt = splisninger * 0.1 #Antal splisninger ganget med 0.1

    kilometer = float(input("angiv længde i kilometer?")) #kilometer som input

    menunr = int(input("Vælg imellem 1310 eller 1550:")) #menunr som input

    if menunr == 1310:
        fiber1 = (diff-((0.35*kilometer)-(konnekteringer_ialt+splisninger_ialt+sikkerhedsmargin+repartioner)))
        final1310 = fiber1 - diff
        print(final1310)
        if final1310 >= 0:
            #Printer alle informationer ud som en liste for 1310
            print()
            print(konnekteringer,"konnekteringer =",konnekteringer_ialt,"dB")
            print(splisninger,"splisninger =",splisninger_ialt,"dB")
            print("Længde i km =",kilometer,"* 0.35 =",round((kilometer*0.2)),"dB")
            print("sikkerhedsmargin =", sikkerhedsmargin,"dB")
            print("repartioner =",repartioner,"dB")
            print("Netto overskud er",round((final1310),2),"dB")

            #Printer informationer ud i filer i samme directory 1310
            file = open("1310_kopi.txt", "w")
            file.write("Fiber powerbudget\n")
            file.write('{0} {1} {2} {3}\n'.format(konnekteringer,"konnekteringer =",konnekteringer_ialt,"dB"))
            file.write('{0} {1} {2} {3}\n'.format(splisninger,"splisninger =",splisninger_ialt,"dB"))
            file.write('{0} {1} {2}\n'.format("dB for Længde/km =",round((kilometer*0.2)),"dB"))
            file.write('{0} {1} {2}\n'.format("Sikkerhedsmargin =", sikkerhedsmargin,"dB"))
            file.write('{0} {1} {2}\n'.format("Repartioner =", repartioner,"dB"))
            file.write('{0} {1} {2}\n'.format("Netto overskud er",round((final1310),2),"dB"))
            file.close()
            break
        else:
            print("Netto overskuddet er i minus =",final1310)
            print("Prøv igen")

    elif menunr == 1550:
        fiber2 = (diff-((0.2*kilometer)-(konnekteringer_ialt+splisninger_ialt+sikkerhedsmargin+repartioner)))
        final1550 = fiber2 - diff
        if final1550 >= 0:
            #Printer alle informationer ud som en liste for 1550
            print()
            print(konnekteringer,"konnekteringer =",konnekteringer_ialt,"dB")
            print(splisninger,"splisninger =",splisninger_ialt,"dB")
            print("dB for Længde/km =",round((kilometer*0.2)),"dB")
            print("Sikkerhedsmargin =", sikkerhedsmargin,"dB")
            print("Repartioner =", repartioner,"dB")
            print("Netto overskud er",round((final1550),2),"dB")

            #Printer informationer ud i filer i samme directory 1550
            file = open("1550_kopi.txt", "w")
            file.write("Fiber powerbudget\n")
            file.write('{0} {1} {2} {3}\n'.format(konnekteringer,"konnekteringer =",konnekteringer_ialt,"dB"))
            file.write('{0} {1} {2} {3}\n'.format(splisninger,"splisninger =",splisninger_ialt,"dB"))
            file.write('{0} {1} {2}\n'.format("dB for Længde/km =",round((kilometer*0.2)),"dB"))
            file.write('{0} {1} {2}\n'.format("Sikkerhedsmargin =", sikkerhedsmargin,"dB"))
            file.write('{0} {1} {2}\n'.format("Repartioner =", repartioner,"dB"))
            file.write('{0} {1} {2}\n'.format("Netto overskud er",round((final1550),2),"dB"))
            file.close()
            break
        else:
            print("Netto overskuddet er i minus =",final1550)
            print("Prøv igen")
    else:
        print("Noget gik galt")
