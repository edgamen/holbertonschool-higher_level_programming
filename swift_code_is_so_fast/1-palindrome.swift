// Return true if string is palindrome, otherwise return false
func is_palindrome(s: String) -> Bool {
  let reversed_s = String(s.characters.reverse())

  if reversed_s == s {
     return true
  }

  return false
}
