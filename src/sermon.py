class Sermon():
    def __init__(self, date, book, passage, url, speaker):
        self.date = date
        self.book = book
        self.passage = passage
        self.url = url
        self.speaker = speaker
        # print(self.date, self.book, self.passage, self.url, self.speaker)


class SermonDatabase():
    def __init__(self):
        self.sermon_list = []

    def add_sermon(self, sermon):
        self.sermon_list.append(sermon)
        print(self.sermon_list)


# ----------------------------------------------------------------------------------------------------
print('working')
Sermon1 = Sermon("1-3 JAN 2026", "Deuteronomy", "24:14-22",
                 "youtu.be/pFpdztW09H4?si=L2qI-L3A3EuE119c", "李思敬博士")
Sermon2 = Sermon("12-13 JAN 2026", "Deuteronomy", "30:11-20",
                 "wtccc.ca/sermons.php?select=2&sermfile=sermons-2006.dat", "李思敬博士")
Sermon3 = Sermon("19-20 JAN 2026", "Deuteronomy", "34:1-12",
                 "wtccc.ca/sermons.php?select=2&sermfile=sermons-2006.dat", "李思敬博士")

database = SermonDatabase()
database.add_sermon(Sermon1)
database.add_sermon(Sermon2)
database.add_sermon(Sermon3)
