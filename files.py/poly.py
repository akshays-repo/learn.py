class parrot:
    def __init__(self):
        pass
    def fly(self):
        print("flying parrot")
class pigeon:
    def __init__(self):
        pass
    def fly(self):
        print("flying pigeon")

def flying(bird):
    bird.fly()
    
pa=parrot()
pg=pigeon()

flying(pa)
flying(pg)

