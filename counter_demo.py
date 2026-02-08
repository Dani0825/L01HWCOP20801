from counter import Counter

tally = Counter()

tally.setLimit(2)

tally.reset()
tally.click()
tally.click()
tally.click()
tally.click()
tally.click()


result = tally.getValue()
print("Value", result)


