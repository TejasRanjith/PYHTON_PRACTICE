dict_num_words = {
    "0":"zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
    "100": "hundred",
    "1000": "thousand"
    # "10000": "ten thousand",
    # "100000": "hundred thousand",
    # "1000000": "million",
    # "10000000": "ten million",
    # "100000000": "hundred million",
    # "1000000000": "billion",
    # "10000000000": "ten billion",
    # "100000000000": "hundred billion",
    # "1000000000000": "trillion",
    # "10000000000000": "ten trillion",
    # "100000000000000": "hundred trillion",
    # "1000000000000000": "quadrillion",
    # "10000000000000000": "ten quadrillion",
    # "100000000000000000": "hundred quadrillion",
    # "1000000000000000000": "quintillion",
    # "10000000000000000000": "ten quintillion",
    # "100000000000000000000": "hundred quintillion",
    # "1000000000000000000000": "sextillion"
}


# a function to convert a number to a word from 0 to 10
def num_0_to_10():
    num = input("Please enter a number from 0 to 10: ")
    if num in dict_num_words:
        print(dict_num_words[num])
    else:
        print("Please enter a number from 0 to 10.")
        num_1_to_10()

def num_11_to_20():
    num = input("Please enter a number from 11 to 20: ")
    if num in dict_num_words:
        print(dict_num_words[num])
    else:
        print("Please enter a number from 11 to 20.")
        num_11_to_20()

def num_21_to_110():
    num_str = input("Number in string format: ")
    if 21 <= int(num_str) <= 110:
        num_list = list(num_str)
        num_list.reverse()
        new_num_list = []
        new_num_str = 0
        for i in range(len(num_list)):
            new_num_list.append(num_list[i]+"0"*i)
        # print(new_num_list)
        new_tup = tuple()
        keys = list(dict_num_words.keys())[28:]
        main_keys = keys.copy()
        keys.reverse();keys.extend(["10","1"]);keys.reverse()
        # print(keys)
        for i in range(len(new_num_list)):
            if int(new_num_list[i]) == 0:
                continue
            else:
                if new_num_list[i] in main_keys:
                    new_tup+= (dict_num_words[new_num_list[i]],)
                elif int(new_num_list[i]) % int(keys[i]) == 0 and keys[i] in main_keys:
                    # print(new_num_list[i],keys[i])
                    new_tup += (dict_num_words[keys[i]],dict_num_words[str(int(new_num_list[i]) // int(keys[i]))])
                else:
                    new_tup += (dict_num_words[new_num_list[i]],)
        new_list = list(new_tup)
        new_list.reverse()
        if 'zero' in new_list:
            new_list.remove('zero')
        result = ' '.join(new_list)
        print(result)

def num_111_to_120():
    pass