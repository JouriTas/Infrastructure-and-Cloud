#!/bin/python3

def druk_af():
  print("Hallo")
  print("Volgende lijn")

druk_af()
druk_af()




#!/bin/python3

def druk_af(naam):
  print("Hallo", naam)
  print("Volgende lijn")

druk_af("Ronny")
druk_af("Elke")



#!/bin/python3

def verdubbel(getal):
  resultaat = getal * 2
  return resultaat

test = verdubbel(5)
print("Het resultaat is ", test)



#!/bin/python3

class Persoon:
  def __init__(self):
    self.naam = "Ronny"
  def afdrukken(self):
    print(self.naam)
  def welkom_boodschap(self):
    print("Hallo", self.naam)

ronny = Persoon()
ronny.afdrukken()
ronny.welkom_boodschap()



#!/bin/python3

class Persoon:
  def __init__(self, naam):
    self.naam = naam
  def afdrukken(self):
    print(self.naam)
  def welkom_boodschap(self):
    print("Hallo", self.naam)

ronny = Persoon("Ronny")
ronny.afdrukken()
ronny.welkom_boodschap()
test = Persoon("Elke")
test.afdrukken()
test.welkom_boodschap()
dimi = Persoon("Dimitri")
dimi.welkom_boodschap()




#!/bin/python3

class Persoon:
  def __init__(self, naam):
    self._naam = naam
  def afdrukken(self):
    print(self._naam)
  def welkom_boodschap(self):
    print("Hallo", self._naam)

ronny = Persoon("Ronny")
ronny.afdrukken()
ronny.welkom_boodschap()
test = Persoon("Elke")
test.afdrukken()
test.welkom_boodschap()
dimi = Persoon("Dimitri")
dimi.welkom_boodschap()
print(test._naam) # Verboden statement, _vars niet aanspreken of wijzigen
test._naam = "Kiekeboe" # Verboden statement
test.welkom_boodschap()




#!/bin/python3

# IP adres is id van een host
# opbouw ip adres = 4 octet (octet = 8 bits), decimaal, gescheiden door punten
# bijv. 192.168.0.1
# Eenvoudige communicatie, omdat ip-adres = 32 bit getal groot is.

# ip_adres = input("Geef een IP adres in:")

# Voorbereidende code
# octet = "92"
# octet_int = int(octet)
# txt = "Binair formaat {:08b}"
# print(txt.format(octet_int))

ip_adres = "192.168.0.1"
print("Het ingegeven IP adres is", ip_adres)

ip_adres_split = ip_adres.split(".")
txt = "{:08b}{:08b}{:08b}{:08b}"
ip_adres_bin = txt.format(int(ip_adres_split[0]),
  int(ip_adres_split[1]),
  int(ip_adres_split[2]),
  int(ip_adres_split[3]))
print(ip_adres_bin)
print(int(ip_adres_bin, 2))

ip_adres = "192.168.0.2"
print("Het ingegeven IP adres is", ip_adres)

ip_adres_split = ip_adres.split(".")
txt = "{:08b}{:08b}{:08b}{:08b}"
ip_adres_bin = txt.format(int(ip_adres_split[0]),
  int(ip_adres_split[1]),
  int(ip_adres_split[2]),
  int(ip_adres_split[3]))
print(ip_adres_bin)
print(int(ip_adres_bin, 2))




#!/bin/python3

# IP adres is id van een host
# opbouw ip adres = 4 octet (octet = 8 bits), decimaal, gescheiden door punten
# bijv. 192.168.0.1
# Eenvoudige communicatie, omdat ip-adres = 32 bit getal groot is.

# ip_adres = input("Geef een IP adres in:")

# Voorbereidende code
# octet = "92"
# octet_int = int(octet)
# txt = "Binair formaat {:08b}"
# print(txt.format(octet_int))

def ip_naar_dec(ip_adres):
  ip_adres_split = ip_adres.split(".")
  txt = "{:08b}{:08b}{:08b}{:08b}"
  ip_adres_bin = txt.format(int(ip_adres_split[0]),
    int(ip_adres_split[1]),
    int(ip_adres_split[2]),
    int(ip_adres_split[3]))
  ip_adres_dec = int(ip_adres_bin, 2)
  return ip_adres_dec

ip_adres = "192.168.0.1"
print("Het ingegeven IP adres is", ip_adres)
print("Het decimaal is", ip_naar_dec(ip_adres))

ip_adres = "192.168.0.2"
print("Het ingegeven IP adres is", ip_adres)
print("Het decimaal is", ip_naar_dec(ip_adres))

ip_adres = "192.168.0.100"
print("Het ingegeven IP adres is", ip_adres)
print("Het decimaal is", ip_naar_dec(ip_adres))

ip_adres = "192.168.1.0"
print("Het ingegeven IP adres is", ip_adres)
print("Het decimaal is", ip_naar_dec(ip_adres))






