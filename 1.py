input = open('advent-of-code-2022/1.txt').readlines()
lines = [line.strip('\n') for line in input]

def get_sums(lines):
    sums = []
    counter = 1

    current_sum = 0
    for line in lines:
        if line:
            current_sum += int(line)
        else:
            sums.append(current_sum)
            counter += 1
            current_sum = 0
    return sums

def get_top_sums(sums, top_counter):
    sorted_sums = sorted(sums)
    return sum(sorted_sums[len(sums)-top_counter:])

#print(get_top_sums(get_sums(lines),3))

input = open('advent-of-code-2022/1.txt').read().strip()
groups = input.split('\n\n')
sums = [[int(number) for number in group.split('\n')] for group in groups]
print(sums)