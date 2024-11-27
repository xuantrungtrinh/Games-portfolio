# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # ==> Well, we can define a class, let's call it Fish, and it has an initializer. Now in order to get this Fish class to inherit from another class, all we have to do is to add a set of parentheses after the name of the class and then provide the class that we want to inherit from. So in this case our fish is inheriting from the animal class. And then in order to get a hold of everything that an animal has and is, so its attributes and methods, all we have to do is inside the init, add this super().__init__(). And the super refers to the superclass. So basically, initialize everything that the superclass can do in our fish
                            # ==> also, now what these two parts of the code does is it allows anything that's created from my fish class to inherit all of the attributes and methods from the superclass, which is the animal class.
                            # ==> now my object that's created from the Fish class now has access to all the attributes and methods from the superclass that inherited from the animal class.
    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe()
        # ==> But what if I wanted to modify it a little bit? So for example, a fish does, in fact, breathe, but it kind of breathes underwater. So let's say I want to define the breathe function and I wanted to have the same functionality as the superclass which I'm inheriting from. So I want to print inhale, exhale, but I also want to do something extra. Well, in this case, we would get hold of the superclass and then call breathe on it. This means we're going to do everything that the breathe method from the superclass does, so all of this, but afterwards we're going to do something a little bit more special.
        print("doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)



