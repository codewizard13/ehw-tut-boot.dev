# WORKS!
def get_most_common_enemy(enemies_dict): 
    
    # early exit if no enemies
    if len(enemies_dict) == 0:
        return None

    max_so_far = float("-inf")
    most_common_enemy = None

    for name in enemies_dict:

        count = enemies_dict[name]

        # print(f"ENEMY = {name}, COUNT = {count}")

        if count > max_so_far:
            most_common_enemy = name
            print(f"{name} ({count}) is greater than {max_so_far}\n\tNew Most Common Enemy = {most_common_enemy}")
            max_so_far = count

        elif count == max_so_far:
            return most_common_enemy 

    return most_common_enemy


enemies_dict = {
    # "jackal": 1,
    # "kobold": 2,
    # "soldier": 3,
    # "gremlin": 5,
    # "selkie": 5
}

# enemies_dict = {}

most_common_enemy = get_most_common_enemy(enemies_dict)

print(f"The Most Common Enemy is:  {most_common_enemy}")


"""
# ALGORITHM:

# RETURN/OUTPUT:  Name of most common enemy

# LOOP over all enemies in dictionary and return only the NAME of the ONE with the highest count

# IF no enemies, return None

# If multiple enemies with same highest count, return the first encountered

# Track max_so_far starting at negative infinity

# Track enemy name associated with max count, initialized to None








"""
