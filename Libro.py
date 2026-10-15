class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, prezzo, pagine=None):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.prezzo = prezzo
        self.pagine = pagine

    def __str__(self):
        return f"{self.titolo} - {self.autore} ({self.anno_pubblicazione}), €{self.prezzo:.2f}"

    def __repr__(self):
        return self.__str__()

    def sconto(self, percentuale):
        if percentuale < 0 or percentuale > 100:
            raise ValueError("La percentuale di sconto deve essere compresa tra 0 e 100.")
        return self.prezzo * (1 - percentuale / 100)

    def reading_time(self, pagine=None, velocita=30):
        if pagine is None:
            if self.pagine is None:
                raise ValueError("Devi specificare il numero di pagine o impostarlo nel costruttore.")
            pagine = self.pagine

        if pagine <= 0:
            raise ValueError("Il numero di pagine deve essere positivo.")
        if velocita <= 0:
            raise ValueError("La velocità di lettura deve essere positiva.")

        minuti = pagine / velocita * 60
        ore = minuti / 60

        if ore < 1:
            return f"Tempo di lettura: {int(minuti)} minuti"
        return f"Tempo di lettura: {ore:.1f} ore"


# Esempio d'uso:
if __name__ == "__main__":
    libro1 = Libro("Il Nome della Rosa", "Umberto Eco", 1980, 19.90, pagine=500)
    print(libro1)
    print(f"Prezzo scontato: €{libro1.sconto(10):.2f}")
    print(libro1.reading_time())
    print(libro1.reading_time(200, velocita=40))
