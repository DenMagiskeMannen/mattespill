# Teodor sitt mattespill
# Copyright (C) 2016 Teodor Solbu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Attributions:
# Error sound 'Error' by Autistic Lucario - https://freesound.org/people/Autistic%20Lucario/sounds/142608/
# Correct sound 'correct' - by 'ertfelda' - https://www.freesound.org/people/ertfelda/sounds/243701/

import os
import winsound as ws
from random import randint


#Teodor matte oppgave
#

print("Teodor sitt mattespill!")
print("Hei!")
print("")

# spør hvor mange oppgaver
antallOppgaver = int(input("Hvor mange oppgaver? "))

print("Du får nå " + str(antallOppgaver) + " oppgaver!")

oppgaverGjort = 0
retteSvar = 0
feilSvar = 0

rettlyd ="rett.wav"
feillyd ="feil.wav"


while oppgaverGjort < antallOppgaver:
    # gi matteoppgaver
    tall1 = randint(1,10)
    tall2 = randint(1,10)

    svar = int(input("hvor mye er " + str(tall1) + " * " + str(tall2) + "? "))

    # Fortelle om svaret var rett eller galt
    if svar == tall1*tall2:
        print("RIKTIG!!!!")
        ws.PlaySound(rettlyd,ws.SND_ASYNC)

        retteSvar = retteSvar + 1
    else:
        print("GALT")
        ws.PlaySound(feillyd,ws.SND_ASYNC)
        feilSvar += 1

    oppgaverGjort = oppgaverGjort + 1
    # huske hvor mange som er rett og galt

# vise hvor mange rett og hvor mange galt svar
print("Du fikk "+str(retteSvar)+" av "+str(antallOppgaver)+" rett!")
print("")


# ikke avslutt før du er klar
os.system('pause')
