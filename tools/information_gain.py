import math

def information_gain(parent_entropy, children_occurrences):

    tot_occurr = sum(children_occurrences)
    children_entropy = 0

    for i in range(0, len(children_occurrences)):
        p_i = children_occurrences[i] / tot_occurr
        children_entropy += -(p_i * math.log2(p_i))*children_occurrences[i]

    children_entropy /= tot_occurr

    return 1 - children_entropy
