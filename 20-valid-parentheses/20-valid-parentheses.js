/**
 * @param {string} s
 * @return {boolean}
 */


const isValid = (s) => {
  // initialize empty stack 
  
  const stack = [];
  
  // iterate through string
  for (let i = 0; i < s.length; i++) {
    // check the type of s[i] to see if it's open
    if (s[i] === '(') {
      stack.push(')')
      
    } else if (s[i] === '[') {
      stack.push(']')

    } else if (s[i] === '{') {
      stack.push('}')
      
    } else if (s[i] !== stack.pop()) {
        return false
    
    }
  }

  return stack.length === 0
}