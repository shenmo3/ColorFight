import colorfight


class Mainbody:
    def __init__(self):
        pass

    #detect and return all attackable cell
    def detect(self):
        attackable = []
        for x in range(g.width):
            for y in range(g.height):
                c = g.GetCell(x, y)
                #first store all own cell inside the list
                if c.owner == g.uid:
                    adjacent1 = g.GetCell(x + 1, y)
                    adjacent2 = g.GetCell(x - 1, y)
                    adjacent3 = g.GetCell(x, y + 1)
                    adjacent4 = g.GetCell(x, y - 1)
                    if adjacent1.owner != g.uid and not ([x + 1,y] in attackable):
                        attackable.append([x + 1,y])
                    if adjacent2.owner != g.uid and not ([x - 1,y] in attackable):
                        attackable.append([x - 1,y])
                    if adjacent3.owner != g.uid and not ([x,y + 1] in attackable):
                        attackable.append([x,y + 1])
                    if adjacent4.owner != g.uid and not ([x,y - 1] in attackable):
                        attackable.append([x,y - 1])
        return attackable

    # calculate and return a list of most valuable cells
    # append this for future function updates
    def calculate(self):
        pass

    # choose the closest and most valuable cell
    # calculate an attackable cell that is closest to that cell and return it
    def optimal(self):
        pass

    def attack(self):
        pass



g = colorfight.Game()
g.JoinGame('DBN_niubi')
m = Mainbody()
while True:
    m.detect()
    #m.attack()
    g.Refresh()