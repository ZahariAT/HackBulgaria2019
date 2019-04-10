#set, dict, ord dict -> all with {}

#import smth(func,class,var,etc.) from file as smth_else ## rename
'''
def f():
    from file import smth
    use smth only here
'''
import sys

def hangman(clue_word):
    print("Welcome to Hangman! Let's play!")
    clue_length = len(clue_word)
    guess_word = '-'*clue_length
    print(guess_word)
    guess_word = list(guess_word)
    count_incorrect = 0
    while count_incorrect < 10:
        if guess_word == list(clue_word):
            print("You won!")
            return
        print("Guess a letter:")
        letter = input()
        if letter in clue_word:
            #count_correct += 1
            for index in range(clue_length):
                if letter == clue_word[index]:
                    guess_word[index] = clue_word[index]
            print(''.join(guess_word))
        else:
            print("Incorrect")
            count_incorrect += 1


    print("You lost!")


    #return {(x, y):sum(map(sum, m)) for x in range(len(m)) for y in range(len(m[0]))}
def matrix_bombing_plan(m):
    result = {}
    s = 0
    for index,row in enumerate(m):
        for i,col in enumerate(row):
            s += col

    for index,row in enumerate(m):
        for i,col in enumerate(row):
            su = s
            lstngb = get_neighbors(index,i,m)
            current = []
            for x in lstngb:
                if(x >= m[index][i]):
                    x = x - m[index][i]
                    current.append(x)
                else:
                    x = 0
                    current.append(x)
            result[(index,i)] = su - (sum(lstngb) - sum(current))
    print(result)


def get_neighbors(a, b,matrix):
    d = {(i, c):matrix[i][c] for i in range(len(matrix)) for c in range(len(matrix[0]))}
    return list(filter(None, [d.get(i) for i in
    [(a+1, b+1), (a, b+1), (a+1, b), (a-1, b+1), (a-1, b), (a, b-1), (a+1, b-1),(a-1,b-1)]]))

   
#matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def main():
    #data = sys.argv[1]
    #hangman(data)
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    main()