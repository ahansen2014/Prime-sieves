import time
from time import process_time
import dis

def check_everything(upper):
    primes = []
    for test_value in range(2, upper):
        is_prime = True
        for factor in range(2, test_value):
            if test_value % factor == 0:
                is_prime = False
        if is_prime:
            primes.append(test_value)
    return primes

def check_odds(upper):
    primes = []
    for test_value in range(3, upper, 2):
        is_prime = True
        for factor in range(3, test_value, 2):
            if test_value % factor == 0:
                is_prime = False
        if is_prime:
            primes.append(test_value)
    return primes




uppers = [1000, 5000, 10_000, 50_000, 100_000]
for upper in uppers:
    start = time.process_time()
    print(len(check_everything(upper)))
    #print(len(check_odds(upper)))
    stop = time.process_time()
    print(f'Processing time for {upper}: {stop - start} sec.')
#dis.dis(check_everything)