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

def dec_naar_ip(decimaal):
  # van decimaal naar binair
  # 4 groepjes 8 bit uit binair
  # binair -> decimaal per groep, scheiden door een punt
  return ip_adres

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
  
def dec_naar_ip(decimaal):
  # van decimaal naar binair
  txt = "{:032b}"
  ip_adres_bin = txt.format(decimaal)
  # 4 groepjes 8 bit uit binair
  groep_1 = ip_adres_bin[0:8]
  groep_2 = ip_adres_bin[8:16]
  groep_3 = ip_adres_bin[16:24]
  groep_4 = ip_adres_bin[24:32]
  # binair -> decimaal per groep, scheiden door een punt
  txt = "{}.{}.{}.{}"
  ip_adres = txt.format(int(groep_1, 2),
    int(groep_2, 2),
    int(groep_3, 2), 
    int(groep_4, 2))
  return ip_adres
  
sm_mask = "255.255.255.0"
sm_mask_dec = ip_naar_dec(sm_mask)
print("Het ingegeven Ip adres is", sm_mask)
print("Het decimaal is", sm_mask_dec)

ip_adres = "192.168.0.2"
ip_adres_dec = ip_naar_dec(ip_adres)
print("Het ingegeven Ip adres is", ip_adres)
print("Het decimaal is", ip_adres_dec)

nw_adres_dec = ip_adres_dec & sm_mask_dec
nw_adres = dec_naar_ip(nw_adres_dec)
print("Het ingegeven Ip adres is", nw_adres)
print("Het decimaal is", nw_adres_dec)

host_dec = nw_adres_dec + 250
host = dec_naar_ip(host_dec)
print("Het IP adres van de 250e host", host)
print("Het decimaal van de 250e host", host_dec)

host_id = ip_adres_dec - nw_adres_dec
print("De host ID van het ip-adres is", host_id)





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
  
def dec_naar_ip(decimaal):
  # van decimaal naar binair
  txt = "{:032b}"
  ip_adres_bin = txt.format(decimaal)
  # 4 groepjes 8 bit uit binair
  groep_1 = ip_adres_bin[0:8]
  groep_2 = ip_adres_bin[8:16]
  groep_3 = ip_adres_bin[16:24]
  groep_4 = ip_adres_bin[24:32]
  # binair -> decimaal per groep, scheiden door een punt
  txt = "{}.{}.{}.{}"
  ip_adres = txt.format(int(groep_1, 2),
    int(groep_2, 2),
    int(groep_3, 2), 
    int(groep_4, 2))
  return ip_adres
  
sm_mask = "255.255.255.0"
sm_mask_dec = ip_naar_dec(sm_mask)
print("Het ingegeven sm is", sm_mask)

ip_adres = "192.168.0.2"
ip_adres_dec = ip_naar_dec(ip_adres)
print("Het ingegeven ip adres is", ip_adres)

nw_adres_dec = ip_adres_dec & sm_mask_dec
nw_adres = dec_naar_ip(nw_adres_dec)
print("Het netwerkadres", nw_adres)

host_dec = nw_adres_dec + 250
host = dec_naar_ip(host_dec)
print("Het IP adres van de 250e host", host)

host_id = ip_adres_dec - nw_adres_dec
print("De host ID van het ip-adres is", host_id)





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

class IP_Adres:
  def __init__(self):
    self.decimaal = 0

  def set_dotted(self, ip_adres):
    ip_adres_split = ip_adres.split(".")
    txt = "{:08b}{:08b}{:08b}{:08b}"
    ip_adres_bin = txt.format(int(ip_adres_split[0]),
      int(ip_adres_split[1]),
      int(ip_adres_split[2]),
      int(ip_adres_split[3]))
    ip_adres_dec = int(ip_adres_bin, 2)
    self.decimaal = ip_adres_dec
  
  def get_dotted(self):
    # van decimaal naar binair
    txt = "{:032b}"
    ip_adres_bin = txt.format(self.decimaal)
    # 4 groepjes 8 bit uit binair
    groep_1 = ip_adres_bin[0:8]
    groep_2 = ip_adres_bin[8:16]
    groep_3 = ip_adres_bin[16:24]
    groep_4 = ip_adres_bin[24:32]
    # binair -> decimaal per groep, scheiden door een punt
    txt = "{}.{}.{}.{}"
    ip_adres = txt.format(int(groep_1, 2),
      int(groep_2, 2),
      int(groep_3, 2), 
      int(groep_4, 2))
    return ip_adres
  
  def set_decimal(self, decimaal):
    self.decimaal = decimaal
    
  def get_decimal(self):
    return self.decimaal
  
