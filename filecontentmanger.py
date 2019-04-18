

with  open('example.txt', 'r') as var:
	size = 10
	while (var.read()!=''):
		print(var.read(size))

