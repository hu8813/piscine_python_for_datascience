ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

try:
	ft_list[1] = "World"
	ft_tuple=(ft_tuple[0],"Austria")
	ft_set.discard("tutu!") # discard is safer then remove for the case tutu! not exist
	ft_set.add("Vienna")
	ft_dict["Hello"] = "42Vienna"
except Exception as e:
	print("An error occured " + str(e))

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

