def max_char(text:str)->str:
    if len(text)<=1:
        return text

    first=text[0]
    rest=text[1:len(text)]

    max_in_rest=max_char(rest)

    if first>=max_in_rest:
        return first
    else:
        return max_in_rest

