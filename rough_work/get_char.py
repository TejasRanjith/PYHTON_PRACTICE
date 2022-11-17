def get_char_at(filename, row, col):
    row = int(row)
    col = int(col)
    with open(filename) as f:
        lines = f.read().splitlines()
    if row >= len(lines):
        raise KeyError(f"File {filename} doesn't contain {row} lines")
    if col >= len(lines[row]):
        raise KeyError(f"Line {row} doesn't contain {col} characters")
    char =  lines[row][col]
    if row == 0:
        index = lines[row].index(char)
    else:
        index = len(lines[row])+(lines[row].index(char))
    return index, char
filename = input('Input file name: ')
row = input('Input row: ')
col = input('Input col: ')
index = get_char_at(filename, row, col)


with open(filename) as f:
    f.seek(index-1)
    f.read()