def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    return "incorrect amount"

print(f'Running function with (500, 1000): {check_swords_for_army(500, 1000)}')
print(f'Running function with (800, 800): {check_swords_for_army(800, 800)}')
# print(f"check_swords_for_army(500, 1000)")
# print('Running function with (800, 800)')
# check_swords_for_army(800, 800)


# from main import *

# run_cases = [
#     (500, 1000, "incorrect amount"),
#     (800, 800, "correct amount"),
# ]

# submit_cases = run_cases + [
#     (1500, 1000, "incorrect amount"),
#     (200, 200, "correct amount"),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}")
#     result = check_swords_for_army(input1, input2)
#     print(f"Expected: {expected_output}")
#     print(f"Actual:   {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     skipped = len(submit_cases) - len(test_cases)
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")

#     if skipped > 0:
#         print(f"{passed} passed, {failed} failed, {skipped} skipped")
#     else:
#         print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()