print("Hvor mange Danske kroner vil du veksle??")
dkk = input()
euro = 7.44
# print  (Euro)

penge = str(float(dkk) / euro)

commision = (0.02 * float(penge))

gebyr = 0.98 # 2%

udbetalt = str(float(penge) * gebyr)
if float(commision) > (float(euro) * 0.5): print ("Så får du " + (udbetalt) + " Euro")


if float(commision) < (float(euro) * 0.5): print ("Den angivede mængde penge, er desværre under minimums veksling på 3,72kr")
# print(penge)
# print ("Så får du " + str(int(udbetalt) + " Euro"))
# print ("Så får du " + str(int(dkk) / euro) + " Euro")

# Fiks så den ikke printer begge dele når de enkelte værdier er hvad de er.
# DEN VIRKER IKKE 