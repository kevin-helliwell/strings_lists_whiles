# Takes a list of numbers, adds all negative even numbers in the list and returns the average of those numbers.
def average_neg_evens(list_of_numbers):
    num, total, i = 0, 0, 0
    while i < len(list_of_numbers):
        if list_of_numbers[i] < 0 and list_of_numbers[i] % 2 == 0:
            num += 1
            total += list_of_numbers[i]
        i += 1
    return total/num

# Counts the number of letters in a list of strings, both upper and lower case.
# Original iteration
# def count_letter(list_of_strings, letter):
#     total_list = []
#     i = 0
#     while i < len(list_of_strings):
#         total_list += list_of_strings[i].lower()
#         i += 1
#     count = total_list.count(letter.lower())
#     return count


# Counts the number of letters in a list of strings, both upper and lower case.
# Second iteration
# def count_letter(list_of_strings, letter):
#     total_list = []
#     i = 0
#     count = 0
#     while i < len(list_of_strings):
#         total_list += list_of_strings[i].lower()
#         count = total_list.count(letter.lower())
#         i += 1
#     return count


# Counts the number of letters in a list of strings, both upper and lower case.
# Third iteration
def count_letter(list_of_strings, letter):
    letter = letter.lower()  # Converts input letter into lower-case version
    i, total = 0, 0  # Initializes loop variable and return variable
    while i < len(list_of_strings):  # Runs loop while index is in range of list length
        string = list_of_strings[i].lower()  # Converts string into lower-case version
        total += string.count(letter)  # Adds up occurrences of the input letter in the string
        i += 1  # Increments loop variable to move on to next string
    return total  # Returns sum of occurrences of input letter from all strings in list


def main():
    # Test cases
    # 1
    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
    if average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]) == -3:
        print("Test successful!")
    else:
        print("Oops!")
    # 2
    list1 = ["HELLO", "goodbye", "1234 Oooh!"]
    print(count_letter(list1, "o"))
    if count_letter(list1, "o") == 6:
        print("Test successful!")
    else:
        print("Oops!")
    # 3
    print(average_neg_evens([-2, -4, -6, -9, -10, 2]))
    if average_neg_evens([-2, -4, -6, -9, -10, 2]) == -5.5:
        print("Test successful!")
    else:
        print("Oops!")
    # 4
    print(count_letter(list1, "e"))
    if count_letter(list1, "e") == 2:
        print("Test successful!")
    else:
        print("Oops!")


main()
