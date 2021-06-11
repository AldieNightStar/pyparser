# PyParser - Lexer miniframework

# Install

```
pip install git+https://github.com/AldieNightStar/pyparser.git
```

# Import

```py
import pyparser as pp
```



# Usage

```py
text = '''123 !"Hello!" "Hi\\"Jack\\" and Roe" "S'tiven"'''

for (token, cnt) in pp.parse(text, pp.parser_string):
	if type(token) == pp.StringToken:
		print(token.value)
	else:
		print(str(token))
```

# Parsers

## Parser until some subString
```py
p = pp.parser_until("@")

for (t, cnt) in pp.parse("xyz@111", p):
	print(t)

# Output:
# xyz
```

## Any of string-set parser
```py
p = pp.parser_any_of("abcdef")

for (t, cnt) in pp.parse("aabacaaff@babe", p):
	if type(t) == pp.AnyOfTag:
		print(t)

# Output:
# AnyOfTag(default): aabacaaff
# AnyOfTag(default): babe
```


# Custom parser

* Custom parser does `return token, cnt`
	* `cnt` - number of processed symbols
* If fail, `return None, 0`

```py
def number_parser(txt):
	cb = []
	for i in range(len(txt)):
		c = txt[i]
		if not c in "0123456789":
			break
		cb.append(c)
	t = "".join(cb)
	if len(t) < 1:
		return None, 0
	return int(t), len(cb)
```


```py
nums = "123 321 11"

# Test it
for (token, cnt) in pp.parse(p, number_parser):
	if type(token) == int:
		print("Number: " + str(token))
	else:
		print("UNKNOWN: " + str(token))
```

# Tools
```py
# Returns that next text is "Operation".
# True | False
isNextIsOp = pp.is_next(src, "operation")

# Returns one element from the list which will be next or None
# - If next element for ex is "del" then "del" will be returned
# - If none of elements is next string - then None will be returned
operations = pp.is_next_of(src, ["del", "rem", "create", "..."])

# Reads all text before "end" substring
# if substring "end" will not find - return None
text = pp.read_until(src, "end")

# Reads text before the closest substring from the list
# Returns tuple with 3 elements (str, int, str) or (None, None, None) if fails
#	- str: Text until closest substring
#	- int: Index of closest substring
#	- str: Closest substring
(text, id, subs) = pp.read_until_of(src, ["end", "stop", "proc"])
```