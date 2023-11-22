from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        grid_liste = []
        for _ in range(self._ant_rader):
            grid_liste.append(self._lag_tom_rad())
        return grid_liste

    def _lag_tom_rad(self):
        liste = []
        for _ in range(self._ant_kolonner):
            liste.append(None)
        return liste

    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)
                rand_num = randint(0,2)
            if rand_num == 0:
                self._rutenett[rad][kol].sett_levende()

    def lag_celle(self, rad, kol):
        self._rutenett[rad][kol] = Celle()
        

    def hent_celle(self, rad, kol):
        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
            cell = self._rutenett[rad][kol]
            return cell
        else:
            return None
        
    def tegn_rutenett(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                celle = self.hent_celle(rad, kol)
                print(celle.hent_status_tegn(), end='')
            print()

    def _sett_naboer(self, rad, kol):
        cell = self.hent_celle(rad, kol)
        if cell:
            naboer = [self.hent_celle(rad + 1, kol + 1), self.hent_celle(rad + 1, kol), 
                    self.hent_celle(rad, kol + 1), self.hent_celle(rad - 1, kol - 1), 
                    self.hent_celle(rad, kol - 1), self.hent_celle(rad - 1, kol), 
                    self.hent_celle(rad + 1, kol - 1), self.hent_celle(rad - 1, kol + 1)]
            for x in naboer:
                if x:
                    cell.legg_til_nabo(x)

    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        alle_celler = []
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                alle_celler.append(self.hent_celle(rad, kol))
        return alle_celler

    def antall_levende(self):
        counter = 0
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                if (self.hent_celle(rad, kol)).er_levende():
                    counter += 1
        return counter
