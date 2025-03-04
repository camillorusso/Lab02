import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()
    txtIn = input(f"Seleziona una opzione: ")
    if (int(txtIn) < 1 or int(txtIn) > 5) or txtIn.isalpha():
        print("Input non valido!!!")
    else:
        pass

    if int(txtIn) == 1:
        txtIn = input(f"Inserisci la parola aliena e le sue rispettive traduzioni: ")
        if txtIn == "" or not isinstance(txtIn, str):
            print("Input non valido")
        else:
            txtIn = txtIn.lower()
            t.handleAdd(txtIn)
            txtIn = 1
        pass
    if int(txtIn) == 2:
        txtIn = input(f"Inserisci la parola aliena di cui vuoi scoprire la traduzione: ")
        if txtIn == "" or not isinstance(txtIn, str):
            print("Input non valido")
        else:
            txtIn = txtIn.lower()
            t.handleTranslate(txtIn)
            txtIn = 2
        pass
    if int(txtIn) == 3:
        print(f"Ricordati di inserire il carattere '?' nel nome della parola aliena soltanto una volta!")
        txtIn = input(f"Inserisci la parola aliena di cui vuoi scoprire la traduzione: ")
        if txtIn == "" or not isinstance(txtIn, str):
            print("Input non valido")
        else:
            t.handleWildCard(txtIn)
            txtIn = 3
        pass
    if int(txtIn) == 4:
        txtIn = input(f"Inserisci il nome del file del dizionario che vuoi visualizzare: ")
        if txtIn == "" or not isinstance(txtIn, str):
            print("Input non valido")
        else:
            txtIn = txtIn.lower()
            t.loadDictionary(txtIn)
            txtIn = 4
        pass
    if int(txtIn) == 5:
        break
