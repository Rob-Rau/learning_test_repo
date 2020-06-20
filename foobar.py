def foo_bar(foo):
	if foo:
		print("bar")
	else:
		print("foo")

def baz():
	print("baz")

foo_bar(True)
foo_bar(False)
baz()
