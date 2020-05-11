EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr User 12095 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	6000 2700 6000 2900
Wire Wire Line
	6000 2700 5000 2700
Wire Wire Line
	5000 2700 5000 4100
Wire Wire Line
	5400 4100 5800 4100
Wire Wire Line
	5800 4100 5800 3800
Wire Wire Line
	6200 3800 6200 4100
Wire Wire Line
	6200 4100 5800 4100
Wire Wire Line
	5000 4100 5400 4100
Connection ~ 5800 4100
Connection ~ 6000 2700
Wire Wire Line
	5800 3500 6000 3500
Wire Wire Line
	6000 3500 6000 3300
Wire Wire Line
	6200 3500 6000 3500
Connection ~ 6000 3500
Wire Wire Line
	7300 3200 7300 3700
Wire Wire Line
	7100 2400 6900 2400
Wire Wire Line
	6900 2400 6900 3200
Wire Wire Line
	6900 3200 7300 3200
Connection ~ 7300 3200
Wire Wire Line
	7400 3200 7400 3700
Wire Wire Line
	7400 3200 7800 3200
Wire Wire Line
	7800 3200 7800 2400
Wire Wire Line
	7800 2400 7500 2400
Connection ~ 7400 3200
$Comp
L heatedBed-eagle-import:DINA4_L #FRAME1
U 1 1 73DA64CA
P 900 7200
F 0 "#FRAME1" H 900 7200 50  0001 C CNN
F 1 "DINA4_L" H 900 7200 50  0001 C CNN
F 2 "" H 900 7200 50  0001 C CNN
F 3 "" H 900 7200 50  0001 C CNN
	1    900  7200
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:DINA4_L #FRAME1
U 2 1 73DA64C6
P 7300 7200
F 0 "#FRAME1" H 7300 7200 50  0001 C CNN
F 1 "DINA4_L" H 7300 7200 50  0001 C CNN
F 2 "" H 7300 7200 50  0001 C CNN
F 3 "" H 7300 7200 50  0001 C CNN
	2    7300 7200
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:R-EU_R0805 R1
U 1 1 43360497
P 6000 3100
F 0 "R1" H 5850 3159 59  0000 L BNN
F 1 "2K2" H 5850 2970 59  0000 L BNN
F 2 "heatedBed:R0805" H 6000 3100 50  0001 C CNN
F 3 "" H 6000 3100 50  0001 C CNN
	1    6000 3100
	0    -1   -1   0   
$EndComp
$Comp
L heatedBed-eagle-import:LEDCHIPLED_1206_REV L1
U 1 1 7641244C
P 6200 3600
F 0 "L1" V 6340 3420 59  0000 L BNN
F 1 "597-6001-607F" V 6425 3420 59  0000 L BNN
F 2 "heatedBed:CHIPLED_1206_REVERSE" H 6200 3600 50  0001 C CNN
F 3 "" H 6200 3600 50  0001 C CNN
	1    6200 3600
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:LEDCHIPLED_1206_REV L2
U 1 1 77B97637
P 5800 3700
F 0 "L2" V 5940 3520 59  0000 L BNN
F 1 "LEDCHIPLED_1206_REV" V 6025 3520 59  0000 L BNN
F 2 "heatedBed:CHIPLED_1206_REVERSE" H 5800 3700 50  0001 C CNN
F 3 "" H 5800 3700 50  0001 C CNN
	1    5800 3700
	-1   0    0    1   
$EndComp
$Comp
L heatedBed-eagle-import:LONG_PAD U$2
U 1 1 A8B04D1A
P 5400 4100
F 0 "U$2" V 5600 4100 42  0000 L BNN
F 1 "LONG_PAD" H 5400 4100 50  0001 C CNN
F 2 "heatedBed:LONG_PAD" H 5400 4100 50  0001 C CNN
F 3 "" H 5400 4100 50  0001 C CNN
	1    5400 4100
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:LONG_PAD P2
U 1 1 01CDF5BD
P 6000 2700
F 0 "P2" V 6200 2700 42  0000 L BNN
F 1 "LONG_PAD" H 6000 2700 50  0001 C CNN
F 2 "heatedBed:LONG_PAD" H 6000 2700 50  0001 C CNN
F 3 "" H 6000 2700 50  0001 C CNN
	1    6000 2700
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:SMD5 PAD1
U 1 1 0344E6DA
P 7300 3100
F 0 "PAD1" H 6955 3073 59  0000 L BNN
F 1 "SMD5" H 7255 2970 59  0000 L BNN
F 2 "heatedBed:SMD2,54-5,08" H 7300 3100 50  0001 C CNN
F 3 "" H 7300 3100 50  0001 C CNN
	1    7300 3100
	0    1    1    0   
