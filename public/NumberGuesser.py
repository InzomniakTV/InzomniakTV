#global variables
sugar = 1.5
butter = 1
flour = 2.75
recipeCookiesAmount = 48

#functions
def ingredientsNeeded(cookiesRequested):
  #global variables references
  global sugar
  global butter
  global flour
  global recipeCookiesAmount

  #process ingredient amounts
  tempSugar = ((cookiesRequested/recipeCookiesAmount) * sugar)
  tempButter = ((cookiesRequested/recipeCookiesAmount) * butter)
  tempFlour = ((cookiesRequested/recipeCookiesAmount) * flour)

  #output
  print("You need {:.1f} cups of sugar, {:.1f} cups of butter, and {:.1f} cups of flour.".format(tempSugar, tempButter, tempFlour))

#input
cookiesRequested = int(input('Ayyy boss how many cookies you need? '))

#method calls
ingredientsNeeded(cookiesRequested)
