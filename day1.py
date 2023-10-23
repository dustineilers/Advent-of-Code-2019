
file = open('day1input.txt')

def fuel_required(mass) -> int:
    return (mass // 3) - 2

total_fuel = 0

for mass in file.readlines():
    total_fuel += fuel_required(int(mass))

print(total_fuel)