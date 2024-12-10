class Robot:
    def __init__(self, name, type, job):
        self.name = name
        self.type = type
        self.job = job

    def introduce(self):
        return f"Hi, I am {self.name}. I am a {self.type} robot. My job is {self.job}."

    def features(self, abilities):
        ability_list = ", ".join(abilities)
        return f"I can do the following: {ability_list}."

my_robot = Robot("Robo", "a mathematic solver", "making you love mathematics")
print(my_robot.introduce())

abilities = ["scan question", "talk", "Solve questions"]
print(my_robot.features(abilities))
