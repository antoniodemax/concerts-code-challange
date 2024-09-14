class Concert:
    def __init__(self, band_name, band_hometown, venue_city):
        self.band_name = band_name
        self.band_hometown = band_hometown
        self.venue_city = venue_city

    def hometown_show(self):
        #checks if the concert is in the bands hometown
        return self.band_hometown.lower() == self.venue_city.lower()

    def introduction(self):
        return f"Hello {self.venue_city}!!!!! We are {self.band_name} and we're from {self.band_hometown}"  

#example
concert = Concert("The Beatles", "London", "New York")
print(concert.introduction())
print(concert.hometown_show())     
        