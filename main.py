teksts = input("ievadiet tekstu: ")

def deleteE(text):
  if text.count("e")>0:
    text = text.replace("e"," ")
    text = text.upper()
  else:
    text = "teksts nesatur vajadzigo burtu."
  return text
  print(text)