$EndComp
$Comp
L heatedBed-eagle-import:SMD5 PAD2
U 1 1 5599201C
P 7400 3100
F 0 "PAD2" H 7055 3073 59  0000 L BNN
F 1 "SMD5" H 7355 2970 59  0000 L BNN
F 2 "heatedBed:SMD2,54-5,08" H 7400 3100 50  0001 C CNN
F 3 "" H 7400 3100 50  0001 C CNN
	1    7400 3100
	0    1    1    0   
$EndComp
$Comp
L heatedBed-eagle-import:SMD5 PAD3
U 1 1 5B5DCDFD
P 7400 3800
F 0 "PAD3" H 7055 3773 59  0000 L BNN
F 1 "SMD5" H 7355 3670 59  0000 L BNN
F 2 "heatedBed:SMD2,54-5,08" H 7400 3800 50  0001 C CNN
F 3 "" H 7400 3800 50  0001 C CNN
	1    7400 3800
	0    -1   -1   0   
$EndComp
$Comp
L heatedBed-eagle-import:SMD5 PAD4
U 1 1 4BAB13D1
P 7300 3800
F 0 "PAD4" H 6955 3773 59  0000 L BNN
F 1 "SMD5" H 7255 3670 59  0000 L BNN
F 2 "heatedBed:SMD2,54-5,08" H 7300 3800 50  0001 C CNN
F 3 "" H 7300 3800 50  0001 C CNN
	1    7300 3800
	0    -1   -1   0   
$EndComp
$Comp
L heatedBed-eagle-import:SPARKFUN_OSHW-LOGOL U$5
U 1 1 6A689A17
P 6600 6500
F 0 "U$5" H 6600 6500 50  0001 C CNN
F 1 "SPARKFUN_OSHW-LOGOL" H 6600 6500 50  0001 C CNN
F 2 "heatedBed:SPARKFUN_OSHW-LOGO-L" H 6600 6500 50  0001 C CNN
F 3 "" H 6600 6500 50  0001 C CNN
	1    6600 6500
	1    0    0    -1  
$EndComp
$Comp
L heatedBed-eagle-import:R-EU_R0805 R2
U 1 1 3042A0E0
P 7300 2400
F 0 "R2" H 7150 2459 59  0000 L BNN
F 1 "NTCS0805E3104FXT" H 6660 2240 59  0000 L BNN
F 2 "heatedBed:R0805" H 7300 2400 50  0001 C CNN
F 3 "" H 7300 2400 50  0001 C CNN
	1    7300 2400
	-1   0    0    1   
$EndComp
Text Notes 3000 6600 0    59   ~ 0
Released under the CERN Open Hardware Licence v1.2 
Text Notes 7520 6140 0    170  ~ 0
HEATBED MINI by fm
Text Notes 3940 2480 0    56   ~ 0
Heatbed connection
Text Notes 3840 3880 0    56   ~ 0
Heatbed connection
Text Notes 3400 2200 0    56   ~ 0
Make sure that there are sufficient vias to\nhandle 5A-6A.
Text Notes 7600 3100 0    56   ~ 0
Thermistor surface PADs
Text Notes 3000 6800 0    56   ~ 0
http://www.ohwr.org/attachments/2388/cern_ohl_v_1_2.txt
Text Notes 4520 1140 0    170  ~ 0
HEATBED MINI - by fm
Text Notes 10990 6940 0    127  ~ 0
B
Text Notes 3500 4800 0    59   ~ 12
RevA - 110W - track width = 1.41 aprox \nRevB - 69W - track width = 0.82 aprox
Wire Notes Line
	5000 4100 4500 4500
$EndSCHEMATC
