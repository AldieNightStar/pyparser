from typing import Any, Generator, List, Tuple

class UnknownToken:
	value = ""
	def __init__(self, val) -> None:
		self.value = val
	def __repr__(self) -> str:
		return f"Unknown Token [{self.value}]"

def _parse(parsers: List, s: str) -> Tuple[Any, int]:
	for parser in parsers:
		token, cnt = parser(s)
		if cnt > 0:
			return token, cnt
	return None, 0

def parse(s: str, *parsers: List) -> Generator:
	cnt = 0
	while True:
		if len(s[cnt:]) < 1:
			break
		token, i = _parse([*parsers, _p_etc], s[cnt:])
		if i > 0:
			yield (token, i)
			cnt += i
		else:
			raise RuntimeError("Could not parse: " + s[cnt:])

_ETC_STR = "\n \r\t.,!@#$%^&*()_+{}[]:;\"'\\/|~`\0<>?-="
def _p_etc(s: str):
	arr = []
	for c in s:
		arr.append(c)
		if c in _ETC_STR:
			break
	return UnknownToken("".join(arr)), len(arr)