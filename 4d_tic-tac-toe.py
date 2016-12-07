# A four-dimensional tic-tac-toe
# Copyright Mika "AgenttiX" Mäki, 2015

# This program is one of my earliest creations and is thereby unfortunately in Finnish.


# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
Neliulotteinen ristinolla
TIE-02100 HT7
Mika Mäki

Neliulotteinen ristinolla on tavallisen ristinollan laajennus. Heurekan
katossa on kolmiulotteinen versio (3x3x3), jossa tehtävänä on muodostaa suora
viiva kuution läpi. Tässä tehtävänä on samoin muodostaa suora viiva, mutta
käytettävissä on useampia ruudukoita. Yksittäisessä ruudukossa peli tietysti
käyttäytyy kuten tavallinen ristinolla.

Pelin hahmottamista helpottaa, jos kuvittelet pinoavasi käyttämäsi
ruudukkolinjan kuutioksi ja yrität piirtää suoraa sen läpi. Lisäksi netistä
löytyy esimerkkikuvia hakusanalla four-dimensional tic-tac-toe.

3x3x3x3-esimerkkejä:
VY-ruudukon VY + K-ruudukon K + OA-ruudukon OA = viiva
KY-ruudukon K + K-ruudukon K + KA-ruudukon K = viiva
VY-ruudukon VA + KV-ruudukon KA + VA-ruudukon OA = viiva

Esimerkkien lyhenteet:
VY = vasen ylä
K = keski
KY = keski ylä
KV = keski vasen
OA = oikea ala

