class Dictionary:
    def __init__(self):
        pass

    def creaRaccolta(self):
        raccoglitore = {}
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            for riga in file:
                parole = riga.strip().split()  # Divide la riga in parole
                raccoglitore[parole[0]] = parole[1:]
        return raccoglitore

    def aggiornaRaccolta(self, dict):
        with open("dictionary.txt", "w", encoding="utf-8") as file:
            i = 0
            for chiave, valore in dict.items():
                if i == 0:
                    i = 1
                    file.write(f"{chiave} {' '.join(map(str, valore))}")
                else:
                    file.write(f"\n{chiave} {' '.join(map(str, valore))}")
            i = 0

    def addWord(self, esse):
        parole = esse.strip().split()
        raccoglitore = self.creaRaccolta()
        if parole[0] in raccoglitore:
            for i in range(1, len(parole)):
                if parole[i] not in raccoglitore[parole[0]]:
                    raccoglitore[parole[0]].append(parole[i])
            self.aggiornaRaccolta(raccoglitore)
            return 2
        else:
            with open("dictionary.txt", "a", encoding="utf-8") as file:
                file.write(f"\n{esse}")
            return 1

    def translate(self, parola):
        raccoglitore = self.creaRaccolta()
        for chiave in raccoglitore:
            if chiave == parola:
                return raccoglitore[chiave]
        pass

    def translateWordWildCard(self,parola):
        ter = parola.split("?")
        ter[0] = ter[0].lower()
        prima = ter[0].__len__()
        ter[1] = ter[1].lower()
        seconda = prima + 1
        raccoglitore = self.creaRaccolta()
        listaTemp = []
        for chiave in raccoglitore:
            if chiave.__len__() == parola.__len__():
                if ter[0] == chiave[0:prima] and ter[1] == chiave[seconda:]:
                    listaTemp.append(chiave)
        return listaTemp