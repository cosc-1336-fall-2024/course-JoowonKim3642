#get_options_ratio and get_faculty_rating

def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    if ratio >= 1: #range not given
        return "Invalid Value"
    elif ratio >= .9:
        return "Excellent"
    elif ratio > .8:
        return "Very Good"
    elif ratio > .7:
        return "Good"
    elif ratio > .6:
        return "Needs Improvement"
    elif ratio >= .0 and ratio < .6:
        return "Unacceptable"
    else: #case of ratio .6, less than 0 (range not given)
        return "Invalid Value"