class StringToken:
    value = ""
    quotes = ""

    def __init__(self, val, q) -> None:
        self.value = val
        self.quotes = q

    def __repr__(self) -> str:
        return f"StringToken: [{self.quotes}] [{self.value}]"


def parser_string(s: str) -> StringToken:
    if len(s) < 1:
        return None, 0
    q = s[0]
    if not q in "\"'`":
        return None, 0
    s = s[1:]
    arr = []
    additional = 2
    escaped = False
    for i in range(len(s)):
        c = s[i]
        if escaped:
            arr.append(c)
            escaped = False
            additional += 1
            continue
        if c == '\\':
            escaped = True
            continue
        if c == q:
            break
        arr.append(c)
    return StringToken("".join(arr), q), len(arr) + additional
