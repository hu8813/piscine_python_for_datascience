def NULL_not_found(object: any) -> int:
	try:
		if type(object):
			if isinstance(object, (str, int, bool, float)):
				print(object,":", type(object).__name__.title(),":",type(object))
			else:
				print("Type not found")
		else:
			print("Type not found")
	except Exception as e:
		print("An error occured " + str(e))
		
	return 1
