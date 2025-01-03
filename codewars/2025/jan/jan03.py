cw = '''
Create a function that will return true if the input is in the following date time format 01-09-2016 01:20 and false if it is not.

This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.
'''

# from datetime import datetime
#
#
# def date_checker(date):
#     try:
#         datetime.strptime(date, '%d-%m-%Y %H:%M')
#         return True
#     except ValueError:
#         return False


'''The example above didn't work as the kata is completely misleading.
The date itself doesn't have to be valid so checking for the datetime will not work. 
Random bs tests checks for month 47th or hours like 97:78, etc. 
'''

import re


def date_checker(date):
    pattern = r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$'
    return bool(re.match(pattern, date))


# print(date_checker("01-09-2016 01:20"))
# print(date_checker("01-09-2016 01;20"))
# print(date_checker("01-09_2016 01:20"))
# print(date_checker("01-09 2016 01:20"))
# print(date_checker("01-09 2016"))

'''
Your dad doesn't really get punctuation, and he's always putting extra commas in when he posts.
You can tolerate the run-on sentences, as he does actually talk like that, but those extra commas have to go!

Write a function that takes a string as an argument and returns a string with the extraneous commas removed.
The returned string should not end with a comma or have any trailing whitespace.
'''
import re


def dad_filter(string):
    return re.sub(r',+', ',', string).strip().strip(',')


# print(dad_filter("all this,,,, used to be trees,,,,,,"))
# print(dad_filter("Dead or alive,,,, you're coming with me,,,   "))


'''
DNA is a biomolecule that carries genetic information.
It is composed of four different building blocks, called nucleotides: adenine (A), thymine (T), cytosine (C) and guanine (G).
Two DNA strands join to form a double helix, whereby the nucleotides of one strand bond to the nucleotides of the other strand at the corresponding positions.
The bonding is only possible if the nucleotides are complementary: A always pairs with T, and C always pairs with G.

Due to the asymmetry of the DNA, every DNA strand has a direction associated with it.
The two strands of the double helix run in opposite directions to each other, which we refer to as the 'up-down' and the 'down-up' directions.

Write a function checkDNA that takes in two DNA sequences as strings, and checks if they are fit to form a fully complementary DNA double helix. The function should return a Boolean true if they are complementary, and false if there is a sequence mismatch (Example 1 below).

Note:

All sequences will be of non-zero length, and consisting only of A, T, C and G characters.
All sequences will be given in the up-down direction.
The two sequences to be compared can be of different length. If this is the case and one strand is entirely bonded by the other, and there is no sequence mismatch between the two (Example 2 below), your function should still return true.
If both strands are only partially bonded (Example 3 below), the function should return false.
Example 1:

seq1 = 'GTCTTAGTGTAGCTATGCATGC';  // NB up-down
seq2 = 'GCATGCATAGCTACACTACGAC';  // NB up-down

checkDNA (seq1, seq2);
// --> false

// Because there is a sequence mismatch at position 4:
// (seq1)    up-GTCTTAGTGTAGCTATGCATGC-down
//              ||| ||||||||||||||||||
// (seq2)  down-CAGCATCACATCGATACGTACG-up
Example 2:

seq1 = 'GCGCTGCTAGCTGATCGA';             // NB up-down
seq2 = 'ACGTACGATCGATCAGCTAGCAGCGCTAC';  // NB up-down

checkDNA (seq1, seq2);
// --> true

// Because one strand is entirely bonded by the other:
// (seq1)       up-GCGCTGCTAGCTGATCGA-down
//                 ||||||||||||||||||
// (seq2)  down-CATCGCGACGATCGACTAGCTAGCATGCA-up
Example 3:

seq1 = 'CGATACGAACCCATAATCG';  // NB up-down
seq2 = 'CTACACCGGCCGATTATGG';  // NB up-down

checkDNA (seq1, seq2);
// --> false

// Because both strands are only partially bonded:
// (seq1)  up-CGATACGAACCCATAATCG-down
//                      |||||||||
// (seq2)          down-GGTATTAGCCGGCCACATC-up
'''


def check_DNA(seq1, seq2):
    seq2rev = seq2[::-1]
    dna_dict = {'A': 'T',
                'C': 'G',
                'T': 'A',
                'G': 'C'
                }
    seq2complementary = ''.join([dna_dict[letter] for letter in seq2rev])

    if len(seq2complementary) <= len(seq1):
        return True if seq2complementary in seq1 else False
    else:
        return True if seq1 in seq2complementary else False
    # return seq2complementary, seq2rev, seq2, seq1

print(check_DNA('GTCTTAGTGTAGCTATGCATGC', 'GCATGCATAGCTACACTACGAC'))
print(check_DNA('TGCTACGTACGATCGACGATCCACGAC', 'GTCGTGGATCGTCGATCGTACGTAGCA'))
