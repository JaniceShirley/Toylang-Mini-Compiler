import re

# Token types and patterns
TOKENS = [
    ("LET", r"let"),
    ("PRINT", r"print"),
    ("NUMBER", r"\d+"),
    ("IDENTIFIER", r"[a-zA-Z_]\w*"),
    ("EQUAL", r"="),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("SKIP", r"[ \t\n]+"),  # spaces/newlines
]

def tokenize(code):
    tokens = []

    while code:
        match = None

        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code)

            if match:
                text = match.group(0)

                if token_type != "SKIP":
                    tokens.append((token_type, text))

                code = code[len(text):]
                break

        if not match:
            raise SyntaxError("Invalid character: " + code[0])

    return tokens