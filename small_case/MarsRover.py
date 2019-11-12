class MarsRover(object):
    def __init__(self, length: int, width: int, position: tuple, oriented: str):
        self.area_length = length
        self.area_width = width
        self.position_x = position[0]
        self.position_y = position[1]
        # how to display oriented
        self.oriented = oriented

    def move(self, f_or_b: str):
        """
                         N
                         ^
                         |
                         |
                         |
    W                    |
    ---------------------|--------------------------> E
                         |
                         |
                         |
                         S
        """
        if self.oriented in ("E", "W"):
            if (f_or_b == 'f' and self.oriented == "E") or (f_or_b == 'b' and self.oriented == "W"):
                self.position_x += 1
            else:
                self.position_x -= 1
        else:
            if (f_or_b == 'f' and self.oriented == "N") or (f_or_b == 'b' and self.oriented == "S"):
                self.position_y += 1
            else:
                self.position_y -= 1

        return self.position_x, self.position_y

    def turn(self, direct: str):
        direct_list = ["E", "S", "W", "N"]
        oriented_ind = direct_list.index(self.oriented)
        if direct == "l":
            self.oriented = direct_list[oriented_ind-1]
        else:
            new_ind = oriented_ind + 1
            if new_ind > 4:
                new_ind = 0
            self.oriented = direct_list[new_ind]

        return self.oriented

