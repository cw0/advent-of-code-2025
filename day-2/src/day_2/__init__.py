from day_2.utils import find_invalid_codes

def main() -> None:
    print("Hello from day-2!")
    with open("input", "r") as file:
        id_ranges_raw = file.readline()

    id_ranges = list(id_ranges_raw.split(","))
    sum_invalid = 0

    for id_range in id_ranges:
        sum_invalid += find_invalid_codes(id_range)            

    print("sum of invalid ids:", sum_invalid)

if __name__ == "__main__":
    main()