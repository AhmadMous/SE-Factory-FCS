# Thought process:
# - We need to keep track of values of the greatest distance and pair of points creating it
# - To find all possibilities, we find the distance between every possible combination of points
# - Note: This is very unoptimized and inefficient, since many calculations would be repeated
# without gain, for example (5, 2) and (6, 3) are recalculated as (6, 3) and (5, 2)

def find_farthest_points(points):
    
    # Hold pair of points with greatest distance between them, and the distance
    farthest_pair = []
    farthest = 0
    
    # Compare every point in the list, with every other point in the list
    for point1 in points:
        for point2 in points:

            # No distance between the same point and itself
            if point1 == point2:
                continue
                
            # Find the distance between the 2 points
            x_difference = point2[0] - point1[0]
            y_difference = point2[1] - point1[1]

            distance = (x_difference ** 2 + y_difference ** 2) ** 0.5

            # If the distance is greater than previous farthest pair, update the values
            if distance > farthest:
                farthest = distance
                farthest_pair = [point1, point2]
            
    return farthest_pair
    pass
