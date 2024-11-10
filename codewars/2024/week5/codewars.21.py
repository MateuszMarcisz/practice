may21 = """Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""


def sort_array(source_array):
    if not source_array:
        return []
    else:
        sorted_lst = []
        sorted_odd_lst = sorted([x for x in source_array if x % 2 == 1])
        counter_odd = 0

        for i in source_array:
            if i % 2 == 1:
                sorted_lst.append(sorted_odd_lst[counter_odd])
                counter_odd += 1
            else:
                sorted_lst.append(i)
        return sorted_lst


# print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 11, 0]))
# print(sort_array([]))


"""When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:
    Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
    Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")
Example
"#FF9933" --> {r: 255, g: 153, b: 51}
"""


def hex_string_to_RGB(hex_string):
    # r = int(hex_string[1:3], 16)
    # g = int(hex_string[3:5], 16)
    # b = int(hex_string[5:7], 16)
    # RGBdict = {'r': r, 'g': g, 'b': b}
    # return RGBdict
    return {'r': int(hex_string[1:3], 16), 'g': int(hex_string[3:5], 16), 'b': int(hex_string[5:7], 16)}


# print(hex_string_to_RGB("#FF9933"))
# print(hex_string_to_RGB("#beaded"))
# print(hex_string_to_RGB("#111111"))

"""Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.
Remarks
    a or b might be [] or {} (all languages except R, Shell).
    a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
"""


def comp(array1, array2):
    if not array1 and not array2:
        return False
    if not array1 or not array2:
        return False
    if len(array1) != len(array2):
        return False

    s1 = sorted(array1)
    s2 = sorted(array2)

    for i in range(len(s1)):
        if s1[i] ** 2 != s2[i]:
            return False
    return True


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([], []))

two errors
