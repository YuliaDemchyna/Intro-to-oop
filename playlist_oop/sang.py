class Sang:

    def __init__(self, tittel: str, artist: str):       #the constructor
        self._tittel = tittel
        self._artist = artist

    def spill(self):        #prints a statement to a song that is playing right now
        print(f'Nå spilles {self._tittel} med {self._artist}')

    def sjekk_artist(self, navn: str):  
        navn_parts = navn.lower().split() # created a list of the string input with the method
        artist_parts = self._artist.lower().split() #created a list of all the words in the name
        for part in navn_parts: #using a for loop compared if the input is in the artists name
            if part in artist_parts:
                return True
        return False        # the return must be outside the loop to not return False before the whole list was itirated 

    def sjekk_tittel(self, tittel: str):
        return self._tittel.lower() == tittel.lower()  #all lowercase 

    def sjekk_artist_og_tittel(self, artist: str, tittel: str): #used the method from above if both true this will be true because of AND
        return self.sjekk_artist(artist) and self.sjekk_tittel(tittel)

    def streng_til_fil(self): #outputs a string
        return f'{self._tittel};{self._artist}\n'

                
