def detect_pattern(s1, s2):
    # Check if the lengths of the two strings are the same
    if len(s1) != len(s2):
        return False
    
    # Create mappings for both strings
    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}
    
    # Iterate over characters of both strings
    for char1, char2 in zip(s1, s2):
        # Check mapping from s1 to s2
        if char1 in mapping_s1_to_s2:
            if mapping_s1_to_s2[char1] != char2:
                return False
        else:
            mapping_s1_to_s2[char1] = char2
        
        # Check mapping from s2 to s1
        if char2 in mapping_s2_to_s1:
            if mapping_s2_to_s1[char2] != char1:
                return False
        else:
            mapping_s2_to_s1[char2] = char1
            
    return True

# Test cases
assert detect_pattern("", "") == True
assert detect_pattern("a", "a") == True
assert detect_pattern("x", "y") == True
assert detect_pattern("ab", "xy") == True
assert detect_pattern("aba", "xyz") == False
assert detect_pattern("---", "xyz") == False
assert detect_pattern("---", "aaa") == True
assert detect_pattern("xyzxyz", "toetoe") == True
assert detect_pattern("xyzxyz", "toetoa") == False
assert detect_pattern("aaabbbcccd", "eeefffgggz") == True
assert detect_pattern("cbacbacba", "xyzxyzxyz") == True
assert detect_pattern("abcdefghijk", "lmnopqrstuv") == True
assert detect_pattern("asasasasas", "xxxxxyyyyy") == False
assert detect_pattern("ascneencsa", "aeiouaeiou") == False
assert detect_pattern("aaasssiiii", "gggdddfffh") == False

print("All test cases passed!")
