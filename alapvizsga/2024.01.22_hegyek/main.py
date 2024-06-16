from peaks import *

def main():
    load_from_file('hegyekMO.txt')
    print(f'3. feladat: Hegycsúcsok száma: {len(list_of_peaks)} darab')
    print(f'4. feladat: Hegyek magasságának átlaga: {avg_height()} m')
    print(f'A legmagasabb hegycsúcs adatai: ')
    highest = highest_peak()
    print(f'\tNév: {highest.name}')
    print(f'\tHegység: {highest.mountain}')
    print(f'\tMagasság: {highest.height}')
    height = int(input('6.feladat: kérek egy magasságot '))
    if exists_higher(height):
        print(f'Van {height} méternél magasabb hegycsúcs.')
    else:
        print(f'Nincs {height} méternél magasabb hegycsúcs.')

    search_result = search_first_higher(height)
    if search_result != None:
        print(f'Van {height} méternél magasabb hegycsúcs: {search_result.name}')
    else:
        print(f'Nincs {height} méternél magasabb hegycsúcs.')
    
    print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {count_in_foot(3000)}')
    print('9. feladat: bukk-videk.txt')
    write_to_file('Bükk-vidék', 'bukk-videk.txt')

main()