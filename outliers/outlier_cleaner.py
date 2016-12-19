#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import operator

    cleaned_data = []
    removed_data = []

    errors = (net_worths - predictions)**2
    for i in range(0, len(net_worths)):
        tupla = (ages[i][0], net_worths[i][0], errors[i][0])
        cleaned_data.append(tupla)

    cleaned_data.sort(key = operator.itemgetter(2), reverse=True)

    # remove 10% of total points
    n_points_to_remove = len(predictions) // 10

    for i in range(0, n_points_to_remove):
        # the point to remove is always at the top of the list
        removed_data.append(cleaned_data.pop(0))

    return cleaned_data, removed_data