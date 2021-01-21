# A dynamic array in Python is meaningless since we can't create of a specific size.
# However, the idea is:
# 1. Initialize an array of a certain size
# 2. When you add an item, increment size.
# 3. When you remove an item, decrement size.
# 4. When adding an item, if the array is 2/3 full,
#    double the array and copy over contents to new array.