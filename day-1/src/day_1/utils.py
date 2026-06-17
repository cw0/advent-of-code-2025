def left(current_value, distance):
    temp_value = current_value - distance
    rotations = 0
    while (temp_value < 0):
        temp_value += 100
        rotations += 1
        
    temp_rotations = rotations if current_value != 0 else rotations - 1

    if temp_value == 0:
        temp_rotations += 1

    return (temp_value, temp_rotations)

def right(current_value, distance):
    temp_value = current_value + distance
    rotations = 0
    while (temp_value > 99):
        temp_value -= 100
        rotations += 1
    return (temp_value, rotations)