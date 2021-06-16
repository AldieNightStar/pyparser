from typing import List, Tuple, cast

def read_while(text: str, set: str):
	for i in range(len(text)):
		if not text[i] in set:
			break
	return text[:i]

def is_next(text: str, subtext: str):
	return text[0:len(subtext)] == subtext

def is_next_of(text: str, list: List[str]):
	for l in list:
		if is_next(text, l):
			return l
	return None

def read_until(text: str, subtext: str):
	try:
		ind = text.index(subtext)
		return text[0:ind]
	except ValueError:
		return None

def read_until_of(text: str, list: List[str]) -> Tuple[str, int, str]:
	indexes : List[Tuple[int, str]] = []
	for l in list:
		try:
			ind = text.index(l)
			indexes.append((ind, l))
		except ValueError:
			pass
	if len(indexes) < 1:
		return None, None, None
	lower = 0xFFFFFFFF
	lowerText = ""
	for elem in indexes:
		ind, t = elem
		if ind < lower:
			lower = ind
			lowerText = t
	return text[0:lower], lower, lowerText