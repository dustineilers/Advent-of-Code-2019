
file = open('day1input.txt')

def fuel_required(mass) -> int:
    return (mass // 3) - 2

total_fuel = 0

for mass in file.readlines():
    fuel = fuel_required(int(mass))
    
    total_fuel += fuel

    additional_mass = fuel

    while (additional_fuel := fuel_required(additional_mass)) > 0:
        total_fuel += additional_fuel
        additional_mass = additional_fuel

print(total_fuel)