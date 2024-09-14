#get_options_ratio and get_faculty_rating

def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    if ratio >=1:
        return "Total should be larger than option"
    elif ratio >= .9:
        return "Excellent"
    elif ratio > .8:
        return "Very Good"
    elif ratio > .7:
        return "Good"
    elif ratio > .6:
        return "Needs Improvement"
    elif ratio > .0 and ratio < .59:
        return "Unacceptable"