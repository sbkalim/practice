class Human:
    def __init__(self, n, o):
        self.name= n
        self.occ= o
    def do_work(self):
        if self.occ== "tennis player":
            print(self.name, " Plays Tennis")
        elif self.occ=="actor":
            print(self.name, " Shoots a film")
    def speaks(self):
        print(self.name, " Says, How are you????")


tom=Human('Tom cruise', 'actor')
tom.do_work()
tom.speaks()