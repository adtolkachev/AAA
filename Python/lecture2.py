
def fuzz_buzz_test(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return 'FuzzBuzz'

        return 'Fuzz'

    elif num % 5 == 0:
        return 'Buzz'

    else:
        return num



def custom_fuzz_buzz(slice:list = [], start:int = 0, end:int = 0):
    if slice == [] and start == 0 and end == 0:
        raise ValueError
    
    elif slice == []:
        for _ in list(range(start, end)):
            print(fuzz_buzz_test(_))
    
    else:
        for _ in slice:
            print(fuzz_buzz_test(_))


if __name__ == '__main__':
    custom_fuzz_buzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15], 10)

