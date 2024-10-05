#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens
    pass

def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]
    pass