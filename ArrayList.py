class ArrayList:
     def __init__(self):
      self.data = [2]
     def append(self, elem):
         self.data.append(elem)
     def extend(self, seq):
         for x in seq:
            self.append(x)
         return self
     def __len__(self):
         return len(self.data)
     def __getitem__(self, key):
         if isinstance(key, slice):
             return "a slice!"
         return self.data[key]
     def __setitem__(self, key, val):
        self.data[key] = val
     def __str__(self):
         return str(self.data)
     def __repr__(self):
         return repr(self.data)
     def __delitem__(self, key):
         if key == len(self.data)-1:
            del self.data[key]
         else:
             for i in range(key, len(self.data)-1):
                self.data[i] = self.data[i+1]
             del self.data[len(self.data)-1]
    # def __iter__(self):
class Iterator:
     def __init__(self, data):
       self.idx = len(data)
       self.data = data

     def __iter__(self):
         return self
     def __next__(self):
        if self.idx > 0:
         self.idx -= 1
        return self.data[self.idx]
        raise StopIteration
        return Iterator(self.data)