class Snake:
    length = 0
    score = 0
    def __init__(self,pos) -> None:
        self.positions = [pos]
        self.direction = "right"