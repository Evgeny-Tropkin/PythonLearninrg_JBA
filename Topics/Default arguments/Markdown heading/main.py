def heading(text, level=1):
    if level < 1:
        level = 1
    if level > 6:
        level = 6
    hash_tags = "#" * level
    return f"{hash_tags} {text}"
