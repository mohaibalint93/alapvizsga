from sports import Sport

data : list[Sport] = []

def load_from_file(filename: str) -> bool:
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        data.append(Sport(row))
    file.close()
    return True

def counting_placements():
    counter = 0
    for c in data:
        if c.placement <= 6:
                counter += 1
    return counter

def gold():
    counter = 0
    for c in data:
        if c.placement == 1:
                counter += 1
    return counter

def silver():
    counter = 0
    for c in data:
        if c.placement == 2:
                counter += 1
    return counter

def bronze():
    counter = 0
    for c in data:
        if c.placement == 3:
                counter += 1
    return counter

def point_counter():
    points = 0
    for c in data:
        if c.placement == 1:
            points += 7
        if c.placement == 2:
            points += 5
        if c.placement == 3:
            points += 4
        if c.placement == 4:
            points += 3
        if c.placement == 5:
            points += 2
        if c.placement == 6:
            points += 1
    return points

def torna_or_uszas():
    torna_count = 0
    uszas_count = 0
    for c in data:
        if c.sport == 'torna':
            if c.placement == 1 or c.placement == 2 or c.placement == 3:
                torna_count += 1
        elif c.sport == 'uszas':
            if c.placement == 1 or c.placement == 2 or c.placement == 3:
                uszas_count += 1
    if uszas_count > torna_count:
        return 1
    elif uszas_count < torna_count:
        return 2
    else:
        return 3
        
def most_players() -> Sport|None:
    number_of_players = 0
    sport = None
    for c in data:
        if c.placement <= 6:
            if c.number > number_of_players:
                number_of_players = c.number
                sport = c
    return sport
          