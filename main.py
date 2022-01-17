teksts = input("ievadiet cipari virkne: ")

def countNumbers(teksts):
  summa=0
  for simbols in teksts:
   summa = summa + int(simbols)
  return summa
countNumbers(teksts)