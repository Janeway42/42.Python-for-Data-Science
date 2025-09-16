#function returns true or false 
#iterable is a sequence such as a list, tuple or string to be run through the above function
#the result is a filter object that can be converted to a lost or other collection

def ft_filter(function, iterable):
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError("iterable is not an iterable object")
        
        if function is not None and not callable(function):
            raise TypeError("function must be callable or else None")
        
        if function is None:
            return (item for item in iterable if item)
        
        return (item for item in iterable if function(item)) 
        
    except Exception as e:
        raise e
    


# testing: 

# iterable = [1, 2, 3 ,4, 5, 6, 7]

# def odd_or_even(number: int):
#     if number % 2 == 0:
#         return True
#     return False

# # recoded filter function
# ft_filtered = ft_filter(odd_or_even, iterable)
# for item in ft_filtered:
#     print(f"{item}")

# ft_filtered_list = list(ft_filter(odd_or_even, iterable))
# print(f"{list(ft_filtered_list)}\n")

# # recoded filter function None
# ft_filtered = ft_filter(None, iterable)
# for item in ft_filtered:
#     print(f"{item}")

# ft_filtered_list = list(ft_filter(None, iterable))
# print(f"{list(ft_filtered_list)}\n")

# # original filter function: 
# filtered = filter(odd_or_even, iterable)
# for item in filtered:
#     print(f"{item}")

# filtered_list = list(filter(odd_or_even, iterable))
# print(f"{list(filtered_list)}\n")

# #original None
# filtered = filter(None, iterable)
# for item in filtered:
#     print(f"{item}")

# filtered_list = list(filter(None, iterable))
# print(f"{list(filtered_list)}")

