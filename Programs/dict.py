def dict_datastructure(ransomNote,magazine):
    for char in ransomNote:
     if char not in magazine:
       return False
  
    return True
    
ransomNote = "cba"
magazine = "acb"
print(dict_datastructure(ransomNote,magazine))




