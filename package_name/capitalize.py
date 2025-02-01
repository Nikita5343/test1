def capitalize(text):
    if text == "":
        return ""
    upp = text[0].upper()
    return f"{upp}{text[1:]}"

# print(capitalize("hello"))