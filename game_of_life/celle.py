class Celle:
    # Konstruktør
    def __init__(self):
        self._status = 'doed'
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        self._status = 'doed'

    def sett_levende(self):
        self._status = 'levende'

    def er_levende(self):
        return self._status == 'levende'

    def hent_status_tegn(self):
        if self._status == 'levende':
            return 'O'
        else:
            return '.'

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        counter = 0
        for i in self._naboer:
            if i.er_levende():
                counter += 1
        self._ant_levende_naboer = counter

    def oppdater_status(self):
        if self._status == 'levende':
            if self._ant_levende_naboer < 2:
                self._status = 'doed'
            if self._ant_levende_naboer > 3:
                self._status = 'doed'
        if self._status == 'doed':
            if self._ant_levende_naboer == 3:
                self._status = 'levende'



