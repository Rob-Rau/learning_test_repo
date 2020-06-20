def foo_bar(foo):
	if foo:
		print("foo")
	else:
		print("bar")

def baz():
	print("baz")

foo_bar(True)
foo_bar(False)
baz()
