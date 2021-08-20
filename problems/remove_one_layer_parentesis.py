"""

Given a valid parenthesis string (with only '(' and ')', an open parenthesis will always end with a close parenthesis, and a close parenthesis will never start first), 
remove the outermost layers of the parenthesis string and return the new parenthesis string.

If the string has multiple outer layer parenthesis (ie (())()), remove all outer layers and construct the new string. So in the example, 
the string can be broken down into (()) + (). By removing both components outer layer we are left with () + '' which is simply (), 
thus the answer for that input would be ().

"""

def kick_outers(string: str):
  string = string.replace(" ","")
  OPEN = "("
  CLOSE= ")"
  
  MATCHES = dict(zip(CLOSE,OPEN))

  open_stack = list()
  outers = list()

  for i, char in enumerate(string):
    if char == OPEN:
      elem = (i, char,)
      open_stack.append(elem)
    elif char == CLOSE:
      assert open_stack
      i_match, match = open_stack.pop()
      assert match == MATCHES[char]
      if not open_stack:
        ## IS OUTER! ##
        outers.append(i_match)
        outers.append(i)

  l_str = list(string)
  for idx in outers[::-1]:    
    l_str.pop(idx)


  return "".join(l_str)

if __name__ == "__main__":
  print(kick_outers("()()(())(())"))

        
