# make file 'temp_functions.py' and add two def fahr_to_celsius and temp_classifier

def fahr_to_celsius(temp_fahrenheit):
  #create converted_temp which is celsius temp of temp_fahrenheit, and show it
  converted_temp=(temp_fahrenheit-32)/1.8
  return converted_temp

def temp_classifier(temp_celsius):
  #create temp_classifier which classify by value of temp_celsius and return 0 or 1 or 2 or 3
  if  temp_celsius<-2:
    return 0
  elif  temp_celsius<2:
    return 1
  elif  temp_celsius<15:
    return 2
  else:
    return 3