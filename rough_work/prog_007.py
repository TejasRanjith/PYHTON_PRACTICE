def solution(x):
    new,alpha,rev = "","abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba"
    for elem in x:
        if not elem.isalpha() or elem.isupper():
            new+=elem
        else:
            if elem in alpha:new+=rev[alpha.index(elem)]
    return new,type(new)
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("AabcdefghijklmnopqrstuvwxyzZ"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))