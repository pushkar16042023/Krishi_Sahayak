import re

cities = {"Andhra Pradesh":"""Fertilizers:\n
1) Carbendazim (Rs 350 per kg)
2) Malathion (Rs 300 per liter)
3) Dimethoate (Rs 250 per liter)
4) Carbofuran (Rs 600 per kg)
5) Chlorantraniliprole (Rs 1500 per liter)
6) Cypermethrin (Rs 300 per liter)
7) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
8) MTU 1010 (Rs 50 per kg)
9) Jaya (Rs 55 per kg)
10) IR 64 (Rs 60 per kg)
11) BPT 5204 (Rs 65 per kg)
12) HD 2967 (Rs 75 per kg)
13) HI 1544 (Rs 80 per kg)
14) Swarna (Rs 50 per kg)
15) Indrayani (Rs 70 per kg)
16) JS 335 (Rs 65 per kg)
17) MACS 124 (Rs 70 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)
22) Bunny Bt (Rs 200 per kg)
23) RCH 2 Bt (Rs 220 per kg)
24) Co 86032 (Rs 30 per piece)
25) Co 0238 (Rs 35 per piece)""",
         
"Arunachal Pradesh":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) Gypsum (Rs 200)

Pesticides:
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Monocrotophos (Rs 180 per liter)
10) Mancozeb (Rs 400 per kg)
11) Carbendazim (Rs 350 per kg)
12) Malathion (Rs 300 per liter)
13) Dimethoate (Rs 250 per liter)
14) Carbofuran (Rs 600 per kg)
15) Chlorantraniliprole (Rs 1500 per liter)
16) Cypermethrin (Rs 300 per liter)
17) Cartap hydrochloride (Rs 200 per kg)

Seeds:
18) CAU R1 (Rs 70 per kg)
19) RC Maniphou-7 (Rs 75 per kg)
20) P 44 (Rs 60 per kg)
21) JG 11 (Rs 65 per kg)
22) HQPM 1 (Rs 100 per kg)
23) P 3396 (Rs 120 per kg)""",

"Assam":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Cartap hydrochloride (Rs 200 per kg)
12) Carbofuran (Rs 600 per kg)
13) Monocrotophos (Rs 180 per liter)
14) Chlorantraniliprole (Rs 1500 per liter)
15) Cypermethrin (Rs 300 per liter)

Seeds:
16) MTU 1010 (Rs 50 per kg)
17) Jaya (Rs 55 per kg)
18) BPT 5204 (Rs 65 per kg)
19) P 44 (Rs 60 per kg)
20) JG 11 (Rs 65 per kg)
21) HQPM 1 (Rs 100 per kg)
22) P 3396 (Rs 120 per kg)
23) TV 1 (Rs 90 per kg)
24) UPASI 9 (Rs 100 per kg)""",
         
