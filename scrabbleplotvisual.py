import matplotlib.pyplot as plt

scrable_x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
scrable_y = [
            100,
            83.33333333333334,
            37.5,
            10.833333333333334,
            1.6666666666666667,
            0.21825396825396826,
            0.027281746031746032,
            0.0016534391534391536,
            0.00013778659611992947,
            0.000015031265031265032,
            0.0000008350702795147241,
            0.00000004817713151046484,
            0.0000000034412236793189174,
            0.00000000030588654927279264
            ]

alpha_x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
alpha_y = [
          100,
          100,
          37.5,
          11.66,
          2.083,
          0.277,
          0.0223214,
          0.00248015873015873,
          0.00013778659611992947,
          0.000015031265031265032,
          0.000000626302709636043,
          0.00000006423617534728645,
          0.0000000034412236793189174,
          0.00000000030588654927279264,
          0.00000000000955895466477477,
          0.0000000000005622914508691041,
          0.00000000000003123841393717245,
          0.000000000000001644127049324866,
          0.0000000000000000822063524662433,
          0.0000000000000000039145882126782525,
          0.0000000000000000001779358278490115,
          0.000000000000000000003868170170630684,
          0.00000000000000000000016117375710961184,
          0.0000000000000000000000064469502843844735
          ]
          
max_alpha =   [2,6,9,14,15,14,9,9,5,6,3,4,3,4,2,2,2,2,2,2,2,2,1,1,1]
max_scrable = [2,5,9,13,12,11,11,6,5,6,4,3,3,4]


plt.figure()

# linear
plt.subplot(1,3,1)
plt.plot(alpha_y,"b-",lw=0.5)
plt.plot(scrable_y,"r--",lw=2)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(1,3,2)
plt.plot(alpha_x,alpha_y,"b")
plt.plot(scrable_x,scrable_y,"r--")
plt.yscale('log')
plt.title('log')
plt.grid(True)

# max
plt.subplot(1,3,3)
plt.plot(max_alpha,"b-",lw=0.5)
plt.plot(max_scrable,"r--",lw=2)
plt.yscale('linear')
plt.title('max')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
