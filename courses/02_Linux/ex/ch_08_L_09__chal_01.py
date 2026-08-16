# Pseudocode:
#
# counter = START_VALUE   # some non-negative integer
# flag = false

# while counter >= 0 and not flag:
#     if counter % 3 == 0:
#         flag = true
#     if counter % 2 == 0:
#         continue
#     counter = counter - 1



# count = 0
# while count < 5:
#     print(f"Count is: {count}")
#     count += 1
# else:
#     print("Loop finished normally.")


# WORKS!

counter = 11
flag = False

while counter >= 0 and not flag:

    print(counter)

    # If counter is multiple of 3
    if counter % 3 == 0:
        counter -= 1

        flag = True # early exit

    # If counter is multiple of 2
    elif counter % 2 == 0:
        counter -= 1
        continue

    else:
        counter -= 1
    

    
