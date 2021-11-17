import itertools

keyboard_dict = {
    1: ["1", "2", "4"],
    2: ["2", "1", "3", "5"],
    3: ["3", "2", "6"],
    4: ["4", "1", "5", "7"],
    5: ["5", "2", "4", "6", "8"],
    6: ["6", "3", "5", "9"],
    7: ["7", "4", "8"],
    8: ["8", "5", "7", "9"],
    9: ["9", "6", "8"],
    0: ["0", "8"],
}


def get_pins(observed_pin: str):
    """Purpose: To find all combinations of a number given the specifications provided by the problem
    Parameters: observed_pin = The input string that will undergo analysis,
                 keyboard_dict = Dictionary containing all valid options adjacent to a number
    Return Value: output = A list containing all possible combinations of the inputted number
    """
    results = set()
    output = list(
        itertools.product(
            keyboard_dict[int(observed_pin[0])],
            keyboard_dict[int(observed_pin[1])],
            keyboard_dict[int(observed_pin[2])],
            keyboard_dict[int(observed_pin[3])],
        )
    )
    for grouping in output:
        results.add("".join(grouping))

    return results
