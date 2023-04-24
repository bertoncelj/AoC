
# def add (a):
    # def 
    # return lambda x: x + a
  

add = lambda a: lambda b: a + b 

def sum(i):
    return 0 if i <= 0 else i + sum(i-1)




pair = lambda first: lambda second: {"first": first, "second":second}
head = lambda pair: pair["first"]
tail = lambda pair: pair["second"]
# print(sum(10))
print(add(123)(7))
# print(add(123)(2))
#

# print(pair(1)(2))
# print(head(pair(1)(2)))
# print(tail(pair(1)(2)))
#
xs = pair(3) (pair (2) (pair(1)(None)))
# print(head(xs))
# print(tail(xs))


def list2array(xs):
    end = []
    while None != xs:
        end.append(head(xs))
        xs = tail(xs)
    return end

# print(list2array(xs))


def array2list(ll):
    ll.reverse()
    result = None
    for i in ll:
        result = pair(i) (result)
    return result

# print(list2array(array2list([1,2,3,4,5])))

range(1,10)

range = lambda start: lambda end: None if start > end else pair (start) ( range (start + 1) (end))
print(list2array(range(1)(10)))

map = lambda f: lambda xs: None if xs == None else pair (f (head(xs))) (map(f) (tail (xs)))
print(list2array(map(lambda x: x*2) (range(1)(10))))
list_ana = range(1)(50) 
print(list2array(map (lambda x: "FizBuzz" if x%15 == 0 else x) (list_ana)))
print(list2array(map (lambda x: "Buzz" if x%5 == 0 else x) (list_ana)))
print(list2array(map (lambda x: "Fizz" if x%3 == 0 else x) (list_ana)))


fizzbuzz = lambda x: ("Fizz" if x%3 == 0 else "") + ("Buzz" if x%5 == 0 else "") or x
print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(5))
print(fizzbuzz(3))

print(fizzbuzz(15))
print(list2array(map (fizzbuzz) (list_ana)))
