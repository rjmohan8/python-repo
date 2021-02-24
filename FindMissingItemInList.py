from random import randint


def mylist_def():
    mylist = list(range(101))
    return mylist


def random_pop(alist):
    val = randint(0, 99)
    popped_item = alist.pop(val)
    # print(f"Popped Item is: {popped_item}")
    return alist


def identify_missing_val(blist):
    for item in range(100):
        try:
            if blist[item + 1] - blist[item] != 1:
                print(f"Missing item in list is: {blist[item]+1}")
        except IndexError:
            break
    #return blist

alist = mylist_def()
blist = random_pop(alist)
identify_missing_val(blist)
print(blist)