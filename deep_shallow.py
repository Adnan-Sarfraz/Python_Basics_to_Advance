import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)     # Shallow copy
deep = copy.deepcopy(original)    # Deep copy

original[0][0] = 99               # Change first element

print("Original:", original)    # [[99, 2], [3, 4]]

print("Shallow:", shallow)      # [[99, 2], [3, 4]]  ← also changed
print("Deep:", deep)            # [[1, 2], [3, 4]]   ← not changed