import dictionary as di

d = di.Dictionary()

class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("--------------------------")
        print("Translator Alien - Italian")
        print("--------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        pass

    def loadDictionary(self, dict):
        if dict == "dictionary.txt":
            raccoglitore = d.creaRaccolta()
            for chiave, valore in raccoglitore.items():
                print(chiave, *valore)
        else:
            print("Dizionario non trovato")
        pass

    def handleAdd(self, entry):
        e = d.addWord(entry)
        if e == 2:
            print("Parola già presente e quindi ho aggiornato le traduzioni")
        if e == 1:
            print("Parola non presente e quindi aggiunta al dizionario")
        pass

    def handleTranslate(self, query):
        print(f"Ecco le possibili traduzioni:")
        if d.translate(query).__len__() == 0:
            pass
        else:
            for element in d.translate(query):
                print(element)
        pass

    def handleWildCard(self,txtIn):
        cnt = 0
        for char in txtIn:
            if char == "?":
                cnt += 1
        if cnt == 1:
            d.translateWordWildCard(txtIn)
            for element in d.translateWordWildCard(txtIn):
                self.handleTranslate(element)
        else:
            print("Input non valido")
        pass