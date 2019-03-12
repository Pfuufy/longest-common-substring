
str1 = 'hellobatn'
str2 = 'bellabatm'

str3 = 'borisamr'
str4 = 'boredamr'

str5 = 'ball'
str6 = 'tom'

str7 = 'hellobatncarttumm'
str8 = 'bellopabatmcaratumm'

def manage_substrings(substring, substrings):
    if substring not in substrings:
        substrings.append(substring)

    return substrings


def find_substrings(str1, str2):
    substrings = []
    end1 = len(str1)
    end2 = len(str2) - 1
    index1 = 0
    index2 = 0
    last_chars_match = False

    substring = ''
    substring_start = -1
    
    while index1 < end1:
        char1 = str1[index1]
        char2 = str2[index2]
        
        if char1 != char2:
            
            # reset start of substring search if previous chars were match
            if (last_chars_match):
               index1 = substring_start
               substring_start = -1
            # indicates end of common substring
            elif index2 < end2:
                index2 += 1
            elif index2 == end2:
                index1 += 1
                index2 = 0
                
            substring = ''
            last_chars_match = False
            
        elif char1 == char2:
            
            if substring_start == -1:
                substring_start = index1

            if index2 == end2:
                index1 += 1
                index2 = 0
                last_chars_match = False
                substring_start = -1
            else:
                index2 += 1
                index1 += 1
                last_chars_match = True

            substring += char2
            substrings = manage_substrings(substring, substrings)
    
    return substrings


def longest_substring(str1, str2):
    substrings = find_substrings(str1, str2)
    longest_substring = ''
    longest_substrings = []

    if len(substrings) == 0:
        return 'There are no common substrings'

    for substring in substrings:
        if len(substring) > len(longest_substring):
            longest_substring = substring
        elif len(substring) == len(longest_substring):
            longest_substrings.append(substring)
            longest_substrings.append(longest_substring)

    if len(longest_substrings) > 1:
        separator = ', '
        separated_substrings = separator.join(longest_substrings)
        return ('The longest substrings are {}'
                .format(separated_substrings))
    else:
        return 'The longest substring is {}'.format(longest_substring)


            