"Bihar":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Malathion (Rs 300 per liter)
11) Dimethoate (Rs 250 per liter)
12) Carbofuran (Rs 600 per kg)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) Swarna (Rs 50 per kg)
17) IR 64 (Rs 60 per kg)
18) BPT 5204 (Rs 65 per kg)
19) HD 2967 (Rs 75 per kg)
20) HI 1544 (Rs 80 per kg)
21) JS 335 (Rs 65 per kg)
22) MACS 124 (Rs 70 per kg)
23) P 44 (Rs 60 per kg)
24) JG 11 (Rs 65 per kg)
25) HQPM 1 (Rs 100 per kg)
26) P 3396 (Rs 120 per kg)
27) Bunny Bt (Rs 200 per kg)
28) RCH 2 Bt (Rs 220 per kg)
29) Co 86032 (Rs 30 per piece)
30) Co 0238 (Rs 35 per piece)""",
        
"Chattisgarh":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Malathion (Rs 300 per liter)
11) Dimethoate (Rs 250 per liter)
12) Carbofuran (Rs 600 per kg)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) MTU 1010 (Rs 50 per kg)
17) Swarna (Rs 50 per kg)
18) IR 64 (Rs 60 per kg)
19) BPT 5204 (Rs 65 per kg)
20) HD 2967 (Rs 75 per kg)
21) HI 1544 (Rs 80 per kg)
22) JS 335 (Rs 65 per kg)
23) MACS 124 (Rs 70 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) HQPM 1 (Rs 100 per kg)
27) P 3396 (Rs 120 per kg)
28) Bunny Bt (Rs 200 per kg)
29) RCH 2 Bt (Rs 220 per kg)
30) Co 86032 (Rs 30 per piece)
31) Co 0238 (Rs 35 per piece)""",
         
         
"Goa":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) MTU 1010 (Rs 50 per kg)
16) Jaya (Rs 55 per kg)
17) IR 64 (Rs 60 per kg)
18) BPT 5204 (Rs 65 per kg)
19) HD 2967 (Rs 75 per kg)
20) HI 1544 (Rs 80 per kg)
21) Swarna (Rs 50 per kg)
22) Indrayani (Rs 70 per kg)
23) JS 335 (Rs 65 per kg)
24) MACS 124 (Rs 70 per kg)
25) P 44 (Rs 60 per kg)
26) JG 11 (Rs 65 per kg)
27) HQPM 1 (Rs 100 per kg)
28) P 3396 (Rs 120 per kg)
29) Bunny Bt (Rs 200 per kg)
30) RCH 2 Bt (Rs 220 per kg)
31) Co 86032 (Rs 30 per piece)
32) Co 0238 (Rs 35 per piece)""",
         
"Gujarat":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n

15) Hybrid 4 (Rs 45 per kg)
16) Gujarat 1 (Rs 50 per kg)
17) Anand 2 (Rs 55 per kg)
18) BG 1 (Rs 60 per kg)
19) K 6 (Rs 65 per kg)
20) Dhan 8 (Rs 70 per kg)
21) RCH 7 (Rs 75 per kg)
22) H 9 (Rs 80 per kg)
23) Raj 2 (Rs 85 per kg)
24) RR 5 (Rs 90 per kg)
25) RG 6 (Rs 95 per kg)
26) B 1 (Rs 100 per kg)
27) J 4 (Rs 110 per kg)
28) SB 11 (Rs 120 per kg)
29) MG 13 (Rs 130 per kg)
30) KM 7 (Rs 140 per kg)""",
         
         
"Haryana":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n

6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) HD 2967 (Rs 75 per kg)
16) HI 1544 (Rs 80 per kg)
17) PBW 343 (Rs 85 per kg)
18) Co 86032 (Rs 30 per piece)
19) Co 0238 (Rs 35 per piece)
20) Bunny Bt (Rs 200 per kg)
21) RCH 2 Bt (Rs 220 per kg)
22) RD 2660 (Rs 230 per kg)
23) RD 2552 (Rs 240 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) CoFS 29 (Rs 250 per kg)
27) CoFS 32 (Rs 260 per kg)
28) CoFS 36 (Rs 270 per kg)
29) W 306 (Rs 280 per kg)
30) WH 1105 (Rs 290 per kg)""",
         
"Himachal Pradesh":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n

6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) K 332 (Rs 50 per kg)
16) K 114 (Rs 55 per kg)
17) K 212 (Rs 60 per kg)
18) K 155 (Rs 65 per kg)
19) K 419 (Rs 70 per kg)
20) K 231 (Rs 75 per kg)
21) K 215 (Rs 80 per kg)
22) K 275 (Rs 85 per kg)
23) K 129 (Rs 90 per kg)
24) K 220 (Rs 95 per kg)
25) K 298 (Rs 100 per kg)
26) K 382 (Rs 110 per kg)
27) K 111 (Rs 120 per kg)
28) K 385 (Rs 130 per kg)
29) K 308 (Rs 140 per kg)""",
         
