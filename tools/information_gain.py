import math

def get(parent_entropy, children_splitting):

    occurr = list_occurrences(children_splitting)
    weighted_entropy = 0

    for i in range(0, len(children_splitting)):
       e = entropy(children_splitting[i], occurr[i])
       weighted_entropy += e * occurr[i]

    weighted_entropy /= sum(occurr)
    return parent_entropy - weighted_entropy


def entropy(frequency_list, occurr):
    tot_occurr = occurr
    entropy = 0

    for c in frequency_list:   
        if c < 1: continue
        prob_c = c / tot_occurr
        entropy -= (prob_c * math.log2(prob_c))
    
    return entropy


def list_occurrences(list_of_lists):
    summa = []
    for l in list_of_lists:
        summa.append(sum(l))
    return summa