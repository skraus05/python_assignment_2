def max_num(x, y, z):
    return max([x, y, z])
print(max_num(25, 75, 100))

def mult_list(lst):
    result = 1
    for numbers in lst:
        result *= numbers
    return result
numbers = [4, 5, 6, 7, 8, 9]
print(mult_list(numbers))

def rev_string(string):
    return string[::-1]
string = "hello"
print(rev_string(string))

def num_within(number, beginning, end):
    return beginning <= number <= end
print(num_within(5, 2, 8))
print(num_within(15, 2, 5))

def pascal(n):
    def binomial_coefficient(n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(k):
            res *= (n - 1)
            res //= (i + 1)
        return res
    for line in range(1, n + 1):
        for j in range(n - line):
            print('', end='')
        for i in range(line):
            print(binomial_coefficient(line - 1, i), '', end='')
        print()
n = 5
pascal(5)