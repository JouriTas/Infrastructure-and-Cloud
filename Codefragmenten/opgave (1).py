# ======================================================================
#                               O P G A V E
# ======================================================================
# 
# - Vraag de gebruiker om een IP-adres in te geven (formaat x.x.x.x).
#   Je mag uitgaan van een netmask 255.255.255.0 (2P)
# - Bereken het netwerkadres en broadcast adres uit dit IP-adres en 
#   geef beide adressen weer op het scherm. Bijv. "Het netwerkadres 
#   voor x.x.x.x is y.y.y.y". (6P: 2+2+1+1)
# - Bepaal 4 subnets op basis van het voorgaande netwerkadres (het 
#   netmask wordt dus 255.255.255.192). Je maakt hiervoor gebruik van 
#   een nieuwe functie. Bijv. bereken_subnets() (8P: 2+6)
# - Geef, per subnet, het eerste en laatste bruikbare IP-adres op het 
#   scherm weer. Het weergeven van de resultaten mag deel uitmaken van 
#   de nieuwe functie uit voorgaande functionele eis. Je hoeft dus geen 
#   nieuwe functie aan te maken. (4P)
#
# Voorzie een correcte bestandsnaam voor je oplossing. Deze bestaat uit 
# "PE1" gevolgd door je naam (underscore als spatie).
# Bijv. PE1_ronny_creygelman.py
# 
# Upload je oplossing via "Permanente evaluatie 1, practicum".
# 
# ======================================================================


# Functie om een ip-adres te converteren naar een decimaal getal - om mee te rekenen
def ip_naar_dec(ip_adres):
  ip_adres_split = ip_adres.split(".")
  txt = "{:08b}{:08b}{:08b}{:08b}"
  ip_adres_bin = txt.format(int(ip_adres_split[0]),
    int(ip_adres_split[1]),
    int(ip_adres_split[2]),
    int(ip_adres_split[3]))
  ip_adres_dec = int(ip_adres_bin, 2)
  return ip_adres_dec

# Functie om een decimaal getal te converteren naar een ip-adres - om weer te geven
def dec_naar_ip(decimaal):
  txt = "{:032b}"
  ip_adres_bin = txt.format(decimaal)
  groep_1 = ip_adres_bin[0:8]
  groep_2 = ip_adres_bin[8:16]
  groep_3 = ip_adres_bin[16:24]
  groep_4 = ip_adres_bin[24:32]
  txt = "{}.{}.{}.{}"
  ip_adres = txt.format(int(groep_1, 2),
    int(groep_2, 2),
    int(groep_3, 2), 
    int(groep_4, 2))
  return ip_adres

# Testcode, instellen van een subnet mask en een ip-adres. Berekenen van een netwerkadres.
sm_mask = "255.255.255.0"
print("Het ingegeven subnet mask is", sm_mask)
print("Het decimaal is", ip_naar_dec(sm_mask))

ip_adres = "192.168.10.2"
print("Het ingegeven IP adres is", ip_adres)
print("Het decimaal is", ip_naar_dec(ip_adres))

nw_adres_dec = ip_naar_dec(ip_adres) & ip_naar_dec(sm_mask)
print("Het netwerkadres is", dec_naar_ip(nw_adres_dec))
print("Het decimaal is", nw_adres_dec)
