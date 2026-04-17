# Frågesport spel med olika teman
# Spelaren svarar på frågor och får poäng och ett betyg i slutet

# Vi använder en random Sats och vi valde att ha den i början
import random

# Funktion som ställer en fråga
def fråga_enfråga(fråga, svar):
    användare_svar = input(fråga + " ")
    if användare_svar.lower() == svar.lower():
        print("Rätt svar!")
        return 1
    else:
        print("Fel svar! Rätt svar var:", svar)
        return 0

# Funktion som ger ett betyg baserat på poängen
def ge_betyg(poäng, total):
    if poäng == 5:
        betyg = "A"
    elif poäng == 4:
        betyg = "B"
    elif poäng == 3:
        betyg = "C"
    elif poäng == 2:
        betyg = "D"
    elif poäng == 1:
        betyg = "E"
    else:
        betyg = "F"

    print("Du fick", poäng, "av", total, "poäng.")
    print("Ditt betyg är:", betyg)

# Huvudprogrammet
def fråge_sport():
    print("Välkommen till denna frågesporten!")
    print()
    print("Efter att du har svarat på frågorna kommer du få ett betyg på hur du har preserat")
    print()
    print("Välj tema:")
    print()
    print("1. Geografi")
    print("2. Historia")
    print("3. Sport")
    print("4. Film och TV")
    print("5. Astronomi")
    print("6. Blandade frågor (random från alla kategorier)")
    print()

# Här får en spelare ett val av vilken kategori dem vill svara på
    val = input("Skriv 1,2,3,4,5 eller 6: ")
    print()

    spelarens_poäng = 0
    totala_frågor = 5

    # Här befinner sig alla frågor samt svar.
    geografi_frågor = [
        ("Vad är huvudstaden i Nederländerna?", "Amsterdam"),
        ("Vilket är Sveriges största sjö?", "Vänern"),
        ("Vilken är världens största hav?", "Stilla havet"),
        ("Vilken är världens största kontinent?", "Asien"),
        ("Vilket land i världen har flest öar?", "Sverige"),
    ]

    historia_frågor = [
        ("Vad hette skeppet som sjönk 1912?", "Titanic"),
        ("Vilket år började andra världskriget?", "1939"),
        ("Vilket land styrdes av Napoleon?", "Frankrike"),
        ("Vem va USA:s första president?", "George Washington"),
        ("Vem målade Mona Lisa?", "Leonardo da Vinci"),
    ]
    
    sport_frågor = [
        ("Vad hette laget som överraskande vann Preimer League säsongen 2015/16?", "Leicester"),
        ("Vilket land hållde om sommar OS 2012?", "Storbrittanien"),
        ("Vilken fotbollsspelare har vunnit flest ballon d or (Skriv Efternamn)", "Messi"),
        ("Vad heter boxaren som har ett rekord 50-0 i sin karriär? (Skriv Efternamn)", "Mayweather"),
        ("Vilket land har vunnit ishockey vm flest gånger?", "Kanada"),
    ]
    
    film_frågor = [
        ("Vilken film har dragit in mest pengar på bio?", "Avatar"),
        ("Hur många säsonger blev det av hitt serien Game of Thrones? (Skriv nummer):", "8"),
        ("Leonardo DiCaprio har vunnit en oscar, vad hette filmen där han fick priset?", "The Revenant"),
        ("Enligt IMDB vilken serie har högst rating/betyg?", "Breaking Bad"),
        ("I Sverige har Netflix funnits ett tag men när lanserades de egentligen? (Skriv år)", "2012"),
    ]
    
    astronomi_frågor = [
        ("Vad heter galaxen vi är i?", "Vintergatan"),
        ("Vilken planet är störst i vårt solsystem?", "Jupiter"),
        ("Hur många planeter finns i vårt solsystem?", "8"),
        ("Vilket år gick Neil Armstrong på månen?", "1969"),
        ("Meteoriten som slog ner och utplånade dinosaurierna vilket land slog den ner i?", "Mexiko"),
    ]

    # Välj vilka frågor som ska användas baserat på användarens val
    if val == "1":
        frågor = geografi_frågor
    elif val == "2":
        frågor = historia_frågor
    elif val == "3":
        frågor = sport_frågor
    elif val == "4":
        frågor = film_frågor
    elif val == "5":
        frågor = astronomi_frågor
    elif val == "6":
        
        # Blandade frågor - ta en slumpmässig fråga från varje kategori
        frågor = []
        alla_kategorier = [geografi_frågor, historia_frågor, sport_frågor, film_frågor, astronomi_frågor]
        
        # Välj en slumpmässig fråga från varje kategori
        for kategori in alla_kategorier:
            slump_fråga = random.choice(kategori)
            frågor.append(slump_fråga)
        
        # Blanda ordningen på frågorna så det blir mer varierat
        random.shuffle(frågor)
        print("Du har valt blandade frågor! Här kommer en fråga från varje kategori.")
        print()
    else:
        print("Ogiltigt val, spelet avslutas.")
        return

    # Loopar igenom frågorna
    for q in frågor:
        spelarens_poäng += fråga_enfråga(q[0], q[1])
        print()

    ge_betyg(spelarens_poäng, totala_frågor)

# Start spelet igen
while True:
    fråge_sport()
    
    svar = input("Vill du spela igen? (ja/nej):").lower()
    
    if svar != "ja":
        print("Tack för att du spelade!")
        break
