#Programmet get en specifik lista med olika konverterare från SI-enheter till amerikanska dumheter (imperial units) som man kan välja och räkna ut på.

print("Välkommen till Konventeraren! ")



while True: 

    print("Välj en av följande konverteringar med representerade siffra:\n1. Grader Celsius till grader Farenheit\n2. Meter till amerikanska feet\n3. Kilogram till pounds\n4. Avsluta program")

    try:

        konverteringstyp = int(input("Vad väljer du? ",))


        if konverteringstyp == 1:
            celsius = float(input("Hur många grader Celsius är det?: "))

            c_till_f = (1.8 * (celsius) + 32)

            print(str(celsius) + " grader Celsius är " + str(round(c_till_f, 2)) + " Farenheit")
            

        elif konverteringstyp == 2:
            meter = float(input("Hur många meter är det?: "))

            m_till_mile = (meter * 3.28)

            print(str(meter) + " m är " + str(round(m_till_mile, 2)) + " feet")
            

        elif konverteringstyp == 3:
            kg = float(input("Hur många kg är det?: "))

            kg_till_lbs = (kg * 2.2046)

            print(str(kg) + " kg är " + str(round(kg_till_lbs, 2)) + " pounds")
            
        
        elif konverteringstyp == 4:
            print("Programmet har avslutat! ")
            break
        

        else:
            print("Du kan endast välja mellan 1, 2, 3 och 4")
    
    except ValueError:
        print("Du kan endast skriva med siffror! ")


