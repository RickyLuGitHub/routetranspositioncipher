"""
string, (column, rows), direction
string_bool = false
for num characters in input:
    check for quotation mark
    if input[0] == "
        string_bool != string_bool
        check if input[x] is word

"""
punctuation = " .,:;!?/'-"
test = "This is an example (16, 3) clockwise"
rot_keywords = ["CLOCKWISE", "COUNTER-CLOCKWISE"]
grid_start = 0
grid_end = 0

# breaks up input string into the message, grid size, and rotation
def break_input(input_string):
    for i in range(len(input_string)):
        if input_string[i] == '(':
            grid_start = i+1
        elif input_string[i] == ')':
            grid_end = i

    cipher_string = input_string[0:grid_start-2]
    rotation = input_string[grid_end+2:]
    grid_dim_string = input_string[grid_start:grid_end]
    cipher = ''
    # cipher = []

    # for k in range(len(cipher_string)):
    #     if cipher_string[k].isalpha():
    #         cipher += (cipher_string[k])
    #         # cipher.append(cipher_string[k])
    for k in cipher_string:
        if k.isalpha():
            cipher += k.upper()
            # cipher.append(k]


    for j in range(len(grid_dim_string)):
        if not grid_dim_string[j].isalnum():
            grid_x = grid_dim_string[0:j-1]
            grid_y = grid_dim_string[j+1:] 
    grid = []
    grid.append(int(grid_x))
    grid.append(int(grid_y))

    return(cipher, grid, rotation)
    
print(break_input(test))
