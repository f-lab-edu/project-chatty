import re


def get_text(full_text: str, pattern: re.Pattern = re.compile(r"@\w+\s")):
    return re.sub(pattern, "", full_text, count=1)
