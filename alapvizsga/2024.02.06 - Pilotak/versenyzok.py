from versenyzo import Versenyzo
import math

versenyzo_lista: list[Versenyzo] = []

def main():
    load_from_file('pilotak.csv')
    print(f'3. feladat: {len(versenyzo_lista)}')
    print(f'4. feladat {versenyzo_lista[-1].nev}')
    korabban_szuletett_mint(1901)
    print(f'6.feladat: {legkisebb_rajtszam().nemzetiseg}')
    rajtszam_statisztika()

def load_from_file(filename: str):
    file = open(filename, 'r', encoding= 'utf8')
    file.readline()
    for sor in file:
        versenyzo_lista.append(Versenyzo(sor.strip()))
    file.close()


def korabban_szuletett_mint(ev: int):
    for v in versenyzo_lista:
        if v.szuletesi_ev < ev:
            print(f'\t{v.nev} ({v.szuletes})')

def legkisebb_rajtszam() -> Versenyzo:
    legkisebb_versenyzo = None
    legkisebb_rajtszam_ = math.inf
    for v in versenyzo_lista:
        if v.rajtszam != '' and int(v.rajtszam) < legkisebb_rajtszam_:
            legkisebb_rajtszam_ = int(v.rajtszam)
            legkisebb_versenyzo = v
    return legkisebb_versenyzo

def rajtszam_statisztika():
    stat = {}
    for v in versenyzo_lista:
        if v.rajtszam in stat.keys():
            stat[v.rajtszam] += 1
        else:
            stat[v.rajtszam] = 1
    print('7. feladat:', end=' ')
    for key,value in stat.items():
        if key != '' and value > 1:
            print(key, end= ", ")

main()