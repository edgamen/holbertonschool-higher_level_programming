// Return the longest word in a text
func longest_word(text: String) -> String {
    let words = text.componentsSeparatedByString(" ")
    var longest = words[0]
    for i in 0...words.count - 1 {
        if words[i].characters.count > longest.characters.count {
            longest = words[i]
        }
    }

    return longest
}
