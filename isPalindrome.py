def IsPalindrome(strParam):
    
    contains_digit = any(char.isdigit() for char in strParam)
    contains_letter = any(char.isalpha() for char in strParam)
    contains_alnum = contains_digit and contains_letter

    if contains_alnum:
        cleaned_str = ''.join(char for char in strParam if char.isalnum())
    elif contains_letter:
        cleaned_str = ''.join(char.lower() for char in strParam if char.isalpha())
    else:
        cleaned_str = ''.join(char.lower() for char in strParam if char.isdigit())
         
    return cleaned_str == cleaned_str[::-1]

# keep this function call here
result = "1234321"
print(IsPalindrome(result))