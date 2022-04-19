# Thought process:
# - We need to find any pattern to help us navigate our way around the grid
# - We can notice the grid can be broken down into rings
# - We notice we can calculate spiral index of bottom right corner of any ring, the anchor point
# - You can imagine a to be anchor point of a ring around o:
#   xxx
#   xox
#   xxa
# - We can then walk along the 4 directions to find coordinates we want and get their spiral index
# Note: This can be solved directly without iteration by grabbing (x, - distance) index, then calculating (x, y) but I'm too lazy

def spiral_index(x, y):

    # The farthest component of the coordinates of the point, to find out "ring" it belongs to
    distance = max(abs(x), abs(y))

    # Coordinates of anchor point of relevant ring
    coordinates = (distance, -distance)

    # Incrementation settings of index coordinates  as we iterate through the ring
    increments = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # List of spiral indices of anchor points (where y = -x aka (x, -x)) for rings
    anchorsv = [0]
    for i in range(1, distance + 1):
        anchorsv.append(anchorsv[i - 1] + i * 8)

    # Spiral index of anchor point, we will iterate from it
    index = anchorsv[distance]

    # We intend to proceed along the 4 lines
    for corner in range(4):

        # Setting direction of coordinates incrementation
        increment = increments[corner]

        # Iterate over all points of that line, then change direction to stay on ring
        for i in range(distance * 2):

            # We reach intended coordinates coordinates
            if coordinates == (x, y):
                print("Spiral index of", (x, y), "is", str(index) + ".")
                return index

            # No match, decrement index, and update coordinates
            else:
                index -= 1
                coordinates = (coordinates[0] + increment[0], coordinates[1] + increment[1])