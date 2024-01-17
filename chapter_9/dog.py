class Dog():
    """a simple attempt at dog modelling"""
    def __init__(self, name, age):
        """Initialisation of the name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulation that the dog sits down after receiving a command"""
        print(f"{self. name.titile()} now is sitting")

    def roll_over(self):
        """simulation that the dog lies on its back when commanded"""
        print(f"{self.name.title()} now is lies on its back")

