# Thought process:
# - We must iterate over elements finding their boiling point and acceptable range
# - Element's bioling point with the smallest difference is the match
# - If no elements match then the closest match will be "Unknown" by default
# - Return the closest match

def boiling_material(boiling_map, boiling_point):

    # Default for closest element and difference between it's boiling point and the given one
    smallest_difference = 999999
    closest = "Unknown"
    
    # Iterate over elements in the boiling map
    for element in boiling_map:

        # Max difference between a matching element's boiling point and given one is 5% of element's bp
        element_bp = boiling_map[element]
        max_difference = round(abs(element_bp) * 0.05, 9)

        # Find the difference between given and element's boiling point
        difference = round(abs(element_bp - boiling_point), 9)

        # If it is within acceptable range, find if it has smallest difference
        if difference <= max_difference:
            if difference <= smallest_difference:

                # If it has smallest difference, then it is the closest
                smallest_difference = difference
                closest = element
        
    return closest