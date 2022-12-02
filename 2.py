input = open('advent-of-code-2022/2.txt').read().strip()
lines = input.split('\n')
score_mapping = {'A X': 1+3, 'A Y': 2+6, 'A Z': 3+0, 'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6, 'C X': 1+6, 'C Y': 2+0, 'C Z': 3+3}
correction = {'A X': 'A Z', 'A Y': 'A X', 'A Z': 'A Y', 'B X': 'B X', 'B Y': 'B Y', 'B Z': 'B Z', 'C X': 'C Y', 'C Y': 'C Z', 'C Z': 'C X'}
result = sum(score_mapping[correction[line]] for line in lines)
print(result)

#A X rock lose
#B Y paper draw
#C Z scisors win