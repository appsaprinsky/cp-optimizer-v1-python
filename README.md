# cp-optimizer-v1-python
cp-optimizer-v1-python



Assuming each position in the 9-slot array represents a specific crew role, we can map it like this:

Slot	Role
0	    Purser (Chief Flight Attendant)
1	    Senior Flight Attendant
2	    Business Class Attendant
3	    Economy Class Lead Attendant
4	    Economy Class Attendant 1
5	    Economy Class Attendant 2
6	    Galley Operator
7	    Jumpseat Crew (Relief)
8	    Language Specialist Attendant



At the moment, we will assume three aircraft time and three different slices needed.

[1, 1, 0, 1, 1, 0, 0, 0, 0] Boeing 737-800
[1, 1, 0, 1, 2, 0, 0, 0, 0] Boeing 737 MAX 8
[1, 1, 1, 2, 3, 0, 0, 0, 0] Boeing 787-9
