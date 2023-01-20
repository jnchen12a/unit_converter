from random import randint

#Wheels, 95 items each
owheel1_1 = ('v', 'j', '1', '6', '5', '@', '8', 'M', 'Y', 'y', '_', 'n', 'L', '|', '4', 'O', '{', 'F', 'V', '<', ',', 'T', 't', ':', '=', 'J', '2', 'm', 'R', 'z', 'K', '/', 'H', 'W', ']', 'g', 'B', 'x', 'Z', 'i', '0', '?', 'U', '%', ';', '!', 'Q', 'e', '#', 'w', 'o', '>', 'I', '7', 'q', '(', '}', ' ', '\\', '.', '`', '3', 'S', '*', 'c', 'b', 'l', 'N', "'", 'A', 'C', '9', 's', 'r', 'h', 'E', '+', 'd', '$', 'P', '-', 'u', 'X', 'f', '~', '"', 'a', '^', 'k', 'D', ')', '[', 'p', 'G', '&')
owheel1_2 = ("w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'")
wheel1_2 = ["w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'"]

owheel2_1 = ('x', 'X', '$', 's', 'L', 'e', 'V', '*', 'G', '`', '{', 'c', 'Y', '(', 'm', 'r', '7', '2', 'Z', '?', '^', 'h', '1', 'P', 'q', 'j', 'O', '+', '@', '"', '#', '%', 'A', 'u', 'H', 'F', '}', 'W', 't', 'U', 'b', '3', 'g', '/', 'B', 'R', 'M', 'v', 'i', '!', ':', ')', '|', 'S', 'J', '=', 'C', '.', '&', ' ', 'z', '\\', '[', '5', 'k', ',', 'l', "'", 'w', 'y', 'T', '-', 'E', '>', 'I', ';', 'd', 'Q', 'n', '~', '_', 'p', '8', '4', 'N', '<', 'o', ']', '6', 'f', 'K', '0', 'D', 'a', '9')
owheel2_2 = ('(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N')
wheel2_2 = ['(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N']

owheel3_1 = ('&', '*', '_', 'z', 'c', '}', 'V', 'n', 'r', 'W', '2', '+', 'U', 'Q', 'v', '@', 'w', '(', 'T', '0', 'X', 'O', 'K', '>', '!', 'i', '^', '`', ';', 'A', 'P', '-', '1', '8', "'", '=', 'o', '3', ',', 'k', 't', ')', 'p', '$', 'D', 'F', '%', ']', '4', 'm', 'B', 'j', '~', '"', 'a', 'N', '?', 'S', 'e', '|', ':', '5', 's', 'g', '{', 'y', 'q', 'I', 'u', '#', 'C', 'f', '<', ' ', 'L', 'b', 'Z', '/', '9', 'H', '.', 'h', 'd', '6', '7', 'l', 'R', 'G', '\\', 'E', 'J', 'Y', 'M', '[', 'x')
owheel3_2 = ('>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i')
wheel3_2 = ['>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i']

wheel1_2moves = 0
wheel2_2moves = 0

#Decoding function
def decoding_function(message):
    global owheel1_1
    global owheel1_2
    global wheel1_2
    global owheel2_1
    global owheel2_2
    global wheel2_2
    global owheel3_1
    global owheel3_2
    global wheel3_2
    global wheel1_2moves
    global wheel2_2moves

    returnmes = ""
    wheel1_2moves = 0
    wheel2_2moves = 0

    message = list(message)

    value1 = message.pop(0)
    value2 = message.pop(0)
    value3 = message.pop(0)

    value1 = owheel1_1.index(value1)
    value2 = owheel1_1.index(value2)
    value3 = owheel1_1.index(value3)

    startshift = value1 + (value2 * 95) + (value3 * 9025)

    shiftwheel(startshift)

    #Decoding actual 
    for character in message:
        index = wheel3_2.index(character)
        newchar = owheel3_1[index]

        index = wheel2_2.index(newchar)
        newchar = owheel2_1[index]

        index = wheel1_2.index(newchar)
        newchar = owheel1_1[index]

        returnmes += newchar
        shiftwheel(1)

    wheel1_2 = list(owheel1_2)
    wheel2_2 = list(owheel2_2)
    wheel3_2 = list(owheel3_2)
    
    return returnmes

#Shifting wheel function
def shiftwheel(times):
    global wheel1_2moves
    global wheel2_2moves

    global wheel1_2
    global wheel2_2
    global wheel3_2
    
    for n in range(times):
        endchar = wheel1_2.pop()
        wheel1_2.insert(0, endchar)
        wheel1_2moves += 1
        if wheel1_2moves == 95:
            endchar = wheel2_2.pop()
            wheel2_2.insert(0, endchar)
            wheel2_2moves += 1
            wheel1_2moves = 0
        if wheel2_2moves == 95:
            endchar = wheel3_2.pop()
            wheel3_2.insert(0, endchar)
            wheel2_2moves = 0