sm_mask = IP_Adres()
sm_mask.set_dotted("255.255.255.0")
print("Het ingegeven sm is", sm_mask.get_dotted())

ip_adres = IP_Adres()
ip_adres.set_dotted("192.168.0.2")
print("Het ingegeven ip adres is", ip_adres.get_dotted())

nw_adres = IP_Adres()
nw_adres_dec = ip_adres.get_decimal() & sm_mask.get_decimal()
nw_adres.set_decimal(nw_adres_dec)
print("Het netwerkadres", nw_adres.get_dotted())

host = IP_Adres()
host_dec = nw_adres.get_decimal() + 250
host.set_decimal(host_dec)
print("Het IP adres van de 250e host", host.get_dotted())

host_id = ip_adres.get_decimal() - nw_adres.get_decimal()
print("De host ID van het ip-adres is", host_id)






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

class IP_Adres:
  def __init__(self):
    self._decimaal = 0

  def set_dotted(self, ip_adres):
    ip_adres_split = ip_adres.split(".")
    txt = "{:08b}{:08b}{:08b}{:08b}"
    ip_adres_bin = txt.format(int(ip_adres_split[0]),
      int(ip_adres_split[1]),
      int(ip_adres_split[2]),
      int(ip_adres_split[3]))
    ip_adres_dec = int(ip_adres_bin, 2)
    self._decimaal = ip_adres_dec
  
  def get_dotted(self):
    # van decimaal naar binair
    txt = "{:032b}"
    ip_adres_bin = txt.format(self._decimaal)
    # 4 groepjes 8 bit uit binair
    groep_1 = ip_adres_bin[0:8]
    groep_2 = ip_adres_bin[8:16]
    groep_3 = ip_adres_bin[16:24]
    groep_4 = ip_adres_bin[24:32]
    # binair -> decimaal per groep, scheiden door een punt
    txt = "{}.{}.{}.{}"
    ip_adres = txt.format(int(groep_1, 2),
      int(groep_2, 2),
      int(groep_3, 2), 
      int(groep_4, 2))
    return ip_adres
  
  def set_decimal(self, decimaal):
    self._decimaal = decimaal
    
  def get_decimal(self):
    return self._decimaal

sm_mask = IP_Adres()
sm_mask.set_dotted("255.255.255.0")
print("Het ingegeven sm is", sm_mask.get_dotted())

ip_adres = IP_Adres()
ip_adres.set_dotted("192.168.0.2")
print("Het ingegeven ip adres is", ip_adres.get_dotted())

nw_adres = IP_Adres()
nw_adres_dec = ip_adres.get_decimal() & sm_mask.get_decimal()
nw_adres.set_decimal(nw_adres_dec)
print("Het netwerkadres", nw_adres.get_dotted())

host = IP_Adres()
host_dec = nw_adres.get_decimal() + 250
host.set_decimal(host_dec)
print("Het IP adres van de 250e host", host.get_dotted())

host_id = ip_adres.get_decimal() - nw_adres.get_decimal()
print("De host ID van het ip-adres is", host_id)





# Opgave
# Vul deze klasse aan met de inhoud van de methoden

class Temperatuur:
  def __init__(self):
    self._kelvin = 0
    
  def set_celsius(self, celsius):
    # Vul aan
    self._kelvin = 0
    
  def get_celsius(self):
    # Vul aan
    return 0 # vul aan
    
  def set_fahrenheit(self, fahrenheit):
    # Vul aan
    self._kelvin = 0
    
  def get_fahrenheit(self):
    # Vul aan
    return 0 # vul aan
    
  def set_kelvin(self, kelvin):
    self._kelvin = kelvin
    
  def get_kelvin(self):
    return self._kelvin


x = Temperatuur()
x.set_kelvin(100)
print(x.get_kelvin())
print(x.get_fahrenheit())
print(x.get_celsius())