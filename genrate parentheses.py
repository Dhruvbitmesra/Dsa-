def solve(ind, total, brackets, result):
    # base case: all positions filled
    if ind == len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return

    # if invalid state, stop
    if total < 0 or total > len(brackets) // 2:
        return

    # place '('
    brackets[ind] = "("
    solve(ind + 1, total + 1, brackets, result)

    # place ')'
    brackets[ind] = ")"
    solve(ind + 1, total - 1, brackets, result)


# driver code
ind = 0
total = 0
n = 3
brackets = [""] * (n * 2)
result = []

solve(ind, total, brackets, result)
print(result)
