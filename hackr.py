def find_num(otherS, string):
    count = 0
    while string.find(otherS) >= 0:
        # print'---*---'
        # print string + '/' + otherS
        # print'---//---'
        count += 1
        string = string[string.find(otherS)+1:]
    # print'##%d##'%(count)
    return count

def minion_game(string):
    # your code goes here
    score_S = 0
    score_K = 0
    checked = []
    for j in range(0, len(string)):
        for i in range(j+1, len(string)+1):
            # print string[j:i]
            # print 'checked :'+str(checked)
            if string[j:i] in checked:
                continue
            if string[j:i] in string:
                checked.append(string[j:i])
                if string[j] in ['A', 'E', 'I', 'O', 'U']:
                    score_K += find_num(string[j:i], string)
                else:
                    score_S += find_num(string[j:i], string)
    if score_K > score_S:
        print 'Kevin'+' '+ str(score_K)
    elif score_K < score_S:
        print 'Stuart'+' '+ str(score_S)
    else:
        print 'Draw'

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
