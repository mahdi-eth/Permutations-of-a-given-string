from itertools import permutations
def permutation_finder(string):
    string_list = list(permutations(string))
    for i in string_list:
        print("    ","".join(list(i)))
    print(len(string_list))    

string = str(input("Enter a string to see its permutations : "))
permutation_finder(string)




