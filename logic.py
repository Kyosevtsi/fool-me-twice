from random import randint

def shuffle():
    n = len(pool)-1
    for i in range(1000):
        index1 = randint(0,n)
        index2 = randint(0,n)
        pool[index1], pool[index2] = pool[index2], pool[index1]



if __name__ == "__main__":
    sentence = "Sosi hui"
    correct = "Hi how are you"
    pool = [("Hi how are you", 0)]

    num_players = int(input("Enter number of players: "))
    scores = [0 for i in range(num_players+1)]
    choice = [[] for i in range(num_players+1)]

    for i in range(num_players):
        resp = input(f"Sentence: {sentence} \nEnter your approximation of the sentence: ")
        pool.append((resp, i+1))
    shuffle()
    print("The pool contains of these answers:")
    for i in range(len(pool)):
        print(f"{i+1}) {pool[i][0]}")
    
    for i in range(num_players):
        selection = int(input("Your choice: "))-1
        # print(pool[selection])
        choice[pool[selection][1]].append(i+1)
        # print(choice)
    # print(choice)
    print(f"Coorect answer: {correct}")
    # print(choice[0])
    for player in choice[0]:
        print(player)
        scores[player] += 2
    
    for i in range(len(choice)):
        scores[i] += len(choice[i])
        # print(scores)
    

    print(scores)
