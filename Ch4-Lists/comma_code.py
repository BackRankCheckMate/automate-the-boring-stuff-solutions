spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(spam):
    res = ''
    for i, item in enumerate(spam):
        res += item +", "

    print(res)

comma(spam)