class Animal: 
    def _init_(self):
        self.num_eyes = 2
    def breath(self):
        print("Inhale, exhale")
    
class Fish: 
    def __init__(self):
        super().__init__()
        

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num.eyes)