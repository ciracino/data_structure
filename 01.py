def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

my_bag = []
insert(my_bag, '가방')
insert(my_bag, '사과')
insert(my_bag, '배')
insert(my_bag, '물')
insert(my_bag, '장난감')
print(my_bag)
print(count(my_bag))
print(contains(my_bag, "물"))
print(contains(my_bag, "사과"))
print(contains(my_bag, "꽃"))
remove(my_bag, '사과')
print(contains(my_bag, "사과"))
print(count(my_bag))