"Jharkhand":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) MTU 1010 (Rs 50 per kg)
16) Jaya (Rs 55 per kg)
17) BPT 5204 (Rs 65 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)
22) TV 1 (Rs 90 per kg)
23) UPASI 9 (Rs 100 per kg)""",
         
"Karnataka":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) MTU 1010 (Rs 50 per kg)
17) Jaya (Rs 55 per kg)
18) BPT 5204 (Rs 65 per kg)
19) P 44 (Rs 60 per kg)
20) JG 11 (Rs 65 per kg)
21) HQPM 1 (Rs 100 per kg)
22) P 3396 (Rs 120 per kg)
23) Bunny Bt (Rs 200 per kg)
24) RCH 2 Bt (Rs 220 per kg)
25) Co 86032 (Rs 30 per piece)
26) Co 0238 (Rs 35 per piece)""",
         
         
"Kerala":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n

7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) Jaya (Rs 55 per kg)
17) R 109 (Rs 60 per kg)
18) VYT 3 (Rs 65 per kg)
19) VYT 4 (Rs 70 per kg)
20) R 109 (Rs 75 per kg)
21) R 109 (Rs 80 per kg)
22) R 109 (Rs 85 per kg)
23) R 109 (Rs 90 per kg)
24) R 109 (Rs 95 per kg)
25) R 109 (Rs 100 per kg)
26) R 109 (Rs 110 per kg)
27) R 109 (Rs 120 per kg)
28) R 109 (Rs 130 per kg)
29) R 109 (Rs 140 per kg)""",
         
"Madhya pradesh":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) MTU 1010 (Rs 50 per kg)
16) Jaya (Rs 55 per kg)
17) BPT 5204 (Rs 65 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)
22) Bunny Bt (Rs 200 per kg)
23) RCH 2 Bt (Rs 220 per kg)
24) Co 86032 (Rs 30 per piece)
25) Co 0238 (Rs 35 per piece)""",
         
"Maharashtra":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) MTU 1010 (Rs 50 per kg)
16) Jaya (Rs 55 per kg)
17) BPT 5204 (Rs 65 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)
22) Bunny Bt (Rs 200 per kg)
23) RCH 2 Bt (Rs 220 per kg)
24) Co 86032 (Rs 30 per piece)
25) Co 0238 (Rs 35 per piece)""",
         
         
"Manipur":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n

6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) CAU R1 (Rs 70 per kg)
16) RC Maniphou-7 (Rs 75 per kg)
17) P 44 (Rs 60 per kg)
18) JG 11 (Rs 65 per kg)
19) HQPM 1 (Rs 100 per kg)
20) P 3396 (Rs 120 per kg)""",
         
"Meghalaya":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) JG 11 (Rs 65 per kg)
16) HQPM 1 (Rs 100 per kg)
17) P 3396 (Rs 120 per kg)""",
         
"Mizoram":"""Fertilizers:\n
2) Urea (Rs 276)
3) DAP (Rs 1200)
4) MOP (Rs 1700)
5) SSP (Rs 400)
6) Potash (Rs 900)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) CAU R1 (Rs 70 per kg)
17) RC Maniphou-7 (Rs 75 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)""",
         
"Nagaland":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) CAU R1 (Rs 70 per kg)
16) RC Maniphou-7 (Rs 75 per kg)
17) P 44 (Rs 60 per kg)
18) JG 11 (Rs 65 per kg)
19) HQPM 1 (Rs 100 per kg)
20) P 3396 (Rs 120 per kg)""",
         
