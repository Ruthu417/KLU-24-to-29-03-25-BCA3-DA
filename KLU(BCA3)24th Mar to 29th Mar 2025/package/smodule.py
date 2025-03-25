def is_palindrome(st):
    if st==st[::-1]:
        return True
    else:
        return False
    
#is_palindrome()
def frequency(st,ch):
    if ch in st:
        return st.count(ch)
    
#frequency()