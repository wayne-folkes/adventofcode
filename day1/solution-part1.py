#!/usr/bin/env python3

TARGET_VALUE = 2020

def load_input():
    input = open("input.txt","r").read().splitlines()
    return [int(x) for x in input]

if __name__ == "__main__":
    input = load_input()
    # import pdb; pdb.set_trace()
    for count, item in enumerate(input):
        # print("%s - %s" % (item, count))
        for addend_count, addend in enumerate(input):
            if addend_count != count:
                sum = item + addend
                # print(sum)
                if sum == TARGET_VALUE:
                    product = addend * item
                    print("%s - %s" % (item, addend))
                    print(product)
                    break