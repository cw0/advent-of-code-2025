
# this is a circularly linked list problem first we need to define how to move in our circularly linked list

# just to save time later the run command is uv run main.py from the day-1 directory
   
def left(current_value, distance):
    temp_value = current_value - distance
    rotations = 0
    while (temp_value < 0):
        temp_value += 100
        rotations += 1
    return (temp_value, rotations)

def right(current_value, distance):
    temp_value = current_value + distance
    rotations = 0
    while (temp_value > 99):
        temp_value -= 100
        rotations += 1
    return (temp_value, rotations)

def main():
    current_value = 50
    zero_count = 0

    with open("input", "r") as file:
        directions = file.readlines()
        print('password file length:', len(directions))

    for instruction in directions:
        instruction_list = list(instruction)
        direction = instruction_list.pop(0)
        distance = "".join(instruction_list)
        zero_rotations = 0
        
        if direction == 'R':
            (current_value, zero_rotations) = right(current_value, int(distance))
        else:
            (current_value, zero_rotations) = left(current_value, int(distance))

        if current_value == 0:
            zero_count += 1

        zero_count += zero_rotations

    print('password:', zero_count)



if __name__ == "__main__":
    main()
