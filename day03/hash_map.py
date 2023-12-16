# Day 03 => Algo 2 -> HashMap : 
# HashMap use used to store Key Value 
# A hashmap, also known as a hash table, is a data structure that implements an associative array abstract data type, 
# a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots,
# from which the desired value can be found.

# HashMap class is defined with an __init__ method that initializes the hash map.
# [param] size => Determine the size of the hash map.
class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
        
    # The _hash_fun method takes a key as input and returns the hash value using the hash() function.
    # The modulo operation is applied to ensure a hash value falls within the range of the hash map's size
    def _hash_fun(self, key):
        return hash(key) %  self.size
    
    # The putKV method takes a key and a value as input.
    # It appends the key-value pair to the list in the corresponding bucket.
    def putKV(self, key, value):
        hash_value = self._hash_fun(key)
        if self.buckets[hash_value] is None:
            self.buckets[hash_value] = []
                
        self.buckets[hash_value].append((key, value))
        
    # The getKV method takes a key as input and retrieves the associated value.
    # If a key match is found, it returns the associated value; otherwise, it returns None.
    def getKV(self, key):
        hash_value = self._hash_fun(key)
        if self.buckets[hash_value] is not None:
            for stored_key, value in self.buckets[hash_value] :
                if stored_key == key :
                    return value
        
        return None
    
    #The removeKV method takes a key as input and deletes the key-value pair from  the hash map.
    def removeKV(self, key):
        hash_value = self._hash_fun(key)
        
        if self.buckets[hash_value] is not None:
            for index, (stored_key, _) in enumerate(self.buckets[hash_value]):
                if stored_key == key:
                    del self.buckets[hash_value][index]
                    return 
    
# Test -> Example Usage : 
my_hash_map = HashMap(size = 12)

my_hash_map.putKV("Ahmad", 19)
my_hash_map.putKV("Hisham ", 23)
my_hash_map.putKV("Malick", 27) 

print("Age of Malick is ", my_hash_map.getKV("Malick"))  

my_hash_map.removeKV("Ahmad")
if (my_hash_map.getKV("ahmad")) is not None:
    print("Age of Ahmad", my_hash_map.getKV("Ahmad"))
else :
    print("Ahmad not Found")