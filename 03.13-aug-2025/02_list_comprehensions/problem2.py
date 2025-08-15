blood_pressures = [134,145,169,180,130,120,130,124,110,150]

high_pressures = [pressure for pressure in blood_pressures if pressure >= 140]

print(high_pressures)