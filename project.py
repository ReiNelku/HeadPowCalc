import re
from exceptions import InvalidSpecification, InvalidOption
from classes import Headphone, Amplifier


def main():
    print("HeadPowCalc")
    print("\n")

    headphone = get_headphone()
    print("\n")

    print("[1] Display headphone specifications")
    if headphone.is_v:
        print("[2] Convert sensitivity to dB/mW")
    else:
        print("[2] Convert sensitivity to dB/V")
    print("[3] Calculate the required power from the Amp")

    option = check_option()
    print("\n")

    match option:
        case "1":
            print(headphone)
        case "2":
            if headphone.is_v:
                print(f"{headphone.sens} dB/V -> {headphone.sens_conv()} db/mW")
            else:
                print(f"{headphone.sens} dB/mW -> {headphone.sens_conv()} db/V")
        case "3":
            amplifier = get_amp(headphone)
            print("\n")
            print(amplifier)


def get_headphone():
    # Ask the user for correct specs and return a Headphone object with those specs
    impedance = check_specification("Impedance")
    sensitivity = check_specification("Sensitivity")
    v = check_unit()

    return Headphone(impedance, sensitivity, v)


def get_amp(headphone):
    # Ask the user for correct specs and return a Amplifier object
    loudness = check_specification("Loudness")

    return Amplifier(headphone, loudness)


def get_specification(spec):
    specification = input(f"Headphone {spec}: ").strip()

    # Check with Regex if the sensitivity is a number, otherwise raise an error
    if (value := re.search(r"^(\d+)(?:\.(\d+))?$", str(specification))) is None:
        raise InvalidSpecification(f"Invalid {spec} Value")

    # Asign the variable as a float if decimal numbers are present
    if value.group(2):
        return float(specification)
    else:
        return int(specification)


def check_specification(spec):
    # Return spec if only it is correct
    while True:
        try:
            specification = get_specification(spec)
        except InvalidSpecification:
            print("\n")
        else:
            break

    return specification


def get_unit():
    # Ask the user for the unit and return True for 1 and False for 2, otherwise raise an error
    print("[1] Sensitivity in dB/V")
    print("[2] Sensitivity in dB/mW")
    print("\n")

    option = input("Type an option 1,2: ").strip()

    if re.match(r"1|2", option) == None:
        raise InvalidOption

    if option == "1":
        return True
    else:
        return False


def check_unit():
    # Return unit if only it is correct
    while True:
        try:
            unit = get_unit()
        except InvalidOption:
            print("\n")
        else:
            break

    return unit


def get_option():
    # Ask the user for an option and raise an error if its incorrect
    option = input("Type an option 1,2,3: ").strip()

    if re.match(r"[1-3]", option) == None:
        raise InvalidOption

    return option


def check_option():
    # Return option if only it is correct
    while True:
        try:
            option = get_option()
        except InvalidOption:
            print("\n")
        else:
            break

    return option


if __name__ == "__main__":
    main()
