"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    pass  # TODO: replace this line with your code
    for item in items: 
        print(item)

def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_nums = []
    for num in nums: 
        if num % 2 == 0: 
            even_nums.append(num)
    return even_nums

def get_odd_indices(items):
    pass  # TODO: replace this line with your code
    result = []
    for idx,item in enumerate(items):
        if idx % 2 != 0: 
            result.append(item)
    return result

def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code
    i = 1
    for item in items: 
        print(f"{i}. {item}")
        i += 1

def get_range(start, stop):
    pass  # TODO: replace this line with your code
    nums = []
    
    num = start
    while num < stop:
        nums.append(num)
        num += 1

    return nums



def censor_vowels(word):
    pass  # TODO: replace this line with your code
    new_word = []
    for letter in word: 
        if letter in 'aeiou':
            new_word.append("*")
        else: 
            new_word.append(letter)
    return "".join(new_word)

def snake_to_camel(string):
    pass  # TODO: replace this line with your code
    camel_case = []
    for word in string.split("_"):
        camel_case.append(word.capitalize())
    return "".join(camel_case)

    
def longest_word_length(words):
    pass  # TODO: replace this line with your code
    longest_length = len(words[0])
    for word in words: 
        if len(word) > longest_length: 
            longest_length = len(word)
    return longest_length

def truncate(string):
    pass  # TODO: replace this line with your code
    result = []
    for char in string: 
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)
    return "".join(result)


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code
    parens = 0
    for char in string: 
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
            if parens < 0: 
                return False
    return parens == 0

def compress(string):
    pass  # TODO: replace this line with your code
    compress = []
    cur_char = ""
    char_count = 0
    for char in string: 
        if char != cur_char: 
            compress.append(cur_char)
            if cur_char > 1: 
                compress.append(str(char_count))
            cur_char = char
            char_count = 0
        else:
            char_count += 1 
    compress.append(cur_char)
    if char_count > 1:
        compress.append(str(char_count))
    return "".join(compress)
                
