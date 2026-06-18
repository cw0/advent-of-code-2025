def find_invalid_codes(id_range):
    min_max = id_range.split("-")
    first_id = int(min_max[0])
    last_id = int(min_max[1])

    subtotal = 0
    for i in range(first_id, last_id + 1):
        if is_invalid(str(i)):
            subtotal += i
    
    return subtotal



def is_invalid(id):
    if len(id) % 2 != 0:
        return False
    
    half_length = int(len(id) / 2)
    first_half = list(id)[:half_length]
    second_half = list(id)[-half_length:]

    if first_half == second_half:
        return True
    else:
        return False
