class Sport:
    def __init__(self, row:str) -> None:
        #1 1 atletika kalapacsvetes
        splitted = row.split(' ')
        self.placement = int(splitted[0])
        self.number = int(splitted[1])
        self.sport = splitted[2]
        self.type = splitted[3].strip()
