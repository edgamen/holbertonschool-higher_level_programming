// Return the factorial of a number
func factorial(N: Int) -> Int {
    if N < 0 {
      print("Invalid number")
      return -1
    }
    if N == 0 {
      return 1
    }

    return N * factorial(N - 1)
}
