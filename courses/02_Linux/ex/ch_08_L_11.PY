def main():

  # skipSevens()

  # skipNegatives()


  test(1, 11, 1)
  test(20, 24, 1)
  test(10, 12, 1)
  test(11, 19, 1)







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



# MY ANSWER TO: award_enchantments() (Works)

def award_enchantments(start, end, step):

    counter = 0
    
    for quest_number in range(start, end, step):
        counter += 1

        if counter < 3:
            continue

        counter = 0
        
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")



main()










main()
  