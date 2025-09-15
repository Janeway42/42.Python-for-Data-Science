ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#array
ft_list[1] = "World"

#tulpe (fixed, must be rewriten)
ft_tuple = ft_tuple[:1] + ("The Netherlands",)

#set (unordered and does not support indexes)
ft_set.discard("tutu!")
ft_set.add("Amsterdam")

#dict
ft_dict["Hello"] = "Codam"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)