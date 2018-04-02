import playprompt
import rec
import recognize
import time
import random


def price(pric):
    p = str(pric)
    unity = ""
    dozens = ""
    bool = False
    for c in p:

        if (bool == False and c != '.'):
            unity += c
        elif (bool == True):
            dozens += c
        elif (c == '.'):
            bool = True
    unity += '.wav'
    dozens += '.wav'

    return unity, dozens


price(3.45)


def is_empty(any_structure):
    if any_structure:
       # print('Structure is not empty.')
        return False
    else:
      #  print('Structure is empty.')
        return True
        # DOPISZ I WYMYSL OBSLUGE SLOW PEWNYCH ALE INNYCH


def main():
    photo_check = 1
    ticket_number = 0
    ticket_payment = 0
    ticket_lastprice = 0
    acceptable_prop = 0.57
    minimal_prob = 0.2
    grammatic_yes_no = ['tak', 'nie', 'powtórz']
    grammatic_one_two_three = ['Jeden', 'Dwa', 'Trzy', 'Powtórz']
    grammatic_one_two_three_f_f = ['Jeden', 'Dwa', 'Trzy', 'Cztery', 'Pięć', 'Powtórz']
    grammatic_one = ['Jeden', 'Powtórz', ]

    grammatic_one_two = ['Jeden', 'Dwa', 'Powtórz', ]
    bool_1 = True
    bool_2 = False
    word_recognized = 0

    bool_opcja1 = False;


    while (bool_1):

        if (bool_2 == False):
            playprompt.play_prompt("resources/dzien_dobry.WAV")  # powitanie
        else:
            playprompt.play_prompt("resources/nie rozumiem krocej.WAV")  # powitanie
            bool_2 = False
        rec.rec(2)
        word_recognized = recognize.return_recognized("answer.wav", grammatic_yes_no)
        if ((is_empty(word_recognized)) == False):
            for name in word_recognized:
                if (name.title() == "Tak" and word_recognized[name] >= acceptable_prop):
                    bool_opcja1 = True
                    bool_1 = False

                elif (name.title() == "Nie" and word_recognized[name] >= acceptable_prop):

                    bool_1 = False
                    return
                elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                    bool_1 = True
                elif (word_recognized[name] <= acceptable_prop and word_recognized[name] >= minimal_prob):

                    bool_2 = True
                else:

                    bool_1 = False
                    return

        else:
            return

    bool_2 = False
    bool_opcja1 = False
    bool_opcja2 = False;
    bool_opcja3 = False;

    word_recognized.clear()

    print("wybor rodzaju biletu normalny/ulgowy/rodzinny")
    bool_powrot_1 = True  # zmienna ktora umozliwia zakup nastepnego bieltu

    while (bool_powrot_1):
        bool_1 = True
        while (bool_1):

            if (bool_2 == False):
                playprompt.play_prompt("resources/nor_ulg_rodz_krocej.WAV")  # powitanie
            else:
                playprompt.play_prompt("resources/nie rozumiem krocej.WAV")  # powitanie
                bool_2 = False
            rec.rec(2.5)
            word_recognized = recognize.return_recognized("answer.wav", grammatic_one_two_three)
            if ((is_empty(word_recognized)) == False):
                for name in word_recognized:
                    if (name.title() == "Jeden" and word_recognized[name] >= acceptable_prop):
                        bool_opcja1 = True
                        bool_1 = False

                    elif ((name.title() == "Dwa") and word_recognized[name] >= acceptable_prop):
                        bool_opcja2 = True
                        bool_1 = False

                    elif ((name.title() == "Trzy") and word_recognized[name] >= acceptable_prop):
                        bool_opcja3 = True
                        bool_1 = False

                    elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                        bool_1 = True
                    elif (word_recognized[name] >= minimal_prob):

                        bool_2 = True
                    else:

                        bool_1 = False
                        return
            else:
                if (photo_check == 1):
                    bool_2 = True

                else:
                    bool_1 = False
                    return

        bool_1 = True
        bool_2 = False

        word_recognized.clear()


        if (bool_opcja1 == True or bool_opcja2 == True):
            bool_split1 = True
            while (bool_1):

                if (bool_2 == False and bool_opcja1 == True):
                    playprompt.play_prompt("resources/normalny_ceny_krocej.WAV")
                elif (bool_2 == False and bool_opcja2 == True):
                    playprompt.play_prompt("resources/ulgowe_ceny_krocej.WAV")
                else:
                    playprompt.play_prompt("resources/nie rozumiem krocej.WAV")
                    bool_2 = False
                rec.rec(2.5)
                word_recognized = recognize.return_recognized("answer.wav", grammatic_one_two_three_f_f)
                if ((is_empty(word_recognized)) == False):
                    for name in word_recognized:
                        if (name.title() == "Jeden" and word_recognized[name] >= acceptable_prop):

                            bool_1 = False
                            ticket_number += 1
                            if (bool_2 == False and bool_opcja1 == True):
                                ticket_payment += 2.8
                                ticket_lastprice = 2.8
                            elif (bool_2 == False and bool_opcja2 == True):
                                ticket_payment += 1.4
                                ticket_lastprice = 1.4
                            print("1")
                        elif (name.title() == "Dwa" and word_recognized[name] >= acceptable_prop):
                            bool_1 = False
                            ticket_number += 1
                            if (bool_2 == False and bool_opcja1 == True):
                                ticket_payment += 3.8
                                ticket_lastprice = 3.8
                            elif (bool_2 == False and bool_opcja2 == True):
                                ticket_payment += 1.9
                                ticket_lastprice = 1.9
                            print("2")
                        elif (name.title() == "Trzy" and word_recognized[name] >= acceptable_prop):
                            bool_1 = False
                            ticket_number += 1
                            if (bool_2 == False and bool_opcja1 == True):
                                ticket_payment += 5
                                ticket_lastprice = 5
                            elif (bool_2 == False and bool_opcja2 == True):
                                ticket_payment += 2.5
                                ticket_lastprice = 2.5
                            print("3")
                        elif (name.title() == "Cztery" and word_recognized[name] >= acceptable_prop):
                            bool_1 = False
                            ticket_number += 1
                            if (bool_2 == False and bool_opcja1 == True):
                                ticket_payment += 7
                                ticket_lastprice = 7
                            elif (bool_2 == False and bool_opcja2 == True):
                                ticket_payment += 3
                                ticket_lastprice = 3
                            print("4")
                        elif (name.title() == "Pięć" and word_recognized[name] >= acceptable_prop):
                            bool_1 = False
                            ticket_number += 1
                            if (bool_2 == False and bool_opcja1 == True):
                                ticket_payment += 14
                                ticket_lastprice = 14
                            elif (bool_2 == False and bool_opcja2 == True):
                                ticket_payment += 7.5
                                ticket_lastprice = 7.5

                        elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                            bool_1 = True
                        elif (word_recognized[name] >= minimal_prob):

                            bool_2 = True
                        else:

                            bool_1 = False
                            return

                else:
                    if (photo_check == 1):
                        bool_2 = True

                    else:
                        bool_1 = False
                        return
        elif (bool_opcja3 == True):
            while (bool_1):
                if (bool_2 == False and bool_opcja3 == True):
                    playprompt.play_prompt("resources/cena_rodzinny_krocej.WAV")
                else:
                    playprompt.play_prompt("resources/nie rozumiem krocej.WAV")  # powitanie
                    bool_2 = False
                rec.rec(2.5)
                word_recognized = recognize.return_recognized("answer.wav", grammatic_one)
                if ((is_empty(word_recognized)) == False):
                    for name in word_recognized:
                        if ((name.title() == "Jeden" or name.title() == "1") and word_recognized[
                            name] >= acceptable_prop):
                            bool_1 = False
                            ticket_number += 1
                            ticket_payment += 16
                            ticket_lastprice = 16

                        elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                            bool_1 = True
                        elif (word_recognized[name] >= minimal_prob):

                            bool_2 = True
                        else:

                            bool_1 = False
                            return
                else:
                    if (photo_check == 1):
                        bool_2 = True

                    else:
                        bool_1 = False
                        return


        bool_1 = True
        bool_2 = False
        bool_opcja1 = False
        bool_opcja2 = False
        bool_opcja3 = False

        while (bool_1):

            if (bool_2 == False):
                playprompt.play_prompt("resources/platnosc_usun_kup_krocej.WAV")  # powitanie
            else:
                playprompt.play_prompt("resources/nie rozumiem krocej.WAV")
                bool_2 = False
            rec.rec(2.5)
            word_recognized = recognize.return_recognized("answer.wav", grammatic_one_two_three)
            if ((is_empty(word_recognized)) == False):
                for name in word_recognized:
                    if (name.title() == "Jeden" and word_recognized[name] >= acceptable_prop):
                        if (ticket_number < 2):
                            bool_1 = False
                        else:
                            playprompt.play_prompt("resources/maxbilety.WAV")
                            bool_1 = False
                            bool_powrot_1 = False

                    elif ((name.title() == "Dwa") and word_recognized[name] >= acceptable_prop):
                        bool_1 = False
                        bool_powrot_1 = False

                    elif ((name.title() == "Trzy") and word_recognized[name] >= acceptable_prop):
                        bool_1 = False  # przechodzimy do pytania czy chce kupic nowy bilet po usunieciu
                        bool_opcja3 = True
                        ticket_number -= 1

                    elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                        bool_1 = True
                    elif (word_recognized[name] >= minimal_prob):

                        bool_2 = True
                    else:

                        bool_1 = False
                        return
            else:
                if (photo_check == 1):
                    bool_2 = True

                else:
                    bool_1 = False
                    return


        while (bool_opcja3):

            if (bool_2 == False):
                playprompt.play_prompt("resources/usunieto_bilet_krocej.WAV")
                # powitanie
            else:
                playprompt.play_prompt("resources/nie rozumiem krocej.WAV")
                bool_2 = False  # powitanie
            rec.rec(2.5)
            word_recognized = recognize.return_recognized("answer.wav", grammatic_yes_no)
            if ((is_empty(word_recognized)) == False):
                for name in word_recognized:
                    if (name.title() == "Tak" and word_recognized[name] >= acceptable_prop):
                        ticket_payment = ticket_payment - ticket_lastprice
                        #print(ticket_payment)
                        bool_opcja3 = False
                        print("1")
                    elif ((name.title() == "Nie") and word_recognized[name] >= acceptable_prop):
                        ticket_payment = ticket_payment - ticket_lastprice
                        #print(ticket_payment)
                        if (ticket_number == 0):
                            playprompt.play_prompt("resources/dziekujemy.WAV")
                            return
                        else:
                            bool_powrot_1 = False
                            bool_opcja3 = False

                    elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                        bool_opcja3 = True
                    elif (word_recognized[name] >= minimal_prob):
                        bool_2 = True
                    else:
                        bool_opcja3 = False
                        return
            else:
                if (photo_check == 1):
                    bool_2 = True

                else:
                    bool_1 = False
                    return

    bool_powrot2 = True
    bool_1 = True
    bool_opcja1 = False
    bool_opcja2 = False

    while (bool_powrot2):
        while (bool_1):

            if (bool_2 == False):
                playprompt.play_prompt("resources/platnosc_karta_gotowka_krocej.WAV")  # powitanie
            else:
                playprompt.play_prompt("resources/nie rozumiem krocej.WAV")
                bool_2 = False  # powitanie
            rec.rec(2.5)
            word_recognized = recognize.return_recognized("answer.wav", grammatic_one_two)
            if ((is_empty(word_recognized)) == False):
                for name in word_recognized:
                    if (name.title() == "Jeden" and word_recognized[name] >= acceptable_prop):
                        bool_1 = False
                        bool_opcja1 = True
                        print("1")
                    elif ((name.title() == "Dwa") and word_recognized[name] >= acceptable_prop):
                        bool_1 = False
                        bool_opcja2 = True  # randint(a,b)
                        print("2")
                    elif (name.title() == "Powtórz" and word_recognized[name] >= acceptable_prop):
                        bool_1 = True
                    elif (word_recognized[name] >= minimal_prob):
                        bool_2 = True
                    else:
                        bool_1 = False
                        return
            else:
                if (photo_check == 1):
                    bool_2 = True

                else:
                    bool_1 = False
                    return

        trans_state = 1
        if bool_opcja1 == True:
            # print(ticket_payment)
            unity, dozens = price(ticket_payment)
            # print(unity)

            pathunity = "resources/unity/" + unity
            pathdozens = "resources/dozens/" + dozens
            #print(pathunity)
            #print(pathdozens)
            playprompt.play_prompt("resources/kwota.WAV")

            playprompt.play_prompt(pathunity)
            if (dozens != '.wav'):
                playprompt.play_prompt(pathdozens)
            playprompt.play_prompt("resources/pln.WAV")
            playprompt.play_prompt("resources/glosnik_karta_krocej.WAV")
            playprompt.play_prompt("resources/muzyczka_1.WAV")
            time.sleep(random.randint(3, 6))
            trans_state = random.randint(1, 2)

        elif bool_opcja2 == True:
            # print(ticket_payment)
            unity, dozens = price(ticket_payment)
            # print(unity)

            pathunity = "resources/unity/" + unity
            pathdozens = "resources/dozens/" + dozens
            # print(pathunity)
            # print(pathdozens)
            playprompt.play_prompt("resources/kwota.WAV")

            playprompt.play_prompt(pathunity)
            if (dozens != '.wav'):
                playprompt.play_prompt(pathdozens)
            playprompt.play_prompt("resources/pln.WAV")
        
            playprompt.play_prompt("resources/glosnik_monety_krocej.WAV")
            playprompt.play_prompt("resources/muzyczka_1.WAV")
            time.sleep(10)  # oczekauje na monety i fotokomorka sprawdza czy klient dalej stoi przy automacie
            trans_state = random.randint(1, 2)

        if (bool_opcja1 == True and trans_state == 1):
            if (bool_opcja1 == True):
                playprompt.play_prompt("resources/transakcja_udana_karta.WAV")
            else:
                playprompt.play_prompt("resources/reszta_bilet_krocej.WAV")
            playprompt.play_prompt("resources/dziekujemy.WAV")
            return
        elif ((bool_opcja1 == True and trans_state == 2)):
            playprompt.play_prompt("resources/trans_nieudana.WAV")
            playprompt.play_prompt("resources/dziekujemy.WAV")
            return
        else:
            playprompt.play_prompt("resources/reszta_bilet_krocej.WAV")
            playprompt.play_prompt("resources/dziekujemy.WAV")
            return
    return


if __name__ == "__main__":
    main()
