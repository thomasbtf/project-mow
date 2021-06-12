from drives import Simple_Drive


class First_Robot:
    def __init__(self):
        self.drive = Simple_Drive()

    def move(self, x, y):
        self.drive.move(x, y)
