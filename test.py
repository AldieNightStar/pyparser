import pyparser as pp

class OpToken:
	val = ""
	brackets = []
def test_next(t: str):
	op = pp.is_next_of(t, ["<<", "[[", "(("])
	if op == None:
		return None, 0
	close = "))"
	if op == "[[":
		close = "]]"
	elif op == "<<":
		close = ">>"
	subs = pp.read_until(t[2:], close)
	print("S", subs, t[2:], "CC", close)
	if subs == None:
		return None, 0
	print("S", subs)
	o = OpToken()
	o.val = subs
	o.brackets = [op, close]
	return o, len(subs) + 4
		

for (t, cnt) in pp.parse("aaba <<Test>>", test_next):
	if type(t) == OpToken:
		print(f"op: {t.val}  brackets: {t.brackets}")
	else:
		print(t)

print("<<< until_of test >>>")
a = "Tiller bin##00@@"
(text, id, subtext) = pp.read_until_of(a, ['00', '##', '@@'])
print(f"{text} == {id},{subtext}")
