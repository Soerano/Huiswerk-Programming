leeftijd = eval(input('Geef je leeftijd: '))
paspoort = (input('Nederlands paspoort: '))

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, u mag stemmen!')

else:
    print('U mag niet stemmen!')