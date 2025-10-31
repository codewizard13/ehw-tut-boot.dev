# Remember, `range` is inclusive of the start, but exclusive of the end
counter = 0
for number in range(1, 51):
    counter = counter + 1

    if counter == 7:
        counter = 0 # Reset the counter
        continue # Skip this number

    print(number)