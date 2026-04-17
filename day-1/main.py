
# this is a circularly linked list problem first we need to define how to move in our circularly linked list

    
def left(current_value, distance):
    temp_value = current_value - distance
    if (temp_value < 0):
        return 100 + temp_value
    else:
        return temp_value

def right(current_value, distance):
    temp_value = current_value + distance
    if (temp_value > 99):
        return temp_value - 100
    else:
        return temp_value

def main():
    current_value = 99;

    with open("day-1/input", "r") as file:
        directions = file.readlines()
        # print(len(directions))

    next_value = right(current_value, 1)
    print(next_value)


if __name__ == "__main__":
    main()
