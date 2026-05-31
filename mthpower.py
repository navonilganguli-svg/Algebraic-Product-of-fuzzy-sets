import re

def validator(func: object) -> object:

    def wrapper(fuzzy_set: dict[str, float],
                m: int):

        if len(fuzzy_set) == 0:

            print("Fuzzy set cannot be empty")

            return

        if m < 1:

            print("Power must be greater than 0")

            return

        return func(fuzzy_set, m)

    return wrapper


def create_fuzzy_set() -> dict[str, float]:

    fuzzy_set: dict[str, float] = {}

    try:

        n = int(input("Enter number of elements: "))

        count: int = 0

        while count < n:

            element: str = input("Enter element: ")

            pattern: str = r"[A-Za-z]+"

            if not re.fullmatch(pattern, element):

                print("Enter a valid element")

                continue

            if element in fuzzy_set:

                print("Element already exists")

                continue

            try:

                membership = float(
                    input("Enter membership value: ")
                )

                if 0 <= membership <= 1:

                    fuzzy_set[element] = membership

                    count += 1

                else:

                    print(
                        "Membership value must be between 0 and 1"
                    )

            except ValueError:

                print(
                    "Enter a valid membership value"
                )

        return fuzzy_set

    except ValueError:

        print("Enter a valid number of elements")

        return {}


@validator
def mth_power(fuzzy_set: dict[str, float],
              m: int) -> dict[str, float]:

    result: dict[str, float] = {}

    for element in fuzzy_set:

        result[element] = (
            fuzzy_set[element] ** m
        )

    return result


if __name__ == "__main__":

    try:

        print("Create Fuzzy Set")

        fuzzy_set = create_fuzzy_set()

        m = int(
            input(
                "Enter the power (m): "
            )
        )

        result = mth_power(
            fuzzy_set,
            m
        )

        print("\nM-th Power of Fuzzy Set:")

        print(result)

    except ValueError:

        print("Enter a valid integer value")