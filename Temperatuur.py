# Opgave
# Vul deze klasse aan met de inhoud van de methoden

class Temperatuur:
  def __init__(self):
    self._kelvin = 273.16
    
  def set_celsius(self, celsius):
    # Vul aan
    self._kelvin = celsius + 273.16
    
  def get_celsius(self):
    # Vul aan
    return self._kelvin - 273.16
    
  def set_fahrenheit(self, fahrenheit):
    # Vul aan
    self._kelvin = (fahrenheit - 32) * 5 / 9 + 273.16
    
  def get_fahrenheit(self):
    # Vul aan
    return (self._kelvin - 273.16) * 9 / 5 + 32
    
  def set_kelvin(self, kelvin):
    self._kelvin = kelvin
    
  def get_kelvin(self):
    return self._kelvin
    


x = Temperatuur()
x.set_kelvin(100)
print(x.get_kelvin())
print(x.get_fahrenheit())