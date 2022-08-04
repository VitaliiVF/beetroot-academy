class Mathematician(list):
    
    def square_nums(self, _list):
        return [i**2 for i in _list]
    
    def remove_positives(self, _list):
        return [i for i in _list if i < 0]
    
    def filter_leaps(self, _list):
        return [i for i in _list if i % 4 == 0]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))

print(m.remove_positives([26, -11, -8, 13, -90]))

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))