class garden:
    name=''
    garden=[]
    def __init__(self,name):
        self.name=name
    def create_field(self, x, y):
        for j in range(y):
            self.garden.append([])
            for i in range(x):
                label = "Podaj opis dla (" + str(i) + "," + str(j) + "): "
                self.garden[j].append(input(label))
        return garden

    def show_garden(self):
        row = ''
        y = len(self.garden)
        for j in range(y):
            x = len(self.garden[j])
            for i in range(x):
                row = row + self.garden[j][i] + ','
            row = row[:-1]
            print(row + '\n')
            row = ''