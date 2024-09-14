class Concert:
    def __init__(self, name, venue):
        self.name = name
        self.venue = venue

class Band:
    def __init__(self, name):
        self.name = name
        self.concerts_list = []

    def add_concert(self, concert):
        self.concerts_list.append(concert)

    def concerts(self):
        return [concert.name for concert in self.concerts_list]

    def venues(self):
        return list(set(concert.venue for concert in self.concerts_list))
    

#example
band = Band("The Rockers")
band.add_concert(Concert("Jazz session", "Nairobi"))
band.add_concert(Concert("Winter Jam", "Mombasa"))
band.add_concert(Concert("Ladies Night", "Kisumu"))

print(band.concerts())
print(band.venues())
    
        

        