def abbreviate(words):
    lst = words.replace('-',' ').replace(',',' ').replace(':',' ').replace('_',' ').split()
    j = ''
    for item in lst:
        j += item[0].upper()
    return j