def get_input(request:list = [])->dict:
    """
    Get formatted input from user
    """
    ret = {}
    for req in request:
        ret[req] = input(f"{req}: ")
    return ret