"Odisha":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) MTU 1010 (Rs 50 per kg)
16) Jaya (Rs 55 per kg)
17) BPT 5204 (Rs 65 per kg)
18) P 44 (Rs 60 per kg)
19) JG 11 (Rs 65 per kg)
20) HQPM 1 (Rs 100 per kg)
21) P 3396 (Rs 120 per kg)""",
         
"Punjab":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) HD 2967 (Rs 75 per kg)
17) HI 1544 (Rs 80 per kg)
18) PBW 343 (Rs 85 per kg)
19) Co 86032 (Rs 30 per piece)
20) Co 0238 (Rs 35 per piece)
21) Bunny Bt (Rs 200 per kg)
22) RCH 2 Bt (Rs 220 per kg)
23) RD 2660 (Rs 230 per kg)
24) RD 2552 (Rs 240 per kg)
25) P 44 (Rs 60 per kg)
26) JG 11 (Rs 65 per kg)
27) CoFS 29 (Rs 250 per kg)
28) CoFS 32 (Rs 260 per kg)
29) CoFS 36 (Rs 270 per kg)
30) W 306 (Rs 280 per kg)
31) WH 1105 (Rs 290 per kg)""",
         
         
"Rajasthan":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) HD 2967 (Rs 75 per kg)
17) HI 1544 (Rs 80 per kg)
18) PBW 343 (Rs 85 per kg)
19) Co 86032 (Rs 30 per piece)
20) Co 0238 (Rs 35 per piece)
21) Bunny Bt (Rs 200 per kg)
22) RCH 2 Bt (Rs 220 per kg)
23) RD 2660 (Rs 230 per kg)
24) RD 2552 (Rs 240 per kg)
25) P 44 (Rs 60 per kg)
26) JG 11 (Rs 65 per kg)
27) CoFS 29 (Rs 250 per kg)
28) CoFS 32 (Rs 260 per kg)
29) CoFS 36 (Rs 270 per kg)
30) W 306 (Rs 280 per kg)
31) WH 1105 (Rs 290 per kg)""",
         
         
"Sikkim":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) HD 2967 (Rs 75 per kg)
16) HI 1544 (Rs 80 per kg)
17) PBW 343 (Rs 85 per kg)
18) Co 86032 (Rs 30 per piece)
19) Co 0238 (Rs 35 per piece)
20) Bunny Bt (Rs 200 per kg)
21) RCH 2 Bt (Rs 220 per kg)
22) RD 2660 (Rs 230 per kg)
23) RD 2552 (Rs 240 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) CoFS 29 (Rs 250 per kg)
27) CoFS 32 (Rs 260 per kg)
28) CoFS 36 (Rs 270 per kg)
29) W 306 (Rs 280 per kg)
30) WH 1105 (Rs 290 per kg)""",
         
"Tamil nadu":"""Fertilizers:\n

1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n

6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n

15) HD 2967 (Rs 75 per kg)
16) HI 1544 (Rs 80 per kg)
17) PBW 343 (Rs 85 per kg)
18) Co 86032 (Rs 30 per piece)
19) Co 0238 (Rs 35 per piece)
20) Bunny Bt (Rs 200 per kg)
21) RCH 2 Bt (Rs 220 per kg)
22) RD 2660 (Rs 230 per kg)
23) RD 2552 (Rs 240 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) CoFS 29 (Rs 250 per kg)
27) CoFS 32 (Rs 260 per kg)
28) CoFS 36 (Rs 270 per kg)
29) W 306 (Rs 280 per kg)
30) WH 1105 (Rs 290 per kg)""",
         
"Telangana":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) HD 2967 (Rs 75 per kg)
16) HI 1544 (Rs 80 per kg)
17) PBW 343 (Rs 85 per kg)
18) Co 86032 (Rs 30 per piece)
19) Co 0238 (Rs 35 per piece)
20) Bunny Bt (Rs 200 per kg)
21) RCH 2 Bt (Rs 220 per kg)
22) RD 2660 (Rs 230 per kg)
23) RD 2552 (Rs 240 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) CoFS 29 (Rs 250 per kg)
27) CoFS 32 (Rs 260 per kg)
28) CoFS 36 (Rs 270 per kg)
29) W 306 (Rs 280 per kg)
30) WH 1105 (Rs 290 per kg)""",
         
         
"Tripura":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) CAU R1 (Rs 70 per kg)
16) RC Maniphou-7 (Rs 75 per kg)
17) P 44 (Rs 60 per kg)
18) JG 11 (Rs 65 per kg)
19) HQPM 1 (Rs 100 per kg)
20) P 3396 (Rs 120 per kg)""",
         
