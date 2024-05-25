MAPART_SIZE = 128


class Coordinate:

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


x, z = input("Enter the size for example: ").split()
row = int(x)
colunm = int(z)

x, y, z = input(
    "Enter the above Northeast coordinate of the mapart on the noobline. "
).split()
orgin = Coordinate(int(x), int(y), int(z))

northeast = Coordinate(orgin.x, orgin.y, orgin.z)
southwest = Coordinate(orgin.x + MAPART_SIZE - 1, orgin.y + 1, orgin.z + MAPART_SIZE)

for i in range(row):
    northeast.z = orgin.z
    southwest.z = orgin.z + MAPART_SIZE - 1

    for j in range(colunm):
        print("piece:", i, j)
        if j == 0:  # we already did the work above
            print(northeast.x, southwest.x)
            print(northeast.y, southwest.y)
            print(northeast.z, southwest.z)
            print()
            continue

        northeast.z += MAPART_SIZE
        southwest.z += MAPART_SIZE

        print(northeast.x, southwest.x)
        print(northeast.y, southwest.y)
        print(northeast.z, southwest.z)
        print()

    northeast.x += MAPART_SIZE
    southwest.x += MAPART_SIZE
