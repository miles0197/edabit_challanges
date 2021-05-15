#Determine the sentence that is censored from a given wovels

def uncensor_text(txt, vowels):
  txt = list(txt)
  vowels = list(vowels)
  for i in range(len(txt)):
    if txt[i] == "*":
      txt[i] = vowels[0]
      del vowels[0]
	  #vowels.pop(0)
  return "".join(txt)
  #return("".join(txt))


print(uncensor_text("M*rh*b* n*b*r n*s*ls*n?","eaaaeaii"))
