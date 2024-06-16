class Peak:
    def __init__(self,row) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.mountain = splitted[1]
        self.height = int(splitted[2])
        self.height_foot = 3.280839895 * self.height