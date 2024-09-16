import numpy as np
import math

def pair_occurrences(matrix, a, b, valid_n_subs = None):
    n_subs = len(matrix[0])
    # print(n_subs)
    n_ques = len(matrix)
    # print(n_ques)

    occurrences = 0
    if valid_n_subs is None:
        if a == b:
            for row in matrix:
                count_a = row.count(a)
                n_pairs = math.comb(count_a, 2)*2
                occurrences += n_pairs / (n_subs - 1)
        else:
            for row in matrix:
                count_a = row.count(a)
                count_b = row.count(b)
                n_pairs = count_a * count_b
                occurrences += n_pairs/(n_subs-1)
    else:
        if a == b:
            r = 0
            for row in matrix:
                if valid_n_subs[r] > 1:
                    count_a = row.count(a)
                    n_pairs = math.comb(count_a, 2)*2
                    occurrences += n_pairs / (valid_n_subs[r] - 1)
                r += 1
        else:
            r = 0
            for row in matrix:
                if valid_n_subs[r] > 1:
                    count_a = row.count(a)
                    count_b = row.count(b)
                    n_pairs = count_a * count_b
                    occurrences += n_pairs/(valid_n_subs[r]-1)
                r += 1

    return occurrences

def coincidence_table(rating_matrix,possible_values, valid_n_subs = None):
    #print('possible_values',possible_values)
    #print('rating_matrix',rating_matrix)
    table_size = len(possible_values)
    table = np.zeros((table_size,table_size))
    list_n = []
    for r in range(table_size):
        for c in range(r,table_size):
            table[r, c] = pair_occurrences(rating_matrix, possible_values[r], possible_values[c], valid_n_subs)
            table[c, r] = pair_occurrences(rating_matrix, possible_values[r], possible_values[c], valid_n_subs)

    for r in range(table_size):
        list_n.append(np.sum(table[r,:]))
    total_n = sum(list_n)
    return table, list_n, total_n

def delta_matrix(possible_values,criterion,rating_matrix):
    size = len(possible_values)
    delta = np.zeros((size, size))
    if criterion == 'nominal':
        for r in range(size):
            for c in range(size):
                if not r == c:
                    delta[r, c] = 1
                    delta[c, r] = 1
    elif criterion == 'interval':
        for r in range(size):
            for c in range(r, size):
                index = abs(r-c)
                delta[r, c] = index * index
                delta[c, r] = index * index
    elif criterion == 'ordinal':
        for r in range(size):
            for c in range(r, size):
                value_counts = [0] * len(possible_values)
                for row in rating_matrix:
                    for value in row:
                        if value in possible_values:
                            index = possible_values.index(value)
                            value_counts[index] += 1
                        else:
                            print('value not included in possible_values')

                start_index = min(r, c)
                end_index = max(r, c) + 1

                theValue = sum(value_counts[start_index:end_index]) - (value_counts[r]+value_counts[c])/2
                delta[r, c] = theValue*theValue

    return delta

def krippendorff_alpha(rating_matrix,possible_values,criterion, missing_data = False):
    """
    Krippendorff's alpha is a statistic to measure the inter-subject agreement in ratings. First, a coincidence table is
    built based on the rating matrix. Then, the degree of disagreement is calculated based on the coincidence table and
    a difference function (AKA delta squared matrix). Finally, Krippendorff's alpha is calculated according to the observed degree of disagreement
    and the expected degree of disagreement given random rating scores.

    PARAMS
    rating_matrix:      list, shape (n_ques,n_subs)
    possible_values:    list, recording all possible values that may appear in rating_matrix
    criterion:          str, what type of difference function is applied. should be one of below:
                            'nominal';    'interval';    'ordinal'.
    missing_data:       boolean, whether there are data missing.

    RETURNS
    a number, the Krippendorff's alpha.

    PRINTS
    total_n, it should be equal or very close to number of elements in rating_matrix,
        otherwise something goes wrong.
    """

    n_subs = len(rating_matrix[0])
    # print(n_subs)
    n_ques = len(rating_matrix)
    # print(n_ques)

    if missing_data:
        valid_n_subs = []
        for row in rating_matrix:
            row_length = len(row)
            valid_n_subs.append(row_length)
        coincidence,list_n,total_n = coincidence_table(rating_matrix, possible_values, valid_n_subs)

    else:
        coincidence, list_n, total_n = coincidence_table(rating_matrix, possible_values)

    print('total_n',total_n)
    #print(coincidence)
    delta = delta_matrix(possible_values,criterion,rating_matrix)
    numerator = 0
    denominator = 0
    for r in range(len(possible_values)):
        for c in range(r+1, len(possible_values)):
            numerator += coincidence[r,c] * delta[r,c]

    for i in range(len(possible_values)-1):
        inner = 0
        for j in range(i+1,len(possible_values)):
            inner += list_n[j] * delta[i,j]
        denominator += list_n[i] * inner
    # print('list_n',list_n)
    # print('denominator',denominator)

    alpha = 1 - (total_n - 1)*(numerator/denominator)
    return alpha


