from sport import *
import os

def main():
    os.system('cls')
    load_from_file('helsinki.txt')
    print('3. feladat')
    print(f'\tPontszerző helyezések száma: {counting_placements()}')
    print('4. feladat')
    print(f'\tArany: {gold()}')
    print(f'\tEzüst: {silver()}')
    print(f'\tBronz: {bronze()}')
    print(f'\tÖsszesen: {bronze()+gold()+silver()}')
    print('5. feladat')
    print(f'\tOlimpiai pontok száma: {point_counter()}')
    print('6.feladat')
    if torna_or_uszas() == 1:
        print('\tÚszás sportágban szereztek több érmet')
    elif torna_or_uszas() == 2:
        print('\tTorna sportágban szereztek több érmet')
    elif torna_or_uszas() == 3:
        print('\tEgyenlő volt az érmek száma')
    print('8. feladat')
    print(f'\tHelyezés: {most_players().placement}')
    print(f'\tSportág: {most_players().sport}')
    print(f'\tVersenyszám: {most_players().type}')
    print(f'\tSportolók száma: {most_players().number}')
main()
