def progressive(string, i_from, i_to) :

	prefix, sufix = string.split("*")

	for i in range(i_from, i_to+1) :
		print(f"{prefix}{i}{sufix}")


string = input("What is the stirng? [One '*' is required]\n")

i_from, i_to = input("What is the range? (extreme inclusive) [Only two integers are required]\n").split()

progressive(string, int(i_from), int(i_to))