"Uttar pradesh":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) Swarna (Rs 55 per kg)
16) IR 64 (Rs 60 per kg)
17) BPT 5204 (Rs 65 per kg)
18) HD 2967 (Rs 75 per kg)
19) HI 1544 (Rs 80 per kg)
20) JS 335 (Rs 85 per kg)
21) MACS 124 (Rs 90 per kg)
22) P 44 (Rs 60 per kg)
23) JG 11 (Rs 65 per kg)
24) HQPM 1 (Rs 100 per kg)
25) P 3396 (Rs 120 per kg)
26) Bunny Bt (Rs 200 per kg)
27) RCH 2 Bt (Rs 220 per kg)
28) Co 86032 (Rs 30 per piece)
29) Co 0238 (Rs 35 per piece)""",
         
"Uttarakhand":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) HD 2967 (Rs 75 per kg)
17) HI 1544 (Rs 80 per kg)
18) PBW 343 (Rs 85 per kg)
19) Co 86032 (Rs 30 per piece)
20) Co 0238 (Rs 35 per piece)
21) Bunny Bt (Rs 200 per kg)
22) RCH 2 Bt (Rs 220 per kg)
23) RD 2660 (Rs 230 per kg)
24) RD 2552 (Rs 240 per kg)
25) P 44 (Rs 60 per kg)
26) JG 11 (Rs 65 per kg)
27) CoFS 29 (Rs 250 per kg)
28) CoFS 32 (Rs 260 per kg)
29) CoFS 36 (Rs 270 per kg)
30) W 306 (Rs 280 per kg)
31) WH 1105 (Rs 290 per kg)""",
         
         
"West bengal":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)

Pesticides:\n
6) Chlorpyrifos (Rs 320 per liter)
7) Imidacloprid (Rs 250 per liter)
8) Mancozeb (Rs 400 per kg)
9) Carbendazim (Rs 350 per kg)
10) Carbofuran (Rs 600 per kg)
11) Monocrotophos (Rs 180 per liter)
12) Chlorantraniliprole (Rs 1500 per liter)
13) Cypermethrin (Rs 300 per liter)
14) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
15) HD 2967 (Rs 75 per kg)
16) HI 1544 (Rs 80 per kg)
17) PBW 343 (Rs 85 per kg)
18) Co 86032 (Rs 30 per piece)
19) Co 0238 (Rs 35 per piece)
20) Bunny Bt (Rs 200 per kg)
21) RCH 2 Bt (Rs 220 per kg)
22) RD 2660 (Rs 230 per kg)
23) RD 2552 (Rs 240 per kg)
24) P 44 (Rs 60 per kg)
25) JG 11 (Rs 65 per kg)
26) CoFS 29 (Rs 250 per kg)
27) CoFS 32 (Rs 260 per kg)
28) CoFS 36 (Rs 270 per kg)
29) W 306 (Rs 280 per kg)
30) WH 1105 (Rs 290 per kg)""",
         
         
"Andaman nicobar":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n

7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) JG 11 (Rs 65 per kg)
17) HQPM 1 (Rs 100 per kg)
18) P 3396 (Rs 120 per kg)""",
         
