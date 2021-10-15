def bracket_validator(string: str) -> bool:
    
    """
    O(n) time complexity -> due to looping the string once.
    O(n) space complexity -> due to stack.
    
    Obs: pop/append operation at the top of stack is O(1).
    Assumes space complexity of OPEN/CLOSE is O(1) because
    there's a fixed amount of possible open/close brackets.
    """
    
    string = string.replace(" ","")
    
    OPEN = ["{","(","["]
    CLOSE = ["}",")","]"]
    
    MATCH = dict(zip(CLOSE,OPEN))
    
    open_stack = []
    for char in string:
        if char in OPEN:
            open_stack.append(char)
        
        elif char in CLOSE:
            if not open_stack:
                return False
            if not MATCH[char] == open_stack.pop():
                return False

    return True
            
                
if __name__=='__main__':
    test1 = "{ [] ( ) }"
    test2 = "{ [(] ) }"
    test3 = "{ [ }"
    test4 = "{ { { } } } } }"
    test5 = "{}{}{}()()[]"
    
    assert bracket_validator(test1)
    assert not bracket_validator(test2)
    assert not bracket_validator(test3)
    assert not bracket_validator(test4)
    assert bracket_validator(test5)
            
