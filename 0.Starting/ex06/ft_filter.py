def ft_filter(filter, iterable, number):
    """Function ft_filter takes an iterable object and a number
Returns a list containing only the items
that furfil the lamda condition"""
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError("iterable is not an iterable object")

        return [item for item in iterable.split() if filter(item, number)]

    except Exception as e:
        raise e