Osa riveistä on koodin luettavuuden vuoksi jätetty ylipitkiksi
"""


from tkinter import *
from tkinter.messagebox import showerror


class Kysely:
    """ Kyselyikkunaa kuvaava luokka """
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Neliulotteinen ristinolla")
        self.__ikkuna.resizable(width=FALSE, height=FALSE)

        # Alustetaan muuttujat

        self.__ruudukon_kokovalinta = IntVar()  # Tkinter halusi tällaisen
        self.ruudukon_koko = 0

        self.__ruudun_kokovalinta = IntVar()
        self.ruudun_koko = 0

        self.__x_varivalinta = StringVar()
        self.__o_varivalinta = StringVar()
        self.x_vari = ""
        self.o_vari = ""

        self.vastattu = False

        # Luodaan kyselyikkunan elementit

        self.__ruudukkoteksti = Label(self.__ikkuna)
        self.__ruudukkoteksti.configure(text="Valitse ruudukon koko (suositeltava 3-4) \n 1-2-kokoisena X voittaa aina säännöistä johtuen \n ja 5-kokoinen tuskin mahtuu näytölle")
        self.__ruudukkoteksti.grid(row=0, column=0)

        self.__ruudukkovaihtoehdot = []
        for n in range(1,6):
            valintanappi = Radiobutton(self.__ikkuna, text=n, variable=self.__ruudukon_kokovalinta, value=n)
            valintanappi.grid(row=n, column=0)
            self.__ruudukkovaihtoehdot.append(valintanappi)
        self.__ruudukkovaihtoehdot[2].select()

        self.__nappi = Button(self.__ikkuna, text="Käynnistä", command=self.tarkista)
        self.__nappi.grid(row=6, column=0)

        self.__ruututeksti = Label(self.__ikkuna)
        self.__ruututeksti.configure(text="Valitse yksittäisen ruudun koko \n Pienemmällä arvolla saat suuremman pelikentän näytölle")
        self.__ruututeksti.grid(row=0, column=1)

        self.__ruutuvaihtoehdot = []
        for n in range(1,4):
            valintanappi = Radiobutton(self.__ikkuna, text=n, variable=self.__ruudun_kokovalinta, value=n)
            valintanappi.grid(row=n, column=1)
            self.__ruutuvaihtoehdot.append(valintanappi)
        self.__ruutuvaihtoehdot[1].select()

        varit = ["red", "green", "blue"]
        varinimet = ["punainen", "vihreä", "sininen"]

        self.__x_variteksti = Label(self.__ikkuna, text="X:n väri")
        self.__x_variteksti.grid(row=0, column=2)

        self.__x_varivaihtoehdot = []
        for n in range(3):
            valintanappi = Radiobutton(self.__ikkuna, text=varinimet[n], variable=self.__x_varivalinta, value=varit[n])
            valintanappi.grid(row=n+1, column=2)
            self.__x_varivaihtoehdot.append(valintanappi)
        self.__x_varivaihtoehdot[2].select()

        self.__o_variteksti = Label(self.__ikkuna, text="O:n väri")
        self.__o_variteksti.grid(row=0, column=3)

        self.__o_varivaihtoehdot = []
        for n in range(3):
            valintanappi = Radiobutton(self.__ikkuna, text=varinimet[n], variable=self.__o_varivalinta, value=varit[n])
            valintanappi.grid(row=n+1, column=3)
            self.__o_varivaihtoehdot.append(valintanappi)
        self.__o_varivaihtoehdot[0].select()

        self.__ikkuna.mainloop()

    def tarkista(self):
        """ Tarkistaa syötteiden kelvollisuuden. Lisäksi se asettaa olion
        ulkopuolelle näkyvät kyselyn tulokset ja sulkee ikkunan, mikäli
        syötteet ovat kunnossa"""
        if self.__ruudukon_kokovalinta.get() == 5 and self.__ruudun_kokovalinta.get() == 3:
            showerror("Varoitus!", "Ikkuna voi olla varsin suuri!")
            # Kyseessä ei kuitenkaan ole keskeyttämisen arvoinen virhe
            # return
        if self.__x_varivalinta.get() == self.__o_varivalinta.get():
            showerror("Virhe", "Pelaajat eivät voi olla saman värisiä!")
            return
        self.ruudukon_koko = int(self.__ruudukon_kokovalinta.get())
        self.ruudun_koko = int(self.__ruudun_kokovalinta.get())
        self.x_vari = str(self.__x_varivalinta.get())
        self.o_vari = str(self.__o_varivalinta.get())
        self.vastattu = True
        self.__ikkuna.destroy()


class Peli:
    """ Peli-ikkunaa kuvaava luokka (joka kutsuu kyselyikkunaa)"""
    def __init__(self):
        self.__kysely = Kysely()
        if not self.__kysely.vastattu:
            return
        self.__koko = self.__kysely.ruudukon_koko
        self.__ruudun_koko = self.__kysely.ruudun_koko
        self.__x_vari = self.__kysely.x_vari
        self.__o_vari = self.__kysely.o_vari

        self.__ikkuna = Tk()
        self.__ikkuna.title("Neliulotteinen ristinolla")
        self.__ikkuna.resizable(width=FALSE, height=FALSE)

        # Alustetaan muuttujat ja tietorakenteet
        self.__pelialue = []
        self.__ruudukko = []
        self.__vuoro = 0
        self.__xvoittamassa = False

        # Luodaan ruudukot y-suunnassa
        for ry in range(self.__koko):
            # Luodaan ruudukot x-suunnassa
            self.__pelialue.append([])
            self.__ruudukko.append([])
            for rx in range(self.__koko):
                # Luodaan y-suunta
                self.__pelialue[ry].append([])
                self.__ruudukko[ry].append([])
                for y in range(self.__koko):
                    # Luodaan x-suunta
                    self.__pelialue[ry][rx].append([])
                    self.__ruudukko[ry][rx].append([])
                    for x in range(self.__koko):
                        # Painettaessa ruutu välittää muuta_tila()-metodille omat koordinaattinsa
                        uusi_ruutu = Button(self.__ikkuna, command=lambda lry=ry,lrx=rx,ly=y,lx=x: self.muuta_tila(lry,lrx,ly,lx))
                        uusi_ruutu.grid(row=ry*(self.__koko+1)+y, column=rx*(self.__koko+1)+x)
                        self.__pelialue[ry][rx][y].append(uusi_ruutu)
                        self.__ruudukko[ry][rx][y].append("")

        # Erotetaan ruudukot toisistaan
        for y in range(self.__koko-1):
            for x in range(self.__koko-1):
                erotin = Label(self.__ikkuna)
                erotin.configure(text="   ")
                erotin.grid(row=self.__koko+y*(self.__koko+1), column=self.__koko+x*(self.__koko+1))

        # Luodaan muut käyttöliittymäelementit
        Button(self.__ikkuna, text="Nollaa peli", command=self.alusta_peli).grid(column=0, columnspan=3, row=self.__koko*self.__koko+self.__koko-1)
        self.__infoteksti = Label(self.__ikkuna)
        self.__infoteksti.configure(text="Aloitetaan!")
        self.__infoteksti.grid(column=3, columnspan=6, row=self.__koko*self.__koko+self.__koko-1)

        self.alusta_peli()
        self.__ikkuna.mainloop()

    def alusta_peli(self):
        self.__vuoro = 0
        self.__xvoittamassa = False
        self.__infoteksti.configure(text="Pelaajan X vuoro")
        # Nollataan ruudut
        for ry in range(self.__koko):
            for rx in range(self.__koko):
                for y in range(self.__koko):
                    for x in range(self.__koko):
                        self.__pelialue[ry][rx][y][x].configure(state=NORMAL, text="-", background="grey", height=self.__ruudun_koko, width=self.__ruudun_koko)
                        self.__ruudukko[ry][rx][y][x] = ""

    def lukitse_pelialue(self):
        for ry in range(self.__koko):
            for rx in range(self.__koko):
                for y in range(self.__koko):
                    for x in range(self.__koko):
                        self.__pelialue[ry][rx][y][x].configure(state=DISABLED)

    def muuta_tila(self, ry, rx, y, x):
        """ Muuttaa ruudukon värin ja tarkistaa voittotilanteen
        :param ry: ruudukon y-koordinaatti
        :param rx: ruudukon x-koordinaatti
        :param y: ruudun y-koordinaatti
        :param x: ruudun x-koordinaatti
        :return:
        """
        # X on parillinen ja O pariton
        if self.__vuoro % 2 == 0:
            self.__pelialue[ry][rx][y][x].configure(state=DISABLED, text="X", background=self.__x_vari)
            pelaaja = "X"
            self.__ruudukko[ry][rx][y][x] = pelaaja
            self.__infoteksti.configure(text="Pelaajan O vuoro")
        else:
            self.__pelialue[ry][rx][y][x].configure(state=DISABLED, text="O", background=self.__o_vari)
            pelaaja = "O"
            self.__ruudukko[ry][rx][y][x] = pelaaja
            self.__infoteksti.configure(text="Pelaajan X vuoro")
        # print("Nappia painettu: ", ry, rx, y, x)

        self.__vuoro += 1

        # Voiton tarkistus eli puhdas autismi alkaa tästä
        # Algoritmi kulkee viivaa neliulotteisessa avaruudessa molempiin
        # suuntiin ja mittaa sen pituuden

        # Algoritmi siis kokeilee kaikki mahdolliset akselit ja kulkee
        # niitä molempiin suuntiin

        # Todettakoon, että kehitin sen itse tätä peliä varten

        # print("Testataan voitto")
        # dry, drx dy ja dx ovat koordinaattien muutoksia
        for dry in [-1, 0, 1]:
            for drx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        # print("Mennään suuntaan", dry, drx, dy, dx)

                        # Ruutua itseään ei arvioida
                        if dry != 0 or drx != 0 or dy != 0 or dx != 0:

                            etenema = 0
                            dry2, drx2, dy2, dx2 = dry, drx, dy, dx
                            while True:
                                # print("Kokeillaan pistettä", ry+dry2, rx+drx2, y+dy2, x+dx2)
                                # Tarkistetaan, ettei piste ole ulkona alueelta
                                if ry+dry2 >= self.__koko or rx+drx2 >= self.__koko or y+dy2 >= self.__koko or x+dx2 >= self.__koko or ry+dry2 < 0 or rx+drx2 < 0 or y+dy2 < 0 or x+dx2 < 0:
                                    # print("Ulkona alueelta")
                                    break
                                # Tarkistetaan, onko piste eri väriä
                                elif self.__ruudukko[ry+dry2][rx+drx2][y+dy2][x+dx2] != pelaaja:
                                    # print("Ei ollut samaa")
                                    break
                                else:
                                    # print("Oli samaa -> jatketaan suoraan")
                                    # Siirrytään suoran seuraavaan pisteeseen
                                    if dry2 > 0:
                                        dry2 += 1
                                    elif dry2 < 0:
                                        dry2 -= 1
                                    if drx2 > 0:
                                        drx2 += 1
                                    elif drx2 < 0:
                                        drx2 -= 1
                                    if dy2 > 0:
                                        dy2 += 1
                                    elif dy2 < 0:
                                        dy2 -= 1
                                    if dx2 > 0:
                                        dx2 += 1
                                    elif dx2 < 0:
                                        dx2 -= 1

                                    etenema += 1

                            # print("Pakitetaan")
                            dry2, drx2, dy2, dx2 = dry, drx, dy, dx
                            pakitus = 0
                            while True:
                                # Tarkistetaan, ettei piste ole ulkona alueelta
                                if ry-dry2 < 0 or rx-drx2 < 0 or y-dy2 < 0 or x-dx2 < 0 or ry-dry2 >= self.__koko or rx-drx2 >= self.__koko or y-dy2 >= self.__koko or x-dx2 >= self.__koko:
                                    # print("Ulkona alueelta")
                                    break
                                # Tarkistetaan, onko piste eri väriä
                                elif self.__ruudukko[ry-dry2][rx-drx2][y-dy2][x-dx2] != pelaaja:
                                    # print("Ei ollut samaa")
                                    break
                                else:
                                    # print("Oli samaa -> jatketaan suoraan")
                                    # Siirrytään suoran seuraavaan pisteeseen
                                    if dry2 > 0:
                                        dry2 += 1
                                    elif dry2 < 0:
                                        dry2 -= 1
                                    if drx2 > 0:
                                        drx2 += 1
                                    elif drx2 < 0:
                                        drx2 -= 1
                                    if dy2 > 0:
                                        dy2 += 1
                                    elif dy2 < 0:
                                        dy2 -= 1
                                    if dx2 > 0:
                                        dx2 += 1
                                    elif dx2 < 0:
                                        dx2 -= 1

                                    pakitus += 1
                            # print("Löytyi viiva, jonka pituus on:", etenema+pakitus+1)

                            # Jos pelaajalla on voittava suora
                            if etenema + pakitus +1 == self.__koko:
                                if pelaaja == "X":
                                    self.__xvoittamassa = True
                                    # Spoiler alert
                                    # self.__infoteksti.configure(text="X on voittamassa!")
                                    return
                                elif self.__xvoittamassa:
                                    self.__infoteksti.configure(text="Tasapeli")
                                    self.lukitse_pelialue()
                                    return
                                else:
                                    self.__infoteksti.configure(text="Pelaaja O voitti!")
                                    self.lukitse_pelialue()
                                    return

        if self.__xvoittamassa:
                self.__infoteksti.configure(text="Pelaaja X voitti!")
                self.lukitse_pelialue()
                return


def main():
    Peli()


main()
