def validate_age(age):
    if len(age)==0:
        return "Empty input"
    elif not age.isdigit():
        return "Expected a number"
    elif not 0<int(age)<100:
        return "Expected 1-99"
    else:
        return age
