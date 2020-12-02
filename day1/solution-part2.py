#!/usr/bin/env python3.8

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
                if sum >= TARGET_VALUE:
                    continue
                else:
                    for deeper_addend_count, deeper_addend in enumerate(input):
                        if (deeper_addend_count != addend_count and deeper_addend_count != count):
                            deepsum = sum + deeper_addend
                            if deepsum == TARGET_VALUE:
                                deep_product = addend * item * deeper_addend
                                print(f"{item} - {addend} - {deeper_addend}")
                                print(deep_product)
                                break