class HashTable:

    def __init__(self):
        self.size = 10
        self.data = [None] * self.size
        self.spots = [None] * self.size


    def put(self, key, data):
        if self.is_full():
            self.resize()
        hashvalue = self.hashfunction(key, len(self.spots))
        if self.spots[hashvalue] == None:
            self.spots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.spots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                next = self.rehash(hashvalue, len(self.spots))
                while self.spots[next] != None and \
                        self.spots[next] != key:
                    next = self.rehash(next, len(self.spots))
                if self.spots[next] == None:
                    self.spots[next] = key
                    self.data[next] = data
                else:
                    self.data[next] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        start = self.hashfunction(key, len(self.spots))
        data = None
        stop = False
        found = False
        position = start
        while self.spots[position] != None and \
                not found and not stop:
            if self.spots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.spots))
                if position == start:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
# Exercises Practice
    
    def __contains__(self, key):
        contains = False
        if key in self.spots:
            contains = True
        return contains

    def remove_item(self, key):
        if self.__contains__(key):
            hash_value = self.hashfunction(key, len(self.spots))
            if self.spots[hash_value] != key:
                hash_value = self.rehash(key, len(self.spots))
                while self.spots[hash_value] != key:
                    hash_value = self.rehash(hash_value, len(self.spots))
            self.spots[hash_value] = None
            self.data[hash_value] = None
        else:
            print(f"{key} is not in the table")

    def __delitem__(self, key):
        self.remove_item(key)

    def is_full(self):
        is_full = False
        amount_of_items = 0
        for item in self.spots:
            if item != None:
                amount_of_items += 1
        if amount_of_items >= self.size:  # The spots are full
            is_full = True
        return is_full

    def resize(self, new_size=23):
        if prime(new_size):
            self.spots = self.spots + ([None] * (new_size - self.size))
            self.data = self.data + ([None] * (new_size - self.size))
            self.size = new_size
        else:
            print("Enter any prime number")


def prime(num):
    prime = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
    return prime


def main():
    H = HashTable()
    H[14] = "kitten"
    H[22] = "dog"
    H[98] = "lion"
    H[10] = "giraffe"
    H[69] = "bird"
    H[30] = "cow"
    H[45] = "bear"
    H[18] = "pig"
    H[28] = "turkey"
    H[76] = "horse"
    print(H.spots)
    print(H.data)
    H[21] = "Male"
    H[40] = "Female"
    H[80] = "Dad"
    H[92] = "Mom"
    H[57] = "G-Ma"
    H[9] = "G-pa"
    print(H.spots)
    print(H.data)


if __name__ == '__main__':
    main()