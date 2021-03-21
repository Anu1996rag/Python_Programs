""" this module implements the concept of dutch flag partitioning """

def dutch_flag_partitioning(index,array_input):
    """
    bottom group : array_input[:smaller]
    middle group : array_input[smaller:equal]
    unclassified group : array_input[equal:larger]
    top group : array_input[larger:]
    :param index:
    :param array_input:
    :return: sorted array
    """
    pivot = array_input[index]
    print("Pivot element :",pivot)

    smaller, equal, larger = 0, 0, len(array_input)
    # keep iterating till there is an unclassified element
    while equal < larger:
        # array_input[equal] is the upcoming unclassified element
        if array_input[equal] < pivot:
            array_input[smaller], array_input[equal] = array_input[equal], array_input[smaller]
            smaller += 1
            equal += 1
        elif array_input[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            array_input[equal], array_input[larger] = array_input[larger], array_input[equal]

    return array_input


print(dutch_flag_partitioning(2,[0,2,1,2,1,2,2,1,2,1,2,2,1,1,2]))

