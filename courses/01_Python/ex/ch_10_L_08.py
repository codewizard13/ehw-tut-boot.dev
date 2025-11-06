def get_most_common_enemy(enemies_dict):
    
    # early exit if no enemies
    if len(enemies_dict) == 0:
        return None


    max_so_far = float("-inf")
    max_name = None

    for enemy in enemies_dict:

        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]

    return 


enemies_dict = {
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}

most_common_enemy = get_most_common_enemy(enemies_dict)

print(f"The Most Common Enemy is:  {most_common_enemy}")