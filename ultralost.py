import time

from enum import Enum



   
class Methode :
    pass
    
    

class Spinnfischen (Methode) :

    def __init__(self, iGewicht, iFarbe, iName) :
        self.gewicht = iGewicht
        self.farbe = iFarbe
        self.name = iName

    gewicht = 0
    farbe = ""
    name = ""

class Blinker (Spinnfischen) :
    pass

class Wobbler (Spinnfischen) :
    pass

class Fliege (Spinnfischen) :
    pass




class Bodenmontage (Methode) :
    köder = ""

class Pose (Methode) :
    köder = ""



class Windrichtung (Enum) :
    N = 1
    S = 2
    W = 3
    O = 4
    NO = 5
    NW = 6
    SO = 7
    SW = 8

class Mondphase (Enum):
    vollmond = 1
    neumond = 2
    abnehmenderMond = 3
    zunehmenderMond = 4


class Wetter :
    windrichtung = Windrichtung (1) 
    windgeschwindigkeit = 0
    temperatur = 0
    luftfeuchtigkeit = 0
    mondphase = Mondphase (1)


    
class Fisch :
    #länge in meter
    länge = 0
    #gewicht in kilogramm
    gewicht = 0
    art = ""

    
class Fang :
    fisch = Fisch()
    ort = "" 
    uhrzeit = time.time()
    methode = Methode ()
    wetter = Wetter()


fang1 = Fang ()
fang1.fisch.art = "Hornhecht"
fang1.fisch.gewicht = 1
fang1.fisch.länge = 1
fang1.ort = "Skansehage"
fang1.uhrzeit = time.localtime ()
fang1.methode = Spinnfischen(14, "Rot", "Salty")






































    
