def minion_game(string):
    # your code goes here
    # need a list of vowels 
    vowels = ["A", "E", "I", "O", "U"]
    ## stuart has to start with consonents so not in vowels
    ## kevin has to start wiht vowels, so in vowels
    ## game ends when both players have made all possible substrings
    ## points: +1 for each occurence of the substring in S
    ## prints the winners name and score. print(f"{w_name} {w_score}) or print("Draw")
    
    ## have 2 pointers, start and end
    ## identify if start is a vowel
    ## look for first substring in teh rest of the string
    ## if its not there, not need to continue with that letter
    ##### increment start
    ##### add + 1 to appropriate player
    ## else increment end, check again
    #####
    ## look for strings in substring
    score: dict = {'kevin': 0, 'stuart': 0}

    length = len(string)
    print(length)
    for i, value in enumerate(string):
        
        if value in vowels:
            score["kevin"] += length - i
        else:
            print(score)
            score["stuart"] += length - i
            print(score)

        print(score)
        
    if score["kevin"] > score["stuart"]:
        winner = "kevin"
        final_score = score["kevin"]
        print(f"{winner} {final_score}")

    elif score["kevin"] < score["stuart"]:
        winner = "stuart"
        final_score = score["stuart"]
        print(f"{winner} {final_score}")
    else:
        print("Draw")
    
    return
    
    

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)