"Chandigarh":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) HD 2967 (Rs 75 per kg)
17) HI 1544 (Rs 80 per kg)
18) PBW 343 (Rs 85 per kg)
19) Co 86032 (Rs 30 per piece)""",
         
         
"J&K":"""Fertilizers:\n
1) Urea (Rs 276)
2) DAP (Rs 1200)
3) MOP (Rs 1700)
4) SSP (Rs 400)
5) Potash (Rs 900)
6) NPK (10:10:10) (Rs 1200)

Pesticides:\n
7) Chlorpyrifos (Rs 320 per liter)
8) Imidacloprid (Rs 250 per liter)
9) Mancozeb (Rs 400 per kg)
10) Carbendazim (Rs 350 per kg)
11) Carbofuran (Rs 600 per kg)
12) Monocrotophos (Rs 180 per liter)
13) Chlorantraniliprole (Rs 1500 per liter)
14) Cypermethrin (Rs 300 per liter)
15) Cartap hydrochloride (Rs 200 per kg)

Seeds:\n
16) HD 2967 (Rs 75 per kg)
17) HI 1544 (Rs 80 per kg)
18) PBW 343 (Rs 85 per kg)
19) Co 86032 (Rs 30 per piece)
20) Co 0238 (Rs 35 per piece)
21) Bunny Bt (Rs 200 per kg)
22) RCH 2 Bt (Rs 220 per kg)
23) RD 2660 (Rs 230 per kg)
24) RD 2552 (Rs 240 per kg)
25) P 44 (Rs 60 per kg)
26) JG 11 (Rs 65 per kg)
27) CoFS 29 (Rs 250 per kg)
28) CoFS 32 (Rs 260 per kg)
29) CoFS 36 (Rs 270 per kg)
30) W 306 (Rs 280 per kg)
31) WH 1105 (Rs 290 per kg)"""}


output = {}
for city in cities.keys():
    data = cities[city].split("\n")
    all_values = {}
    for value in data:
        if ")" in value:
            all_values[str(value.split(")")[0])] = int(re.findall(r"[0-9]+",value)[-1])
            
            
    output[city] = all_values
    
    
from flask import Flask,request,make_response,jsonify
import requests
import json
import re
import razorpay
import datetime
import pytz
from openai import OpenAI
import pymongo
import time
import string
import json
import certifi

ca = certifi.where()

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-proj-4FvPvbZ3XsofkbYEXB90T3BlbkFJgiC63BX6zCkMs4NnFzZF"
}


tz = pytz.timezone('Asia/Kolkata')

client = pymongo.MongoClient('mongodb+srv://pushkarsh16:1Zuk1qwjfLRKBBno@whatsappchatbot.rhvj6vy.mongodb.net/?retryWrites=true&w=majority&appName=whatsappchatbot', tlsCAFile=ca)
db = client.WhatsApp_DB

app = Flask(__name__)

@app.route('/')
def index():
    return 'Piyush Telegram Bot!'

def return_text_and_suggestion_chip_with_context(text,suggestions,context_session,context_parameter_name,context_value):
    suggestion_list = []
    for suggestion in suggestions:
        suggestion_list.append({"title":suggestion})
    return {"fulfillmentMessages": [
      {
        "platform": "ACTIONS_ON_GOOGLE",
        "simpleResponses": {
          "simpleResponses": [
            {
              "textToSpeech": text
            }
          ]
        }
      },
      {
        "platform": "ACTIONS_ON_GOOGLE",
        "suggestions": {
          "suggestions": suggestion_list
        }
      },
      {
        "text": {
          "text": [
            text
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": context_session+"/my_context",
        "lifespanCount": 25,
        "parameters": {
          context_parameter_name+".original":context_value,
          context_parameter_name:context_value
        }
      }
    ],}


def return_list(title,subtitle,options,descriptions,button_text,postback_text):
    options_list = []
    for option,description,postback in zip(options,descriptions,postback_text):
        options_list.append(
    {
                      "cells": [
                        {},
                        {
                          "text": option
                        },
                        {
                          "text": description
                        },
                        {
                            "text":postback
                        }
                        
                      ]
                    })
    return {"fulfillmentMessages": [
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                  "simpleResponses": [
                    {
                      "textToSpeech": ""
                    }
                  ]
                }
              },
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "tableCard": {
                  "title": title,
                  "subtitle": subtitle,
                  "columnProperties": [
                    {
                      "header": "Section Title",
                      "horizontalAlignment": "LEADING"
                    },
                    {
                      "header": "Option Title",
                      "horizontalAlignment": "LEADING"
                    },
                    {
                      "header": "Option Description",
                      "horizontalAlignment": "LEADING"
                    },
                    {
                      "header": "Postback text",
                      "horizontalAlignment": "LEADING"
                    }
                  ],
                  "rows": options_list,
                  "buttons": [
                    {
                      "title": button_text,
                      "openUriAction": {}
                    }
                  ]
                }
              },
              {
                "text": {
                  "text": [
                    ""
                  ]
                }
              }
            ]}

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def return_text_and_suggestion_chip_with_context(text,suggestions,context_session,context_parameter_name,context_value):
    suggestion_list = []
    for suggestion in suggestions:
        suggestion_list.append({"title":suggestion})
    return {"fulfillmentMessages": [
      {
        "platform": "ACTIONS_ON_GOOGLE",
        "simpleResponses": {
          "simpleResponses": [
            {
              "textToSpeech": text
            }
          ]
        }
      },
      {
        "platform": "ACTIONS_ON_GOOGLE",
        "suggestions": {
          "suggestions": suggestion_list
        }
      },
      {
        "text": {
          "text": [
            text
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": context_session+"/my_context",
        "lifespanCount": 25,
        "parameters": {
          context_parameter_name+".original":context_value,
          context_parameter_name:context_value
        }
      }
    ],}

def return_text_with_context(text,context_session,context_parameter_name,context_value):
    
    parameters = {}
    for param,value in zip(context_parameter_name,context_value):
        parameters[param+".original"] = value
        parameters[param] = value

    return {"fulfillmentMessages": [
      {
        "platform": "ACTIONS_ON_GOOGLE",
        "simpleResponses": {
          "simpleResponses": [
            {
              "textToSpeech": text
            }
          ]
        }
      },
      {
        "text": {
          "text": [
            text
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": context_session+"/my_context",
        "lifespanCount": 25,
        "parameters": parameters
      }
    ],}
    


def return_text_and_suggestion_chip(text,suggestions):
    suggestion_list = []
    for suggestion in suggestions:
        suggestion_list.append({"title":suggestion})
    return {"fulfillmentMessages": [
      {
        "quickReplies": {
          "title": text,
          "quickReplies": suggestion_list
        },
        "platform": "TELEGRAM"
      }
    ]}


def return_only_text(text):
    return {'fulfillmentMessages':[
      {
        "text": {
          "text": [text
          ]
        },
        "platform": "TELEGRAM"
      }
    ]}

        
def results():
    req = request.get_json(force=True)
    
    intent_name = req['queryResult']['intent']['displayName']
    session = req['session'].split('/')[-1]
    
    if intent_name =="Place Order":
        if len(str(req['queryResult']['parameters']['city']))<1:
            text = """Please select one state for which you are shopping:
            
