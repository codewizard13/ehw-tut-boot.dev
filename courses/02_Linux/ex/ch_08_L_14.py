"""
# PSEUDOCODE:

Calculate previous level's xp (prev_xp)

Calculate xp needed to jump to current level (jump_xp)

current xp = prev_xp + jump_xp



# level means the current level
# we need a variable name for iterating through levels in a loop, as a temp variable
# ok, we'll call it level iterator for now

function calcPrevXP(cur_lvl)

  prev_lev_xp = 0 # initialize var

  lvl_iterator = cur_lvl-1


  // do stuff
  # Process current lev iterator with loop


    # at end of the loop, decrement the level iter, that way we don't modify 'level'
    lvl_iterator -= 1


"""

#WORKS!
def calcPrevXP(cur_lvl):

  lvl_iterator = cur_lvl
  prev_xp = 0 # initialize at zero

  print(f"lvl_iterator START: {lvl_iterator}")

  for i in range(1, lvl_iterator+1):
    print(f"i: {i}")

    cur_xp = prev_xp + ((i - 1) * 5)
    print(f"Current XP: {cur_xp}")

    # set current prev_xp to cur_xp value to prepare for next iteration
    prev_xp = cur_xp

  return cur_xp


def main():
  print("========================")
  print("Debgging the loop")
  print("========================")

  level = 5

  result = calcPrevXP(level)

  print(f"\nXP for level {level}: {result}")

main()






