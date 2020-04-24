#                               COURSE DATA STRUCTURES
#
#               Native Python Data Structures, Operators for Sequence
#               Types like: Strings, List, Tuples
#               UDEMY LINK: https://www.udemy.com/course/python-data-structures-a-to-z/

# If this code works, it was written by DarkMarksDoe. If not, I don't know
# who wrote it, just pass away


# INFO ABOUT MATHEMATICAL SET OPERATIONS

# ~ Intersection (AND): set1 & set2
# ~ Union (OR): set1 | set2
# ~ Symmetric Difference (XOR): set1 ^ set2
# ~ Difference (in set1 but not set2): set1 - set2
# ~ Subset (set2 contains set1): set1 <= set2
# ~ Superset (set1 contains set2): set1 >= set2

#                               MATHEMATICAL OPERATIONS

set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}

# Intersection
print('Intersection:', set1 & set2)
# Union
print('Union:', set1 | set2)

# Symmetric Difference
print('Symmetric Difference:', set1 ^ set2)

# Difference
print('Difference:', set1 - set2)

# Subset
print('Subset:', set1 <= set2)

# Superset
print('Superset:', set1 >= set2)
