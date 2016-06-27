#!/usr/bin/env python3

# Monster credit to "https://en.wikipedia.org/wiki/Names_of_large_numbers" for giving me this idea and for giving the latin roots needed!

import skilstak.colors as c
import re
result = ''
def get_triplet(digit_number):
  digit_number = re.sub('^0+(\\d)','\\1',digit_number)
  singles = 0
  singles_list = []
  for listing in digit_number:
    singles_list.append(listing)
  word_singles = ['one','two','three','four','five','six','seven','eight','nine']
  word_doubles = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'] # I looked it up! It's "forty" not "fourty"
  word_teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  word_triples = ['one-hundred','two-hundred','three-hundred','four-hundred','five-hundred','six-hundred','seven-hundred','eight-hundred','nine-hundred']
  for single in digit_number:
    singles += 1
  if str(digit_number) == '0' * singles:
    return ''
  if singles == 1:
    return word_singles.pop(int(digit_number)-1)
  if singles == 2:
    tens = int(singles_list.pop(0))
    ones = int(singles_list.pop(0))
    if tens == 1 and ones != 0:
      return word_teens.pop(ones-1)
    elif ones == 0:
      return word_doubles.pop(tens-1)
    else:
      return word_doubles.pop(tens-1) + '-' + word_singles.pop(ones-1)
  if singles == 3:
    hundreds = int(singles_list.pop(0))
    tens = int(singles_list.pop(0))
    ones = int(singles_list.pop(0))
    if tens == 1 and ones != 0:
      return word_triples.pop(hundreds-1) + '-' + word_teens.pop(ones-1)
    elif tens != 0 and ones != 0:
      return word_triples.pop(hundreds-1) + '-' + word_doubles.pop(tens-1) + '-' + word_singles.pop(ones-1)
    elif tens == 0 and ones != 0:
      return word_triples.pop(hundreds-1) + '-' + word_singles.pop(ones-1)
    elif tens != 0 and ones == 0:
      return word_triples.pop(hundreds-1) + '-' + word_doubles.pop(tens-1)
    elif tens == 0 and ones == 0:
      return word_triples.pop(hundreds-1)
