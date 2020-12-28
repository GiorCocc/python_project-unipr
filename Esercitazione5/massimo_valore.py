massimo=""

def max_val(text:str):
    global massimo
    
    if len(text)<=1:
        return massimo

    resto=text[1:len(text)]
    
    if text[0]>=massimo:
        massimo=text[0]
  
    return max_val(resto)

def main():
    stringa=str(input("Scrivi qualcosa: "))
    print(max_val(stringa))

main()