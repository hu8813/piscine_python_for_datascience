def all_thing_is_obj(object: any) -> int:
	try:
		if object and type(object):
			if isinstance(object, str):
				print(object,"is in the kitchen :",type(object))
			elif isinstance(object, (list, tuple, set, dict)):
				print(type(object).__name__.title(),":",type(object))
			else:
				print("Type not found")
		else:
			print("Type not found")
	except Exception as e:
		print("An error occured " + str(e))
	return 42
