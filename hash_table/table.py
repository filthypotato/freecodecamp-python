class HashTable:
    def __init__(self):
        # Stores: { hashed_value: { original_key: value, ... }, ... }
        self.collection = {}

    def hash(self, string):
        # Sum Unicode (ASCII) code points for each character
        total = 0
        for ch in string:
            total += ord(ch)
        return total

    def add(self, key, value):
        hashed_key = self.hash(key)

        # If this hash bucket doesn't exist yet, create it
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the key/value in the bucket (handles collisions)
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)

        # If there's no bucket, or the key isn't in the bucket, do nothing
        bucket = self.collection.get(hashed_key)
        if not bucket or key not in bucket:
            return

        # Remove the key from the bucket
        del bucket[key]

        # Optional cleanup: if bucket becomes empty, remove it from collection
        if not bucket:
            del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        bucket = self.collection.get(hashed_key)

        if not bucket:
            return None

        return bucket.get(key, None)
