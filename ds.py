#!/usr/bin/python3
# Kern Raphael, TERM5 - DS NSI 1 recursivité

# Ex1

def u(n: int) -> int:
    if n < 2: return 1
    return 3 * u(n - 1) + u(n - 2)

# print(u(2))

# Ex2

def bin_to_dec(binaire: str, idx = 0, s = 0) -> int:
    if len(binaire) - 1 < idx: return s
    
    s += int(binaire[::-1][idx] + '0' * idx, 2)
    idx += 1
    
    return bin_to_dec(binaire, idx, s)

# print(bin_to_dec('1011'))

def dec_to_bin(dec: str, idx = 0, s = 0):
    if len(dec) - 1 < idx: return s
    
    s += int(dec[::-1][idx] + '0' * idx, 2)
    idx += 1
    
    return dec_to_bin(dec, idx, s)

print(dec_to_bin('5'))

# Ex3

def is_sorted(li: list) -> bool:
    if len(li) <= 1: return True
    
    if li[-1] < li[-2]: return False
    return is_sorted(li[:-2])
  
# print(is_sorted([1, 2, 3, 4, 4, 5, 7, 8]))
# print(is_sorted([11, 27, 39, 40, 49, 57, 71, 84]))

# Ex4

def maximum(li: list, m = 0):
    if not len(li): return m
    
    if li[-1] > m: m = li[-1]
    return maximum(li[:-1], m)

# print(maximum([9, 0, 7]))

# Ex5

def is_pal(mot: str) -> bool:
    mot = mot.lower()\
        .replace('\'', '')\
        .replace('-', '')\
        .replace(' ', '')
    
    if not mot: return True
    
    if mot[0] == mot[-1]: return is_pal(mot[1:-1])
    return False

# print(is_pal('KAYAK'))