file = open("measurements.txt", "r")
paper_needed = 0
ribbon_needed = 0

def to_int(val):
    return int(val)

for line in file:
    dims = list(map(to_int, line.strip().split("x")))
    sides = [dims[0] * dims[1], dims[1] * dims[2], dims[0] * dims[2]]
    volume = (dims[0] * dims[1] * dims[2])
    
    paper_needed += (2 * sum(sides)) + min(sides)
    ribbon_needed += (2 * min(dims)) + (2 * (volume / min(dims) / max(dims)))
    ribbon_needed += volume # bow

print("Paper needed:", paper_needed)
print("Ribbon needed:", int(ribbon_needed))
input()