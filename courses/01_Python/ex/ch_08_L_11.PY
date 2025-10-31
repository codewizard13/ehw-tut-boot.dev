def main():

  skipSevens()

  skipNegatives()




# SKIP EVERY 7th NUMBER
#
# NOTE: This works by maintaining a secondary 'seventh number counter'

# Remember, `range` is inclusive of the start, but exclusive of the end
def skipSevens():

  counter = 0
  for number in range(1, 51):
      counter = counter + 1

      if counter == 7:
          counter = 0 # Reset the counter
          continue # Skip this number

      print(number)


# SKIP NEGATIVE NUMBERS
#
#
def skipNegatives():
    
    numbers = [16, -4, 25, -9, 36, 0, 49]

    for number in numbers:
        if number < 0:
            continue  # Skip negatives to avoid complex numbers

        print(f"The square root of {number} is {number ** 0.5}.")



main()
  