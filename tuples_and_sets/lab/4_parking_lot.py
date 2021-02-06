n_commands = int(input())

parking_lot = set()

for _ in range(n_commands):

   command, plate = input().split(', ')

   if command == 'IN':
       parking_lot.add(plate)
   elif command == 'OUT':
       parking_lot.remove(plate)

if not parking_lot:
    print('Parking Lot is Empty')
else:
    [print(p) for p in parking_lot]

'''
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU
'''