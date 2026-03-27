def max_unique_char_substring(instring : str):
    char_index_dict : dict[str, int | bool] = dict()
    substring : str = ""
    
    for char in instring:
        print("-", char)
        split_index = char_index_dict.get(char, False)
        if split_index:
            update_chars = substring[:split_index]
            substring = substring[split_index:] + char
            print(update_chars, ",", substring)

            for update_char in update_chars:
                char_index_dict[update_char] = False

            char_index_dict[char] = len(substring) - 1
            continue
        print(substring)

        char_index_dict[char] = len(substring) - 1
        substring += char
    
    return substring

print(max_unique_char_substring("ABCADFECAB"))

print(max_unique_char_substring("BBB"))