def function():

	f_name = input("The full name of the file: ")

	f = open(f_name, "r")
	f.seek(0)
	content = f.read() 
	f.close()

	out = open(f_name, "w")
	out.write(content.upper())
	out.close()	


function()