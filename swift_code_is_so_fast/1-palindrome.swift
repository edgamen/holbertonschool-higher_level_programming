// Return true if string is palindrome, otherwise return false
func is_palindrome(s: String) -> Bool {
  var a_index = s.startIndex
  var b_index = s.endIndex.predecessor()
  
  /* to check what is represented by index values:
  print (a_index), print (b_index) */
  while a_index < b_index {
    if s[a_index] == s[b_index] {
      a_index = a_index.successor()
      b_index = b_index.predecessor()
    }
    else {
      return false
    }
  }
  return true
}
