import step3_Intensity
import step2_test

#Predicting score
#Predicting scores
#score1 = normal
#score2 = tbm
#score3 = pm


sn1 = 0
st1 = 0
sp1 = 0
sn2 = 0
st2 = 0
sp2 = 0
sn3 = 0
st3 = 0
sp3 = 0


# print(N1_min)
# print()
#********* For normal ************
#for TLC (Parameter 1 ):
if ( step3_Intensity.N1_min <= step2_test.a <= step3_Intensity.N1_q1 ):
  sn1 = 1
elif ( step3_Intensity.N1_q1 < step2_test.a <= step3_Intensity.N1_q3 ):
  sn1 = 2
elif( step3_Intensity.N1_q3 < step2_test.a <= step3_Intensity.N1_maximums_N):
  sn1 = 3 
#For Protein( parameter 2 ):
if ( step3_Intensity.N2_min <= step2_test.f <= step3_Intensity.N2_q1 ):
  st1 = 1
elif ( step3_Intensity.N2_q1 < step2_test.f <= step3_Intensity.N2_q3 ):
  st1 = 2
elif( step3_Intensity.N2_q3 < step2_test.f <= step3_Intensity.N2_maximums_N):
  st1 = 3
#For Sugar ( parameter 3 ):
if ( step3_Intensity.N3_min <= step2_test.g <= step3_Intensity.N3_q1 ):
  sp1 = 1
elif ( step3_Intensity.N3_q1 < step2_test.g <= step3_Intensity.N3_q3 ):
  sp1 = 2
elif( step3_Intensity.N3_q3 < step2_test.g <= step3_Intensity.N3_maximums_N):
  sp1 = 3
#calculating normal score
score1 = (sn1 + st1 + sp1)/3
'''
print("**********************")
print("Score for Normal = ", score1)
print("**********************")
'''


#********* For tbm ************
#for TLC (Parameter 1 ):
if ( step3_Intensity.T1_min <= step2_test.a <= step3_Intensity.T1_q1 ):
  sn2 = 1
elif ( step3_Intensity.T1_q1 < step2_test.a <= step3_Intensity.T1_q3 ):
  sn2 = 2
elif( step3_Intensity.T1_q3 < step2_test.a <= step3_Intensity.T1_maximums_N):
  sn2 = 3 
#For Protein( parameter 2 ):
if ( step3_Intensity.T2_min <= step2_test.f <= step3_Intensity.T2_q1 ):
  st2 = 1
elif ( step3_Intensity.T2_q1 < step2_test.f <= step3_Intensity.T2_q3 ):
  st2 = 2
elif( step3_Intensity.T2_q3 < step2_test.f <= step3_Intensity.T2_maximums_N):
  st2 = 3
#For Sugar ( parameter 3 ):
if ( step3_Intensity.T3_min <= step2_test.g <= step3_Intensity.T3_q1 ):
  sp2 = 1
elif ( step3_Intensity.T3_q1 < step2_test.g <= step3_Intensity.T3_q3 ):
  sp2 = 2
elif( step3_Intensity.T3_q3 < step2_test.g <= step3_Intensity.T3_maximums_N):
  sp2 = 3
#calculating tbm score
score2 = (sn2 + st2 + sp2)/3
'''
print("**********************")
print("Score for TBM = ", score2)
print("**********************")
'''


#********* For pm ************
#for TLC ( Parameter 1 ):
if ( step3_Intensity.P1_min <= step2_test.a  <= step3_Intensity.P1_q1 ):
  sn3 = 1
elif ( step3_Intensity.P1_q1 < step2_test.a <= step3_Intensity.P1_q3 ):
  sn3 = 2
elif( step3_Intensity.P1_q3 < step2_test.a <= step3_Intensity.P1_maximums_N):
  sn3 = 3 
#For Protein( parameter 2 ):
if ( step3_Intensity.P2_min <= step2_test.f <= step3_Intensity.P2_q1 ):
  st3 = 1
elif ( step3_Intensity.P2_q1 < step2_test.f <= step3_Intensity.P2_q3 ):
  st3 = 2
elif( step3_Intensity.P2_q3 < step2_test.f <= step3_Intensity.P2_maximums_N):
  st3 = 3
#For Sugar ( parameter 3 ):
if ( step3_Intensity.P3_min <= step2_test.g <= step3_Intensity.P3_q1 ):
  sp3 = 1
elif ( step3_Intensity.P3_q1 < step2_test.g <= step3_Intensity.P3_q3 ):
  sp3 = 2
elif( step3_Intensity.P3_q3 < step2_test.g <= step3_Intensity.P3_maximums_N):
  sp3 = 3
#calculating normal score
score3 = (sn3 + st3 + sp3)/3
'''
print("**********************")
print("Score for PM = ", score3)
print("**********************")
'''

#Plotting intensity graphs 
#CALCULTING INTENSITIES OF EACH DISEASE -
#Plotting graph too.
import matplotlib.pyplot as plt #for graph

'''
## First Ranges 
1 - 1.5
1.5 - 2.5
2.5 - 3

## Editing Ranges1 :
1 - 1.6
1.6 - 2.3
2.3 - 3

#Editing Ranges2 -
0.5 - 1.6
1.6 - 2.3
2.3 - 3
'''

#making graph
plt.figure(figsize = (8,8))
plt.xlim(-10,10) #x axis limit
plt.ylim(-10,10) # y axis limit
axis = plt.gca() #get current axes

#plotting labels for graph
plt.text(x = -9 , y = 9 , s = " TUBERCULOSIS MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - TBM
plt.text(x = 2 , y = 9, s = " PYOGENIC MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - PM
plt.text(x = -1.5, y = -1 , s = " NORMAL ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - NORMAL

#plotting points
print("***************************")
print("step3_Intensity of NORMAL - ")
if (0.5 <= score1 <= 3):
  plt.text(x = -2, y = -5 ,s = " COMPLETELY NORMAL ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")

'''
if (0.5 <= score1 <= 1.6 ):
  plt.scatter(x = 2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = 2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score1 <= 2.3):
  plt.scatter(x = 4.6, y = 4.6, label = s'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = 4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score1 <= 3):
  plt.scatter(x = 7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = 7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = -2, y = -5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")
'''


print("***************************")
print("step3_Intensity of TBM - ")
if (0.5 <= score2 <= 1.6 ):
  plt.scatter(x = -2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = -2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score2 <= 2.3):
  plt.scatter(x = -4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = -4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score2 <= 3):
  plt.scatter(x = -7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = -7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")


print("***************************")
print("step3_Intensity of PM - ")
if (0.5 <= score3 <= 1.6 ):
  plt.scatter(x = 2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = 2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score3 <= 2.3):
  plt.scatter(x = 4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = 4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score3 <= 3):
  plt.scatter(x = 7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = 7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym
  print("Asymptotic")


plt.plot(axis.get_xlim(), [0,0], 'k--')  #x axis plot line across 
#plt.plot([0,0],axis.get_xlim(), 'k--')   #y axis plot line across
plt.vlines(x=0, ymin=0, ymax=10, color='k', linestyle='--') 
plt.ylabel('Y - axis')
plt.xlabel('X - axis')
plt.title(" step3_Intensity of Meningitis ")
#plt.grid()
#plt.legend()
plt.show()