"""
# PSEUDOCODE:

While we still have potions and mana is not maxed

  mana += 1


# Great, but how to we determine if we still have potions?

Let say we start with 3 potions. We need to count up, right?


Round
"""


def meditate(mana, max_mana, num_potions):

    while num_potions > 0 and not (mana == max_mana):

        print(f"Number Potions: {num_potions}")

        mana += 1
        num_potions -= 1

    return mana, num_potions


run_cases = [
    (0, 10, 9, [9, 0]),
    (0, 12, 20, [12, 8]),
    (100, 100, 0, [100, 0]),
    (1, 100, 80, [81, 0]),
]

submit_cases = run_cases + [
    (0, 0, 0, [0, 0]),
    (1000, 1000, 5, [1000, 5]),
    (0, 10, 5, [5, 0]),
    (5, 2000, 500, [505, 0]),
]


def test(input1, input2, input3, expected):
    print("---------------------------------")
    print("Inputs:")
    print(f" *           mana: {input1}")
    print(f" *       max_mana: {input2}")
    print(f" *    num_potions: {input3}")
    result_mana, result_potions = meditate(input1, input2, input3)
    print(f"Expected: mana {expected[0]}, potions {expected[1]}")
    print(f"Actual:   mana {result_mana}, potions {result_potions}")
    if result_mana == expected[0] and result_potions == expected[1]:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
