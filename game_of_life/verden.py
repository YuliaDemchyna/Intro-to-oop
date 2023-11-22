from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rader = rader
        self._kolonner = kolonner

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f'\nGenerasjonsnummer {self._generasjonsnummer}')
        print(f'Antall levende celler {self._rutenett.antall_levende()}')


    def oppdatering(self):
        self._rutenett.koble_celler()
        for rad in range(self._rader):
            for kol in range(self._kolonner):
                celle = self._rutenett.hent_celle(rad, kol)
                celle.tell_levende_naboer()

        for rad in range(self._rader):
            for kol in range(self._kolonner):
                celle = self._rutenett.hent_celle(rad, kol)
                celle.oppdater_status()

        self._generasjonsnummer += 1
        

        

                
