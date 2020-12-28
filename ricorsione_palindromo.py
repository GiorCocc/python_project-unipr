def palindrome(text: str) -> bool:
    if len(text)<=1:
        return True
    
    first=text[0]
    last=text[-1]
    
    if first!=last:
        return False

    inner=text[1:-1]

    return first==last and palindrome(inner)