while True:
  chopped_number = []
  digits = 0
  baseup = 0
  full_triplets = [] 
  base_triplets = ['-thousand-', '-million-', '-billion-', '-trillion-', '-quadrillion-', '-pintillion-', '-sextillion-', '-septillion-', '-octillion-', '-nonillion-', '-decillion-', '-undecillion-', '-duodecillion-', '-tredecillion-', '-quattuorecillion-', '-quinquadecillion-', '-septendecillion-', '-octodecillion-', '-novendecillion-', '-vigintillion-', '-unvigintillion-', '-duovigintillion-', '-tresvigintillion-', '-quattourvigintillion-', '-quinquavigintillion-', '-sesvigintillion-', '-septemvigintillion-', '-octovigintillion-', '-novemvigintillion-', '-trigintillion-', '-untrigintillion-', '-duotrigintillion-', '-trestrigintillion-', '-quattourtrigintillion-', '-quinquatrigintillion-', '-sestrigintillion-', '-septemtrigintillion-', '-octotrigintillion-', '-novemtrigintillion-', '-quadragintillion-', '-unquadragintillion-', '-duoquadragintillion-', '-tresquadragintillion-', '-quattourquadragintillion-', '-quinquaquadragintillion-', '-sesquadragintillion-', '-septemquadragintillion-', '-octoquadragintillion-', '-novemquadragintillion-', '-quinquagintillion-', '-unquinquagintillion-', '-duoquinquagintillion-', '-tresquinquagintillion-', '-quattourquinquagintillion-', '-quinquaquinquagintillion-', '-sesquinquagintillion-', '-septemquinquagintillion-', '-octoquinquagintillion-', '-novemquinquagintillion-', '-sexagintillion-', '-unsexagintillion-', '-duosexagintillion-', '-tresexagintillion-', '-quattoursexagintillion-', '-quinquasexagintillion-', '-sesexagintillion-', '-septemsexagintillion-', '-octosexagintillion-', '-novemsexagintillion-', '-septuagintillion-', '-unseptuagintillion-', '-duoseptuagintillion-', '-treseptuagintillion-', '-quattourseptuagintillion-', '-quinquaseptuagintillion-', '-seseptuagintillion-', '-septemseptuagintillion-', '-octoseptuagintillion-', '-novemseptuagintillion-', '-octogintillion-', '-unoctogintillion-', '-duooctogintillion-', '-treoctogintillion-', '-quattouroctogintillion-', '-quinquaoctogintillion-', '-seoctogintillion-', '-septemoctogintillion-', '-octooctogintillion-', '-novemoctogintillion-', '-nonagintillion-', '-unnonagintillion-', '-duononagintillion-', '-trenonagintillion-', '-quattournonagintillion-', '-quinquanonagintillion-', '-senonagintillion-', '-septenonagintillion-', '-octononagintillion-', '-novenonagintillion-', '-centillion-', '-uncentillion-', '-duocentillion-', '-trescentillion-', '-quattourcentillion-', '-quinquacentillion-', '-sescentillion-', '-septemcentillion-', '-octocentillion-', '-novemcentillion-', '-decicentillion-', '-undecicentillion-', '-duodecicentillion-', '-tredecicentillion-', '-quattourdecicentillion-', '-quinquadecicentillion-', '-sedecicentillion-', '-septemdecicentillion-', '-octodecicentillion-', '-novemdecicentillion-', '-viginticentillion-', '-unviginticentillion-', '-duoviginticentillion-', '-tresviginticentillion-', '-quattourviginticentillion-', '-quinquaviginticentillion-', '-sesviginticentillion-', '-septemviginticentillion-', '-octoviginticentillion-', '-novemviginticentillion-', '-trigintacentillion-', '-untrigintacentillion-', '-duotrigintacentillion-', '-trestrigintacentillion-', '-quattourtrigintacentillion-', '-quinquatrigintacentillion-', '-sestrigintacentillion-', '-septemtrigintacentillion-', '-octotrigintacentillion-', '-novemtrigintacentillion-', '-quadragintacentillion-', '-unquadragintacentillion-', '-duoquadragintacentillion-', '-tresquadragintacentillion-', '-quattourquadragintacentillion-', '-quinquaquadragintacentillion-', '-sesquadragintacentillion-', '-septemquadragintacentillion-', '-octoquadragintacentillion-', '-novemquadragintacentillion-', '-quinquagintacentillion-', '-unquinquagintacentillion-', '-duoquinquagintacentillion-', '-tresquinquagintacentillion-', '-quattourquinquagintacentillion-', '-quinquaquinquagintacentillion-', '-sesquinquagintacentillion-', '-septemquinquagintacentillion-', '-octoquinquagintacentillion-', '-novemquinquagintacentillion-', '-sexagintacentillion-', '-unsexagintacentillion-', '-duosexagintacentillion-', '-tresexagintacentillion-', '-quattoursexagintacentillion-', '-quinquasexagintacentillion-', '-sesexagintacentillion-', '-septemsexagintacentillion-', '-octosexagintacentillion-', '-novemsexagintacentillion-', '-septuagintacentillion-', '-unseptuagintacentillion-', '-duoseptuagintacentillion-', '-treseptuagintacentillion-', '-quattourseptuagintacentillion-', '-quinquaseptuagintacentillion-', '-seseptuagintacentillion-', '-septemseptuagintacentillion-', '-octoseptuagintacentillion-', '-novemseptuagintacentillion-', '-octogintacentillion-', '-unoctogintacentillion-', '-duooctogintacentillion-', '-treoctogintacentillion-', '-quattouroctogintacentillion-', '-quinquaoctogintacentillion-', '-seoctogintacentillion-', '-septemoctogintacentillion-', '-octooctogintacentillion-', '-novemoctogintacentillion-', '-nonagintacentillion-', '-unnonagintacentillion-', '-duononagintacentillion-', '-trenonagintacentillion-', '-quattournonagintacentillion-', '-quinquanonagintacentillion-', '-senonagintacentillion-', '-septenonagintacentillion-', '-octononagintacentillion-', '-novenonagintacentillion-', '-ducentillion-', '-unducentillion-', '-duoducentillion-', '-treducentillion-', '-quattourducentillion-', '-quinquaducentillion-', '-seducentillion-', '-septemducentillion-', '-octoducentillion-', '-novemducentillion-', '-deciducentillion-', '-undeciducentillion-', '-duodeciducentillion-', '-tredeciducentillion-', '-quattourdeciducentillion-', '-quinquadeciducentillion-', '-sedeciducentillion-', '-septemdeciducentillion-', '-octodeciducentillion-', '-novemdeciducentillion-', '-vigintiducentillion-', '-unvigintiducentillion-', '-duovigintiducentillion-', '-tresvigintiducentillion-', '-quattourvigintiducentillion-', '-quinquavigintiducentillion-', '-sesvigintiducentillion-', '-septemvigintiducentillion-', '-octovigintiducentillion-', '-novemvigintiducentillion-', '-trigintaducentillion-', '-untrigintaducentillion-', '-duotrigintaducentillion-', '-trestrigintaducentillion-', '-quattourtrigintaducentillion-', '-quinquatrigintaducentillion-', '-sestrigintaducentillion-', '-septemtrigintaducentillion-', '-octotrigintaducentillion-', '-novemtrigintaducentillion-', '-quadragintaducentillion-', '-unquadragintaducentillion-', '-duoquadragintaducentillion-', '-tresquadragintaducentillion-', '-quattourquadragintaducentillion-', '-quinquaquadragintaducentillion-', '-sesquadragintaducentillion-', '-septemquadragintaducentillion-', '-octoquadragintaducentillion-', '-novemquadragintaducentillion-', '-quinquagintaducentillion-', '-unquinquagintaducentillion-', '-duoquinquagintaducentillion-', '-tresquinquagintaducentillion-', '-quattourquinquagintaducentillion-', '-quinquaquinquagintaducentillion-', '-sesquinquagintaducentillion-', '-septemquinquagintaducentillion-', '-octoquinquagintaducentillion-', '-novemquinquagintaducentillion-', '-sexagintaducentillion-', '-unsexagintaducentillion-', '-duosexagintaducentillion-', '-tresexagintaducentillion-', '-quattoursexagintaducentillion-', '-quinquasexagintaducentillion-', '-sesexagintaducentillion-', '-septemsexagintaducentillion-', '-octosexagintaducentillion-', '-novemsexagintaducentillion-', '-septuagintaducentillion-', '-unseptuagintaducentillion-', '-duoseptuagintaducentillion-', '-treseptuagintaducentillion-', '-quattourseptuagintaducentillion-', '-quinquaseptuagintaducentillion-', '-seseptuagintaducentillion-', '-septemseptuagintaducentillion-', '-octoseptuagintaducentillion-', '-novemseptuagintaducentillion-', '-octogintaducentillion-', '-unoctogintaducentillion-', '-duooctogintaducentillion-', '-treoctogintaducentillion-', '-quattouroctogintaducentillion-', '-quinquaoctogintaducentillion-', '-seoctogintaducentillion-', '-septemoctogintaducentillion-', '-octooctogintaducentillion-', '-novemoctogintaducentillion-', '-nonagintaducentillion-', '-unnonagintaducentillion-', '-duononagintaducentillion-', '-trenonagintaducentillion-', '-quattournonagintaducentillion-', '-quinquanonagintaducentillion-', '-senonagintaducentillion-', '-septenonagintaducentillion-', '-octononagintaducentillion-', '-novenonagintaducentillion-', '-tricentillion-', '-untricentillion-', '-duotricentillion-', '-tretricentillion-', '-quattourtricentillion-', '-quinquatricentillion-', '-setricentillion-', '-septemtricentillion-', '-octotricentillion-', '-novemtricentillion-', '-decitricentillion-', '-undecitricentillion-', '-duodecitricentillion-', '-tredecitricentillion-', '-quattourdecitricentillion-', '-quinquadecitricentillion-', '-sedecitricentillion-', '-septemdecitricentillion-', '-octodecitricentillion-', '-novemdecitricentillion-', '-vigintitricentillion-', '-unvigintitricentillion-', '-duovigintitricentillion-', '-tresvigintitricentillion-', '-quattourvigintitricentillion-', '-quinquavigintitricentillion-', '-sesvigintitricentillion-', '-septemvigintitricentillion-', '-octovigintitricentillion-', '-novemvigintitricentillion-', '-trigintatricentillion-', '-untrigintatricentillion-', '-duotrigintatricentillion-', '-trestrigintatricentillion-', '-quattourtrigintatricentillion-', '-quinquatrigintatricentillion-', '-sestrigintatricentillion-', '-septemtrigintatricentillion-', '-octotrigintatricentillion-', '-novemtrigintatricentillion-', '-quadragintatricentillion-', '-unquadragintatricentillion-', '-duoquadragintatricentillion-', '-tresquadragintatricentillion-', '-quattourquadragintatricentillion-', '-quinquaquadragintatricentillion-', '-sesquadragintatricentillion-', '-septemquadragintatricentillion-', '-octoquadragintatricentillion-', '-novemquadragintatricentillion-', '-quinquagintatricentillion-', '-unquinquagintatricentillion-', '-duoquinquagintatricentillion-', '-tresquinquagintatricentillion-', '-quattourquinquagintatricentillion-', '-quinquaquinquagintatricentillion-', '-sesquinquagintatricentillion-', '-septemquinquagintatricentillion-', '-octoquinquagintatricentillion-', '-novemquinquagintatricentillion-', '-sexagintatricentillion-', '-unsexagintatricentillion-', '-duosexagintatricentillion-', '-tresexagintatricentillion-', '-quattoursexagintatricentillion-', '-quinquasexagintatricentillion-', '-sesexagintatricentillion-', '-septemsexagintatricentillion-', '-octosexagintatricentillion-', '-novemsexagintatricentillion-', '-septuagintatricentillion-', '-unseptuagintatricentillion-', '-duoseptuagintatricentillion-', '-treseptuagintatricentillion-', '-quattourseptuagintatricentillion-', '-quinquaseptuagintatricentillion-', '-seseptuagintatricentillion-', '-septemseptuagintatricentillion-', '-octoseptuagintatricentillion-', '-novemseptuagintatricentillion-', '-octogintatricentillion-', '-unoctogintatricentillion-', '-duooctogintatricentillion-', '-treoctogintatricentillion-', '-quattouroctogintatricentillion-', '-quinquaoctogintatricentillion-', '-seoctogintatricentillion-', '-septemoctogintatricentillion-', '-octooctogintatricentillion-', '-novemoctogintatricentillion-', '-nonagintatricentillion-', '-unnonagintatricentillion-', '-duononagintatricentillion-', '-trenonagintatricentillion-', '-quattournonagintatricentillion-', '-quinquanonagintatricentillion-', '-senonagintatricentillion-', '-septenonagintatricentillion-', '-octononagintatricentillion-', '-novenonagintatricentillion-', '-quadringentillion-', '-unquadringentillion-', '-duoquadringentillion-', '-trequadringentillion-', '-quattourquadringentillion-', '-quinquaquadringentillion-', '-sequadringentillion-', '-septemquadringentillion-', '-octoquadringentillion-', '-novemquadringentillion-', '-deciquadringentillion-', '-undeciquadringentillion-', '-duodeciquadringentillion-', '-tredeciquadringentillion-', '-quattourdeciquadringentillion-', '-quinquadeciquadringentillion-', '-sedeciquadringentillion-', '-septemdeciquadringentillion-', '-octodeciquadringentillion-', '-novemdeciquadringentillion-', '-vigintiquadringentillion-', '-unvigintiquadringentillion-', '-duovigintiquadringentillion-', '-tresvigintiquadringentillion-', '-quattourvigintiquadringentillion-', '-quinquavigintiquadringentillion-', '-sesvigintiquadringentillion-', '-septemvigintiquadringentillion-', '-octovigintiquadringentillion-', '-novemvigintiquadringentillion-', '-trigintaquadringentillion-', '-untrigintaquadringentillion-', '-duotrigintaquadringentillion-', '-trestrigintaquadringentillion-', '-quattourtrigintaquadringentillion-', '-quinquatrigintaquadringentillion-', '-sestrigintaquadringentillion-', '-septemtrigintaquadringentillion-', '-octotrigintaquadringentillion-', '-novemtrigintaquadringentillion-', '-quadragintaquadringentillion-', '-unquadragintaquadringentillion-', '-duoquadragintaquadringentillion-', '-tresquadragintaquadringentillion-', '-quattourquadragintaquadringentillion-', '-quinquaquadragintaquadringentillion-', '-sesquadragintaquadringentillion-', '-septemquadragintaquadringentillion-', '-octoquadragintaquadringentillion-', '-novemquadragintaquadringentillion-', '-quinquagintaquadringentillion-', '-unquinquagintaquadringentillion-', '-duoquinquagintaquadringentillion-', '-tresquinquagintaquadringentillion-', '-quattourquinquagintaquadringentillion-', '-quinquaquinquagintaquadringentillion-', '-sesquinquagintaquadringentillion-', '-septemquinquagintaquadringentillion-', '-octoquinquagintaquadringentillion-', '-novemquinquagintaquadringentillion-', '-sexagintaquadringentillion-', '-unsexagintaquadringentillion-', '-duosexagintaquadringentillion-', '-tresexagintaquadringentillion-', '-quattoursexagintaquadringentillion-', '-quinquasexagintaquadringentillion-', '-sesexagintaquadringentillion-', '-septemsexagintaquadringentillion-', '-octosexagintaquadringentillion-', '-novemsexagintaquadringentillion-', '-septuagintaquadringentillion-', '-unseptuagintaquadringentillion-', '-duoseptuagintaquadringentillion-', '-treseptuagintaquadringentillion-', '-quattourseptuagintaquadringentillion-', '-quinquaseptuagintaquadringentillion-', '-seseptuagintaquadringentillion-', '-septemseptuagintaquadringentillion-', '-octoseptuagintaquadringentillion-', '-novemseptuagintaquadringentillion-', '-octogintaquadringentillion-', '-unoctogintaquadringentillion-', '-duooctogintaquadringentillion-', '-treoctogintaquadringentillion-', '-quattouroctogintaquadringentillion-', '-quinquaoctogintaquadringentillion-', '-seoctogintaquadringentillion-', '-septemoctogintaquadringentillion-', '-octooctogintaquadringentillion-', '-novemoctogintaquadringentillion-', '-nonagintaquadringentillion-', '-unnonagintaquadringentillion-', '-duononagintaquadringentillion-', '-trenonagintaquadringentillion-', '-quattournonagintaquadringentillion-', '-quinquanonagintaquadringentillion-', '-senonagintaquadringentillion-', '-septenonagintaquadringentillion-', '-octononagintaquadringentillion-', '-novenonagintaquadringentillion-', '-quingentillion-', '-unquingentillion-', '-duoquingentillion-', '-trequingentillion-', '-quattourquingentillion-', '-quinquaquingentillion-', '-sequingentillion-', '-septemquingentillion-', '-octoquingentillion-', '-novemquingentillion-', '-deciquingentillion-', '-undeciquingentillion-', '-duodeciquingentillion-', '-tredeciquingentillion-', '-quattourdeciquingentillion-', '-quinquadeciquingentillion-', '-sedeciquingentillion-', '-septemdeciquingentillion-', '-octodeciquingentillion-', '-novemdeciquingentillion-', '-vigintiquingentillion-', '-unvigintiquingentillion-', '-duovigintiquingentillion-', '-tresvigintiquingentillion-', '-quattourvigintiquingentillion-', '-quinquavigintiquingentillion-', '-sesvigintiquingentillion-', '-septemvigintiquingentillion-', '-octovigintiquingentillion-', '-novemvigintiquingentillion-', '-trigintaquingentillion-', '-untrigintaquingentillion-', '-duotrigintaquingentillion-', '-trestrigintaquingentillion-', '-quattourtrigintaquingentillion-', '-quinquatrigintaquingentillion-', '-sestrigintaquingentillion-', '-septemtrigintaquingentillion-', '-octotrigintaquingentillion-', '-novemtrigintaquingentillion-', '-quadragintaquingentillion-', '-unquadragintaquingentillion-', '-duoquadragintaquingentillion-', '-tresquadragintaquingentillion-', '-quattourquadragintaquingentillion-', '-quinquaquadragintaquingentillion-', '-sesquadragintaquingentillion-', '-septemquadragintaquingentillion-', '-octoquadragintaquingentillion-', '-novemquadragintaquingentillion-', '-quinquagintaquingentillion-', '-unquinquagintaquingentillion-', '-duoquinquagintaquingentillion-', '-tresquinquagintaquingentillion-', '-quattourquinquagintaquingentillion-', '-quinquaquinquagintaquingentillion-', '-sesquinquagintaquingentillion-', '-septemquinquagintaquingentillion-', '-octoquinquagintaquingentillion-', '-novemquinquagintaquingentillion-', '-sexagintaquingentillion-', '-unsexagintaquingentillion-', '-duosexagintaquingentillion-', '-tresexagintaquingentillion-', '-quattoursexagintaquingentillion-', '-quinquasexagintaquingentillion-', '-sesexagintaquingentillion-', '-septemsexagintaquingentillion-', '-octosexagintaquingentillion-', '-novemsexagintaquingentillion-', '-septuagintaquingentillion-', '-unseptuagintaquingentillion-', '-duoseptuagintaquingentillion-', '-treseptuagintaquingentillion-', '-quattourseptuagintaquingentillion-', '-quinquaseptuagintaquingentillion-', '-seseptuagintaquingentillion-', '-septemseptuagintaquingentillion-', '-octoseptuagintaquingentillion-', '-novemseptuagintaquingentillion-', '-octogintaquingentillion-', '-unoctogintaquingentillion-', '-duooctogintaquingentillion-', '-treoctogintaquingentillion-', '-quattouroctogintaquingentillion-', '-quinquaoctogintaquingentillion-', '-seoctogintaquingentillion-', '-septemoctogintaquingentillion-', '-octooctogintaquingentillion-', '-novemoctogintaquingentillion-', '-nonagintaquingentillion-', '-unnonagintaquingentillion-', '-duononagintaquingentillion-', '-trenonagintaquingentillion-', '-quattournonagintaquingentillion-', '-quinquanonagintaquingentillion-', '-senonagintaquingentillion-', '-septenonagintaquingentillion-', '-octononagintaquingentillion-', '-novenonagintaquingentillion-', '-sescentillion-', '-unsescentillion-', '-duosescentillion-', '-tresescentillion-', '-quattoursescentillion-', '-quinquasescentillion-', '-sesescentillion-', '-septemsescentillion-', '-octosescentillion-', '-novemsescentillion-', '-decisescentillion-', '-undecisescentillion-', '-duodecisescentillion-', '-tredecisescentillion-', '-quattourdecisescentillion-', '-quinquadecisescentillion-', '-sedecisescentillion-', '-septemdecisescentillion-', '-octodecisescentillion-', '-novemdecisescentillion-', '-vigintisescentillion-', '-unvigintisescentillion-', '-duovigintisescentillion-', '-tresvigintisescentillion-', '-quattourvigintisescentillion-', '-quinquavigintisescentillion-', '-sesvigintisescentillion-', '-septemvigintisescentillion-', '-octovigintisescentillion-', '-novemvigintisescentillion-', '-trigintasescentillion-', '-untrigintasescentillion-', '-duotrigintasescentillion-', '-trestrigintasescentillion-', '-quattourtrigintasescentillion-', '-quinquatrigintasescentillion-', '-sestrigintasescentillion-', '-septemtrigintasescentillion-', '-octotrigintasescentillion-', '-novemtrigintasescentillion-', '-quadragintasescentillion-', '-unquadragintasescentillion-', '-duoquadragintasescentillion-', '-tresquadragintasescentillion-', '-quattourquadragintasescentillion-', '-quinquaquadragintasescentillion-', '-sesquadragintasescentillion-', '-septemquadragintasescentillion-', '-octoquadragintasescentillion-', '-novemquadragintasescentillion-', '-quinquagintasescentillion-', '-unquinquagintasescentillion-', '-duoquinquagintasescentillion-', '-tresquinquagintasescentillion-', '-quattourquinquagintasescentillion-', '-quinquaquinquagintasescentillion-', '-sesquinquagintasescentillion-', '-septemquinquagintasescentillion-', '-octoquinquagintasescentillion-', '-novemquinquagintasescentillion-', '-sexagintasescentillion-', '-unsexagintasescentillion-', '-duosexagintasescentillion-', '-tresexagintasescentillion-', '-quattoursexagintasescentillion-', '-quinquasexagintasescentillion-', '-sesexagintasescentillion-', '-septemsexagintasescentillion-', '-octosexagintasescentillion-', '-novemsexagintasescentillion-', '-septuagintasescentillion-', '-unseptuagintasescentillion-', '-duoseptuagintasescentillion-', '-treseptuagintasescentillion-', '-quattourseptuagintasescentillion-', '-quinquaseptuagintasescentillion-', '-seseptuagintasescentillion-', '-septemseptuagintasescentillion-', '-octoseptuagintasescentillion-', '-novemseptuagintasescentillion-', '-octogintasescentillion-', '-unoctogintasescentillion-', '-duooctogintasescentillion-', '-treoctogintasescentillion-', '-quattouroctogintasescentillion-', '-quinquaoctogintasescentillion-', '-seoctogintasescentillion-', '-septemoctogintasescentillion-', '-octooctogintasescentillion-', '-novemoctogintasescentillion-', '-nonagintasescentillion-', '-unnonagintasescentillion-', '-duononagintasescentillion-', '-trenonagintasescentillion-', '-quattournonagintasescentillion-', '-quinquanonagintasescentillion-', '-senonagintasescentillion-', '-septenonagintasescentillion-', '-octononagintasescentillion-', '-novenonagintasescentillion-', '-septingentillion-', '-unseptingentillion-', '-duoseptingentillion-', '-treseptingentillion-', '-quattourseptingentillion-', '-quinquaseptingentillion-', '-seseptingentillion-', '-septemseptingentillion-', '-octoseptingentillion-', '-novemseptingentillion-', '-deciseptingentillion-', '-undeciseptingentillion-', '-duodeciseptingentillion-', '-tredeciseptingentillion-', '-quattourdeciseptingentillion-', '-quinquadeciseptingentillion-', '-sedeciseptingentillion-', '-septemdeciseptingentillion-', '-octodeciseptingentillion-', '-novemdeciseptingentillion-', '-vigintiseptingentillion-', '-unvigintiseptingentillion-', '-duovigintiseptingentillion-', '-tresvigintiseptingentillion-', '-quattourvigintiseptingentillion-', '-quinquavigintiseptingentillion-', '-sesvigintiseptingentillion-', '-septemvigintiseptingentillion-', '-octovigintiseptingentillion-', '-novemvigintiseptingentillion-', '-trigintaseptingentillion-', '-untrigintaseptingentillion-', '-duotrigintaseptingentillion-', '-trestrigintaseptingentillion-', '-quattourtrigintaseptingentillion-', '-quinquatrigintaseptingentillion-', '-sestrigintaseptingentillion-', '-septemtrigintaseptingentillion-', '-octotrigintaseptingentillion-', '-novemtrigintaseptingentillion-', '-quadragintaseptingentillion-', '-unquadragintaseptingentillion-', '-duoquadragintaseptingentillion-', '-tresquadragintaseptingentillion-', '-quattourquadragintaseptingentillion-', '-quinquaquadragintaseptingentillion-', '-sesquadragintaseptingentillion-', '-septemquadragintaseptingentillion-', '-octoquadragintaseptingentillion-', '-novemquadragintaseptingentillion-', '-quinquagintaseptingentillion-', '-unquinquagintaseptingentillion-', '-duoquinquagintaseptingentillion-', '-tresquinquagintaseptingentillion-', '-quattourquinquagintaseptingentillion-', '-quinquaquinquagintaseptingentillion-', '-sesquinquagintaseptingentillion-', '-septemquinquagintaseptingentillion-', '-octoquinquagintaseptingentillion-', '-novemquinquagintaseptingentillion-', '-sexagintaseptingentillion-', '-unsexagintaseptingentillion-', '-duosexagintaseptingentillion-', '-tresexagintaseptingentillion-', '-quattoursexagintaseptingentillion-', '-quinquasexagintaseptingentillion-', '-sesexagintaseptingentillion-', '-septemsexagintaseptingentillion-', '-octosexagintaseptingentillion-', '-novemsexagintaseptingentillion-', '-septuagintaseptingentillion-', '-unseptuagintaseptingentillion-', '-duoseptuagintaseptingentillion-', '-treseptuagintaseptingentillion-', '-quattourseptuagintaseptingentillion-', '-quinquaseptuagintaseptingentillion-', '-seseptuagintaseptingentillion-', '-septemseptuagintaseptingentillion-', '-octoseptuagintaseptingentillion-', '-novemseptuagintaseptingentillion-', '-octogintaseptingentillion-', '-unoctogintaseptingentillion-', '-duooctogintaseptingentillion-', '-treoctogintaseptingentillion-', '-quattouroctogintaseptingentillion-', '-quinquaoctogintaseptingentillion-', '-seoctogintaseptingentillion-', '-septemoctogintaseptingentillion-', '-octooctogintaseptingentillion-', '-novemoctogintaseptingentillion-', '-nonagintaseptingentillion-', '-unnonagintaseptingentillion-', '-duononagintaseptingentillion-', '-trenonagintaseptingentillion-', '-quattournonagintaseptingentillion-', '-quinquanonagintaseptingentillion-', '-senonagintaseptingentillion-', '-septenonagintaseptingentillion-', '-octononagintaseptingentillion-', '-novenonagintaseptingentillion-', '-octingentillion-', '-unoctingentillion-', '-duooctingentillion-', '-tresoctingentillion-', '-quattouroctingentillion-', '-quinquaoctingentillion-', '-sesoctingentillion-', '-septemoctingentillion-', '-octooctingentillion-', '-novemoctingentillion-', '-decioctingentillion-', '-undecioctingentillion-', '-duodecioctingentillion-', '-tredecioctingentillion-', '-quattourdecioctingentillion-', '-quinquadecioctingentillion-', '-sedecioctingentillion-', '-septemdecioctingentillion-', '-octodecioctingentillion-', '-novemdecioctingentillion-', '-vigintioctingentillion-', '-unvigintioctingentillion-', '-duovigintioctingentillion-', '-tresvigintioctingentillion-', '-quattourvigintioctingentillion-', '-quinquavigintioctingentillion-', '-sesvigintioctingentillion-', '-septemvigintioctingentillion-', '-octovigintioctingentillion-', '-novemvigintioctingentillion-', '-trigintaoctingentillion-', '-untrigintaoctingentillion-', '-duotrigintaoctingentillion-', '-trestrigintaoctingentillion-', '-quattourtrigintaoctingentillion-', '-quinquatrigintaoctingentillion-', '-sestrigintaoctingentillion-', '-septemtrigintaoctingentillion-', '-octotrigintaoctingentillion-', '-novemtrigintaoctingentillion-', '-quadragintaoctingentillion-', '-unquadragintaoctingentillion-', '-duoquadragintaoctingentillion-', '-tresquadragintaoctingentillion-', '-quattourquadragintaoctingentillion-', '-quinquaquadragintaoctingentillion-', '-sesquadragintaoctingentillion-', '-septemquadragintaoctingentillion-', '-octoquadragintaoctingentillion-', '-novemquadragintaoctingentillion-', '-quinquagintaoctingentillion-', '-unquinquagintaoctingentillion-', '-duoquinquagintaoctingentillion-', '-tresquinquagintaoctingentillion-', '-quattourquinquagintaoctingentillion-', '-quinquaquinquagintaoctingentillion-', '-sesquinquagintaoctingentillion-', '-septemquinquagintaoctingentillion-', '-octoquinquagintaoctingentillion-', '-novemquinquagintaoctingentillion-', '-sexagintaoctingentillion-', '-unsexagintaoctingentillion-', '-duosexagintaoctingentillion-', '-tresexagintaoctingentillion-', '-quattoursexagintaoctingentillion-', '-quinquasexagintaoctingentillion-', '-sesexagintaoctingentillion-', '-septemsexagintaoctingentillion-', '-octosexagintaoctingentillion-', '-novemsexagintaoctingentillion-', '-septuagintaoctingentillion-', '-unseptuagintaoctingentillion-', '-duoseptuagintaoctingentillion-', '-treseptuagintaoctingentillion-', '-quattourseptuagintaoctingentillion-', '-quinquaseptuagintaoctingentillion-', '-seseptuagintaoctingentillion-', '-septemseptuagintaoctingentillion-', '-octoseptuagintaoctingentillion-', '-novemseptuagintaoctingentillion-', '-octogintaoctingentillion-', '-unoctogintaoctingentillion-', '-duooctogintaoctingentillion-', '-treoctogintaoctingentillion-', '-quattouroctogintaoctingentillion-', '-quinquaoctogintaoctingentillion-', '-seoctogintaoctingentillion-', '-septemoctogintaoctingentillion-', '-octooctogintaoctingentillion-', '-novemoctogintaoctingentillion-', '-nonagintaoctingentillion-', '-unnonagintaoctingentillion-', '-duononagintaoctingentillion-', '-trenonagintaoctingentillion-', '-quattournonagintaoctingentillion-', '-quinquanonagintaoctingentillion-', '-senonagintaoctingentillion-', '-septenonagintaoctingentillion-', '-octononagintaoctingentillion-', '-novenonagintaoctingentillion-', '-nongentillion-', '-unnongentillion-', '-duonongentillion-', '-trenongentillion-', '-quattournongentillion-', '-quinquanongentillion-', '-senongentillion-', '-septenongentillion-', '-octonongentillion-', '-novenongentillion-', '-decinongentillion-', '-undecinongentillion-', '-duodecinongentillion-', '-tredecinongentillion-', '-quattourdecinongentillion-', '-quinquadecinongentillion-', '-sedecinongentillion-', '-septemdecinongentillion-', '-octodecinongentillion-', '-novemdecinongentillion-', '-vigintinongentillion-', '-unvigintinongentillion-', '-duovigintinongentillion-', '-tresvigintinongentillion-', '-quattourvigintinongentillion-', '-quinquavigintinongentillion-', '-sesvigintinongentillion-', '-septemvigintinongentillion-', '-octovigintinongentillion-', '-novemvigintinongentillion-', '-trigintanongentillion-', '-untrigintanongentillion-', '-duotrigintanongentillion-', '-trestrigintanongentillion-', '-quattourtrigintanongentillion-', '-quinquatrigintanongentillion-', '-sestrigintanongentillion-', '-septemtrigintanongentillion-', '-octotrigintanongentillion-', '-novemtrigintanongentillion-', '-quadragintanongentillion-', '-unquadragintanongentillion-', '-duoquadragintanongentillion-', '-tresquadragintanongentillion-', '-quattourquadragintanongentillion-', '-quinquaquadragintanongentillion-', '-sesquadragintanongentillion-', '-septemquadragintanongentillion-', '-octoquadragintanongentillion-', '-novemquadragintanongentillion-', '-quinquagintanongentillion-', '-unquinquagintanongentillion-', '-duoquinquagintanongentillion-', '-tresquinquagintanongentillion-', '-quattourquinquagintanongentillion-', '-quinquaquinquagintanongentillion-', '-sesquinquagintanongentillion-', '-septemquinquagintanongentillion-', '-octoquinquagintanongentillion-', '-novemquinquagintanongentillion-', '-sexagintanongentillion-', '-unsexagintanongentillion-', '-duosexagintanongentillion-', '-tresexagintanongentillion-', '-quattoursexagintanongentillion-', '-quinquasexagintanongentillion-', '-sesexagintanongentillion-', '-septemsexagintanongentillion-', '-octosexagintanongentillion-', '-novemsexagintanongentillion-', '-septuagintanongentillion-', '-unseptuagintanongentillion-', '-duoseptuagintanongentillion-', '-treseptuagintanongentillion-', '-quattourseptuagintanongentillion-', '-quinquaseptuagintanongentillion-', '-seseptuagintanongentillion-', '-septemseptuagintanongentillion-', '-octoseptuagintanongentillion-', '-novemseptuagintanongentillion-', '-octogintanongentillion-', '-unoctogintanongentillion-', '-duooctogintanongentillion-', '-treoctogintanongentillion-', '-quattouroctogintanongentillion-', '-quinquaoctogintanongentillion-', '-seoctogintanongentillion-', '-septemoctogintanongentillion-', '-octooctogintanongentillion-', '-novemoctogintanongentillion-', '-nonagintanongentillion-', '-unnonagintanongentillion-', '-duononagintanongentillion-', '-trenonagintanongentillion-', '-quattournonagintanongentillion-', '-quinquanonagintanongentillion-', '-senonagintanongentillion-', '-septenonagintanongentillion-', '-octononagintanongentillion-', '-novenonagintanongentillion-', '-millinillion-']
  print(c.clear,end='')
  print(c.yellow + '''
#     #                                           ### 
##    # #    # #    # #####  ###### #####   ####  ### 
# #   # #    # ##  ## #    # #      #    # #      ### 
#  #  # #    # # ## # #####  #####  #    #  ####   #  
#   # # #    # #    # #    # #      #####       #     
#    ## #    # #    # #    # #      #   #  #    # ### 
#     #  ####  #    # #####  ###### #    #  ####  ### 
  ''')
  if result == '':
    print(c.base3 + 'Welecome to P.L.E.N.A.C.H:')
    print()
    print(c.base3 + 'The')
    print(c.violet + '      P' + c.base3 + ' reposterously')
    print(c.violet + '      L' + c.base3 + ' arge')
    print(c.violet + '      E' + c.base3 + ' xponential')
    print(c.violet + '      N' + c.base3 + ' umber')
    print(c.violet + '      A' + c.base3 + ' mender for')
    print(c.violet + '      C' + c.base3 + ' ondesendence and')
    print(c.violet + '      H' + c.base3 + ' aughtiness.')
  else:
    print(result)
  number = input(c.blue + '>>> ')
  result = ''
  number = re.sub('[^0-9]','',number)
  number = re.sub('^0*$','0',number)
  number = re.sub('^0+(\\d)','\\1',number)
  if number == '0':
    result = 'zero'
  else:
    triplet = ''
    for digit in number:
      digits += 1
      chopped_number.append(digit)
      
    if digits % 3 == 1:
      triplet += chopped_number.pop(0)
      full_triplets.append(triplet)
    elif digits % 3 == 2:
      triplet += chopped_number.pop(0)
      triplet += chopped_number.pop(0)
      full_triplets.append(triplet)
    
    while chopped_number != []:
      triplet = ''
      for the_magic_number in range(3):
        triplet += chopped_number.pop(0)
      full_triplets.append(triplet)
    
    for baseupper in full_triplets:
      baseup += 1
      
    for word_maker in full_triplets:
      if baseup > 1:
        mid_triplet = get_triplet(word_maker)
        if mid_triplet != '':
          result += mid_triplet + '-' + base_triplets.pop(baseup-2)
        baseup -= 1
      else:
        last_triplet = get_triplet(word_maker)
        if last_triplet != '':
          last_triplet = '-' + last_triplet
        result += last_triplet
    if result.startswith('-'):
      result = result[1:]
    if result.endswith('-'):
      result = result[:-1]
    result = re.sub('-+','-',result)