1) Andaman nicobar
2) Andhra Pradesh
3) Arunachal Pradesh
4) Assam
5) Bihar
6) Chandigarh
7) Chattisgarh
8) Goa
9) Gujarat
10) Haryana
11) Himachal Pradesh
12) J&K
13) Jharkhand
14) Karnataka
15) Kerala
16) Madhya pradesh
17) Maharashtra
18) Manipur
19) Meghalaya
20) Mizoram
21) Nagaland
22) Odisha
23) Punjab
24) Rajasthan
25) Sikkim
26) Tamil nadu
27) Telangana
28) Tripura
29) Uttar pradesh
30) Uttarakhand
31) West Bengal
"""
            return return_only_text(text)
        
        
        city = req['queryResult']['parameters']['city']
    
        if len(req['queryResult']['parameters']['items'])<1:
            text = f"""Sure! I will help you with your order for {city}

Please type in comma separated numbers which you want to be added in your cart\n\n"""+cities[city]
            return return_only_text(text)
        
        prices = output[city]
        items = req['queryResult']['parameters']['items']
        items = [prices[str(int(item))] for item in items]
       
        total_price = sum(items)
        
        client = razorpay.Client(auth=("rzp_test_63Pd2BF9NY4iA1", "2SX95YRVl7Z6NPwVAUkAIKW0"))

        response = client.payment_link.create({
          "amount": total_price*100,
          "currency": "INR",
          "accept_partial": False,
          "description": "For Farmer Bot",
          "customer": {
            "name": "User",
            "email": "user@gmail.com",
            "contact": "+917485452365"
          },
          "notify": {
            "sms": True,
            "email": True
          },
          "reminder_enable": False,
          "notes": {
            "policy_name": "Farmer Bot Payment"
          },
          "callback_url": "https://example-callback-url.com/",
          "callback_method": "get"
        })
        
        payment_link = response['short_url']
        
        text = "Thank you for your order. Your order is confirmed. The total order value is Rs. "+str(total_price)+"Please make the payment using the following payment link "+payment_link
        
        requests.post('https://api.telegram.org/bot7137863753:AAHmdgsTch5kyCPxJXiAOMbMV4126HX0-vQ/sendMessage?chat_id='+req['originalDetectIntentRequest']['payload']['data']['chat']['id']+'&parse_mode=html&text='+text)

    
    if intent_name == "Default Fallback Intent":
        if db.Chats.count_documents({"Session":session})==0:
            db.Chats.insert_one({
                            "Session":session,
                            "Conversation":[]})
            
            messages = [{"role": "user", "content": req['queryResult']['queryText']}]
            data = {
                "model": "gpt-3.5-turbo",
                "messages": messages,
                "temperature": 0.7
            }
            response = requests.post(url, headers=headers, json=data)
            answer = response.json()['choices'][0]['message']['content']
            messages = messages+[{"role": "assistant", "content": answer}]
     
            db.Chats.update_one(
                                    {
                                        "Session":session
                                    },
                                    {
                                        "$set" :
                                        {
                                            "Conversation":messages
                                        }
                                    }
                                )
            

            requests.post('https://api.telegram.org/bot7137863753:AAHmdgsTch5kyCPxJXiAOMbMV4126HX0-vQ/sendMessage?chat_id='+req['originalDetectIntentRequest']['payload']['data']['chat']['id']+'&parse_mode=html&text='+answer)

        else:
            old_chats = db.Chats.find_one({"Session":session})['Conversation']
            messages = [{"role": "user", "content": req['queryResult']['queryText']}]
            all_chats = old_chats+messages
            data = {
                "model": "gpt-3.5-turbo",
                "messages": all_chats,
                "temperature": 0.7
            }
            response = requests.post(url, headers=headers, json=data)
            answer = response.json()['choices'][0]['message']['content']
            all_chats = all_chats+[{"role": "assistant", "content": answer}]
            
            db.Chats.update_one(
                                    {
                                        "Session":session
                                    },
                                    {
                                        "$set" :
                                        {
                                            "Conversation":all_chats
                                        }
                                    }
                                )
            
            requests.post('https://api.telegram.org/bot7137863753:AAHmdgsTch5kyCPxJXiAOMbMV4126HX0-vQ/sendMessage?chat_id='+req['originalDetectIntentRequest']['payload']['data']['chat']['id']+'&parse_mode=html&text='+answer)

            
        
        
@app.route('/api/', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

if __name__ == '__main__':
    app.run()
    #app.run(host="0.0.0.0",port = 8000)