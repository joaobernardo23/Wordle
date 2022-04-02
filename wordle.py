#Best starting word (mathematically) for wordle, based on wordle's solutions


guesses = open("guesses.txt", "r")
solutions = open("solutions.txt", "r")


guess_lines = guesses.readlines()
sol_lines = solutions.readlines()

def solution_letters(sol):

    dict = {}
    
    for i in range(5):

        counter = 0
        for j in range(5):

            if (sol[i] == sol[j] and i!=j):
                counter  += 1

            if counter!=0:

                dict[sol[i]] = counter


    return dict


score_dict = {}

for line in guess_lines:

    if line == "\n":
        break
    
    score = 0 #0 points for non-existing letter, 1 point for yellow, 2.5 points for green
    for sol in sol_lines:

        if sol == "\n":
            break

        dict = solution_letters(sol)
        #print(dict)
        i = 0

        check_dict = {}
        for letter in line:


            if check_dict.__contains__(letter):
                pass
            else:
                check_dict[letter] = 0

            i += 1

            if i == 6:
                break

            j = 0
            count = 0
            for s_letter in sol:

                j += 1

                if j == 6:
                    break

                if (letter==s_letter and i==j):
                    score +=2.5
                    #print (str(score) + "   " + letter + "    UIIII")
                    check_dict[letter] += 1
                
                if (letter==s_letter and i!=j):
                    
                    if (s_letter!=line[j-1] and sol[i-1]!=letter):

                        if count != 0:
                            pass

                        else:

                            if dict.__contains__(s_letter):

                                #print(check_dict[letter])

                                if (check_dict[letter] != dict[s_letter] + 1):
                                    score +=1
                                    #print (str(score) + "   " + letter + "    YOOO")
                                    check_dict[letter] += 1

                            else:

                                if check_dict[letter] == 0:
                                    score +=1
                                    #print(str(score) + "   " + letter + "    YAAA")
                                
                                check_dict[letter] += 1

                        count += 1

    score_dict[line] = score                        

find_max_score = max(score_dict, key=score_dict.get)
print("Mathematically best starting word for wordle: " + find_max_score.upper())
guesses.close()
solutions.close()