__author__ = 'bharathramh'
import random

def rand_from_name(first_name, last_name):
    return last_name[:3]+first_name[:3]+'_'+''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))

def rand_alphanumeric(length=100):
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(length))