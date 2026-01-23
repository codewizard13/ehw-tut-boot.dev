#WORKS
def count_vowels(text):

    
    #dict
    vowel_counts = {
      "a":0,
      "A":0,
      "e":0,
      "E":0,
      "i":0,
      "I":0,
      "o":0,
      "O":0,
      "u":0,
      "U":0
    }

    # #set
    unique_vowels = set()

    for char in text:
        print(f"Char: {char}")

    #     #if char is a vowel
        if char in vowel_counts:
            # print(f"YES - Char {char} was found in the vowels_counts dict")

            vowel_counts[char] += 1
            
            unique_vowels.add(char)

    return sum(vowel_counts.values()), unique_vowels




test_str = "Did someone say Thunderfury, Blessed Blade of the Windseeker?"
test_str = "All Your Base Are Beloing To Us!!!"

vowel_counts, unique_vowels = count_vowels(test_str)
print("Vowel Counts: ", vowel_counts)
print("Unique Vowels Found", unique_vowels)
        

