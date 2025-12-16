fps=6400
time=[]
t0=1
for i in range(0,q):
    time.append(i/(fps*t0))

len(time)

n = []
for i in neck_width:
    n.append(i)
t = []
for i in time:
    t.append(i)

idx = []
for i in range(len(neck_width)):
    if n[i] >= 250 or n[i] <= 20:
        idx.append(i)
idx.sort(reverse=True)
for i in idx:
    del t[i]
    del n[i]
xf = []
yf = []
tol = 5
for i in range(len(t)):
    if abs(n[i] - n[i - 1]) <= tol:
        yf.append(n[i])
        xf.append(t[i])

import matplotlib.pyplot as plt
import pandas as pd

# df1=pd.read_excel(r'C:\Users\user\Desktop\New folder (2)\phi=0.1\5\5new.xlsx')
# x1=df1['time']
# y1=df1['neck']
plt.figure(figsize=(8, 8))
# plt.scatter(x1,y1,color='red',lw=1)
# plt.scatter(time,neck_width,color='blue',lw=1)
plt.scatter(xf, yf, color='blue', lw=1)
plt.xlabel('time')
plt.ylabel('neck_width')
plt.title('Qd/Qc=1', fontsize=20)
# plt.xlim(xf[0],xf[-1])
plt.grid()

