

#if negative return true else return False
def has_negative_values(lst : list[int]) ->bool:
    for item in lst:
        if item <= -1:
            return True
    return False 
#use Set  to make list an iterable sequence
def conforms_to_a_die(lst : list[int]) ->int:
    n = len(lst)
    num_set = set(range(1, n + 1))
    return set(lst) == num_set
#check to make sure list does not  go down
def is_monotonically_increasing(ps_dict: dict[str, int]) -> bool:
    values = list(ps_dict.values())
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True
