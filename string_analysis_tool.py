def analyze_string(input_str):
    vow = 0
    con = 0
    dig = 0
    spl_char = 0
    vowel_set = "aeiouAEIOU"
    digit_set = "0123456789"
    for char in input_str:
        if char.isalpha(): 
            if char in vowel_set:
                vow += 1
            else:
                con += 1
        elif char in digit_set:  
            dig += 1
        elif not char.isspace():  
            spl_char += 1

    # Reverse the string
    reversed_str = input_str[::-1]

    # Display results
    print("String Analysis Results:")
    print(f"Vowels: {vow}")
    print(f"Consonants: {con}")
    print(f"Digits: {dig}")
    print(f"Special Characters: {spl_char}")
    print(f"Reversed String: {reversed_str}")


# Input from the user
user_input = input("Enter a string: ")

# Call the function to analyze the string
analyze_string(user_input)
