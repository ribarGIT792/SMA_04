
# Paprastuju iteraciju ir Gauso-Zeidelio algoritmai

import numpy as np
from PyFunkcijos import *
import matplotlib.pyplot as plt

# textbox isvedimui
T=ScrollTextBox(100,20) # sukurti teksto isvedimo langa
T.insert(END,"# ********************* Gauso algoritmas  ****************************")

# -------------------iseities duomnenys:
if False :
    A=np.matrix([[ 1, -1,  0,  0],
                 [-1,  2, -1,  0],
                 [ 0, -1,  2, -1],
                 [ 0,  0, -1,  2]]).astype(np.float)
    b=np.array([[2],[0],[0],[0]]).astype(np.float)
    alpha=np.array([1, 1, 1, 1])  # laisvai parinkti metodo parametrai, butinai eilute, kitaip nesusikuria diag matrica
else :
    A=np.matrix([[ 5, 11,  7,  0],
                 [ 2,  6, 17,  2],
                 [ 2,  1,  5,  1],
                 [ 4, 12,  1,  7]]).astype(np.float)
    b=np.array([[50],[75],[30],[171]]).astype(np.float)
    alpha=np.array([100, 20, 1, 1])  # laisvai parinkti metodo parametrai

n=np.shape(A)[0]

method="simple_iterations"
#method="Gauss-Seidel_iterations";
print(alpha)

Atld=np.diag(1./np.diag(A)).dot(A)-np.diag(alpha)
btld=np.diag(1./np.diag(A)).dot(b)
print(Atld)
print(btld)

nitmax=1000; eps=1e-12; prec=[]  # tuscias sarasas tikslumo reiksmiu kaupimui
x=np.zeros(shape=(n,1));x1=np.zeros(shape=(n,1));
T.insert(END,"\n sprendimas iteracijomis:") 
print("sprendimas interacijomis")
for it in range (0,nitmax):
  if method == "Gauss-Seidel_iterations" :
     for i in range (0,n) : x1[i]=(btld[i]-Atld[i,:].dot(x1))/alpha[i];
  elif method == "simple_iterations" :
      x1=((btld-Atld.dot(x)).transpose()/alpha).transpose();  # array negalima transponuoti, o diag matrica pasidaro tik is eilutes    
  else :
       T.insert(END,"\n neaprasytas metodas")
       print("\n neaprasytas metodas")
  print(x1);print(x);
  prec.append(np.linalg.norm(x1-x)/(np.linalg.norm(x)+np.linalg.norm(x1)))
  T.insert(END,"\niteracija Nr. %d,  tikslumas  %g" % (it,prec[it]))
  print("iteracija Nr. %d,  tikslumas  %g" % (it,prec[it]))
  if prec[-1] < eps :  itt=it; break  # -1 reiskia paaskutini saraso elementa
  x[:]=x1[:]  # x-x1 perduoda adresa, o ne reiksmes
  print(x)

SpausdintiMatrica(x,T,'x')
print("patikrinimas")
print(A.dot(x)-b)

X=np.linspace(1,itt,itt) # funkcijos vaizdavimo taskai
fig=plt.figure();ax=fig.add_subplot(1, 1, 1);ax.set_xlabel('iteracijos');ax.set_ylabel('tikslumas')
c1,=ax.semilogy(X,prec[0:itt],'b');plt.draw();plt.show()

T.insert(END,"\n");T.yview(END)  

str1=input("Baigti darba? Press 'Y' \n")