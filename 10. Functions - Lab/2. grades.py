def grade_in_words(grade):
    result = None
    if 2.00 <= grade_number <= 2.99:
        result = "Fail"
    elif 3 <= grade_number <= 3.49:
        result = "Poor"
    elif 3.50 <= grade_number <= 4.49:
        result = "Good"
    elif 4.50 <= grade_number <= 5.49:
        result = "Very Good"
    elif 5.50 <= grade_number <= 6.00:
        result = "Excellent"

    return result


grade_number = float(input())
print(grade_in_words(grade_number))
