import step2_test
import pandas as pd
from mpl_toolkits import mplot3d #For 3d plots
import matplotlib.pyplot as plt #for graph

#Loading dataset
df1 = pd.read_csv("Exp_N.csv")
df2 = pd.read_csv("Exp_T.csv") 
df3 = pd.read_csv("Exp_P.csv")

#*********************
#   NORMAL parameter extraction
#*********************

#graph for Normal 
data = pd.DataFrame(df1, columns = ['TLC', 'Protein', 'Sugar']) 
#creating axes instance 
#fig = plt.figure(figsize=(10,7)) 
#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
bp1 = plt.boxplot(data, notch='True', labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#IMpt - when patch_artist = True --> ranges is giving error 
#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
#plt.scatter(x=1,y=Test.a, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=2,y=Test.f, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=3,y=Test.g, label = 'Scatter', color ='r', marker = 's', s = 100)
#show plot
#plt.show()
#plt.title("Normal Category")

#******** Extracting ranges ***********
#Stats for NORMAL-

#Getting each value of data -
medians_N = [round(item.get_ydata()[0], 1) for item in bp1['medians']]
means_N = [round(item.get_ydata()[0],1) for item in bp1['means']]

minimums_N = [round(item.get_ydata()[0], 1) for item in bp1['caps']][::2]
maximums_N = [round(item.get_ydata()[0], 1) for item in bp1['caps']][1::2]

q1_N = [round(min(item.get_ydata()), 1) for item in bp1['boxes']]
q3_N = [round(max(item.get_ydata()), 1) for item in bp1['boxes']]

fliers_N = [item.get_ydata() for item in bp1['fliers']]
lower_outliers_N = []
upper_outliers_N = []
for i in range(len(fliers_N)):
    lower_outliers_by_box_N = []
    upper_outliers_by_box_N = []
    for outlier in fliers_N[i]: 
        if outlier < q1_N[i]: 
            lower_outliers_by_box_N.append(round(outlier, 1)) 
        else: 
            upper_outliers_by_box_N.append(round(outlier, 1)) 
    lower_outliers_N.append(lower_outliers_by_box_N) 
    upper_outliers_N.append(upper_outliers_by_box_N) 

#print(" ************************************ ")
#print(" STATS FOR NORMAL CATEGORY ARE : ")
#print(" ************************************ ")

#Declaring for further purpose of calculating scores -
N1_min = 0
N1_q1 = 0
N1_q3 = 0
N1_maximums_N = 0
N2_min = 0
N2_q1 = 0
N2_q3 = 0
N2_maximums_N = 0
N3_min = 0
N3_q1 = 0
N3_q3 = 0
N3_maximums_N = 0

#same as above code but combined 
stats = [medians_N, means_N, minimums_N, maximums_N, q1_N, q3_N, lower_outliers_N, upper_outliers_N]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    #print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        #print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            N1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            N2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            N3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N3_maximums_N = stats[j][i]
    print('\n')


#*********************
#   TBM parameter extraction
#*********************

#graph for TBM

data = pd.DataFrame(df2, columns = ['TLC', 'Protein', 'Sugar']) 
#creating axes instance 
#fig = plt.figure(figsize=(10,7)) 
#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'] )
bp2 = plt.boxplot(data, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
#plt.scatter(x=1,y=a, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=2,y=f, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=3,y=g, label = 'Scatter', color ='r', marker = 's', s = 100)
#show plot
#plt.show()
#plt.title("TBM Category")


#******** Extracting ranges ***********
#Stats for TBM -

#Stats for TBM CATEGORY -
#Getting each value of data -
medians_T = [round(item.get_ydata()[0], 1) for item in bp2['medians']]
means_T = [round(item.get_ydata()[0],1) for item in bp2['means']]

minimums_T = [round(item.get_ydata()[0], 1) for item in bp2['caps']][::2]
maximums_T = [round(item.get_ydata()[0], 1) for item in bp2['caps']][1::2]

q1_T = [round(min(item.get_ydata()), 1) for item in bp2['boxes']]
q3_T = [round(max(item.get_ydata()), 1) for item in bp2['boxes']]

fliers_T = [item.get_ydata() for item in bp2['fliers']]
lower_outliers_T = []
upper_outliers_T = []
for i in range(len(fliers_T)):
    lower_outliers_by_box_T = []
    upper_outliers_by_box_T = []
    for outlier in fliers_T[i]:
        if outlier < q1_T[i]:
            lower_outliers_by_box_T.append(round(outlier, 1))
        else:
            upper_outliers_by_box_T.append(round(outlier, 1))
    lower_outliers_T.append(lower_outliers_by_box_T)
    upper_outliers_T.append(upper_outliers_by_box_T) 


#print(" ************************************ ")
#print(" STATS FOR TBM CATEGORY ARE : ")
#print(" ************************************ ")

#Declaring for further purpose of calculating scores -
T1_min = 0
T1_q1 = 0
T1_q3 = 0
T1_maximums_N = 0
T2_min = 0
T2_q1 = 0
T2_q3 = 0
T2_maximums_N = 0
T3_min = 0
T3_q1 = 0
T3_q3 = 0
T3_maximums_N = 0

#same as above code but combined 
stats = [medians_T, means_T, minimums_T, maximums_T, q1_T, q3_T, lower_outliers_T, upper_outliers_T]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    #print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        #print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            T1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            T2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            T3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T3_maximums_N = stats[j][i]
    print('\n')


#***************************
#   PM parameter extraction
#***************************

#graph for PM

data = pd.DataFrame(df3, columns = ['TLC', 'Protein', 'Sugar']) 
#creating axes instance 
#fig = plt.figure(figsize=(10,7)) 
#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'] )
bp3 = plt.boxplot(data, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
#plt.scatter(x=1,y=a, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=2,y=f, label = 'Scatter', color ='r', marker = 's', s = 100)
#plt.scatter(x=3,y=g, label = 'Scatter', color ='r', marker = 's', s = 100)
#show plot
#plt.show()
#plt.title("PM Category")

#******** Extracting ranges ***********
#Stats for PM -

#Stats for PM CATEGORY -
#Getting each value of data -
medians_P = [round(item.get_ydata()[0], 1) for item in bp3['medians']]
means_P = [round(item.get_ydata()[0],1) for item in bp3['means']]

minimums_P = [round(item.get_ydata()[0], 1) for item in bp3['caps']][::2]
maximums_P = [round(item.get_ydata()[0], 1) for item in bp3['caps']][1::2]

q1_P = [round(min(item.get_ydata()), 1) for item in bp3['boxes']]
q3_P = [round(max(item.get_ydata()), 1) for item in bp3['boxes']]

fliers_P = [item.get_ydata() for item in bp3['fliers']]
lower_outliers_P = []
upper_outliers_P = []
for i in range(len(fliers_P)):
    lower_outliers_by_box_P = []
    upper_outliers_by_box_P = []
    for outlier in fliers_P[i]:
        if outlier < q1_P[i]:
            lower_outliers_by_box_P.append(round(outlier, 1))
        else:
            upper_outliers_by_box_P.append(round(outlier, 1))
    lower_outliers_P.append(lower_outliers_by_box_P)
    upper_outliers_P.append(upper_outliers_by_box_P) 

#print(" ************************************ ")
#print(" STATS FOR PM CATEGORY ARE : ")
#print(" ************************************ ")

#Declaring for further purpose of calculating scores -
P1_min = 0
P1_q1 = 0
P1_q3 = 0
P1_maximums_N = 0
P2_min = 0
P2_q1 = 0
P2_q3 = 0
P2_maximums_N = 0
P3_min = 0
P3_q1 = 0
P3_q3 = 0
P3_maximums_N = 0

#same as above code but combined 
stats = [medians_P, means_P, minimums_P, maximums_P, q1_P, q3_P, lower_outliers_P, upper_outliers_P]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    #print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        #print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            P1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            P2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            P3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P3_maximums_N = stats[j][i]
    print('\n')

