import re

def validator(func: object) -> object:

    def wrapper(set1: dict[str, float],
                set2: dict[str, float]):

        if len(set1) == 0 or len(set2) == 0:
            print("Fuzzy sets cannot be empty")
            return

        return func(set1, set2)

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

                print("Enter a valid membership value")

        return fuzzy_set

    except ValueError:

        print("Enter a valid number of elements")

        return {}


@validator
def algebraic_product(set1: dict[str, float],
                      set2: dict[str, float]) -> dict[str, float]:

    result: dict[str, float] = {}

    common_elements = (
        set(set1.keys()) &
        set(set2.keys())
    )

    for element in common_elements:

        result[element] = (
            set1[element] *
            set2[element]
        )

    return result


if __name__ == "__main__":

    try:

        print("Create First Fuzzy Set")

        fuzzy_set1 = create_fuzzy_set()

        print("\nCreate Second Fuzzy Set")

        fuzzy_set2 = create_fuzzy_set()

        result = algebraic_product(
            fuzzy_set1,
            fuzzy_set2
        )

        print("\nAlgebraic Product:")

        print(result)

    except Exception as e:

        print("An unexpected error occurred:", e)