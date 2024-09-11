#Points are used to determine which eating outlet is better - after a comparative study
#basis for points: +1 points if the items provided by the eatery have lower mean fat, TransFat, St.fat, Calories, Cholesterol and sugar
#basis for points: +1 points if the items provided by the eatery have higher mean prot, fibre, carbs, sodium
#basis for points: +1 points if the items provided by the eatery have higher Net range of nutrient attributes
#basis for points: +1 points if the items provided by the eatery have higher IQR of nutrient attributes
#bais for points:  +1 points if the common items between the two eating outlets have better nutrient attributes
#EXTRA basis for points:prelude to cohort study: +1 points if the nutrient attributes of the items chosen by the user falls within the recommended range
#For Analysis of the two datasets
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from fitness_tools.meals.meal_maker import MakeMeal
#Reading the CSV files
df_CF = pd.read_csv("C:\\Users\\mania\\Downloads\\project_final_chickfila.csv")
df_KFC = pd.read_csv("C:\\Users\\mania\\Downloads\\project_final_KFC.csv")
#Variables needed for computation
column_names_CF = df_CF.iloc[1, :].index
column_names_KFC = df_KFC.iloc[1, :].index
mean_cf = []
mean_kfc = []
max_cf = []
max_kfc = []
min_cf = []
min_kfc = []
range_cf=[]
range_kfc=[]
q1_cf=[]
q3_cf=[]
q1_kfc=[]
q3_kfc=[]
iqr_cf=[]
iqr_kfc=[]
#Findiing Mean,Max Value, Min Value, Range & DF of items with more the 0 Transfat
for i in range(2, len(column_names_CF)):
    mean_cf.append(df_CF[column_names_CF[i]].mean())
    max_cf.append(df_CF[column_names_CF[i]].max())
    min_cf.append(df_CF[column_names_CF[i]].min())
    q1_cf.append(np.percentile(df_CF[column_names_CF[i]].values.tolist(), 25))
    q3_cf.append(np.percentile(df_CF[column_names_CF[i]].values.tolist(), 75))
    iqr_cf.append(np.percentile(df_CF[column_names_CF[i]].values.tolist(), 75)-np.percentile(df_CF[column_names_CF[i]].values.tolist(), 25))
    range_cf.append(df_CF[column_names_CF[i]].max()-df_CF[column_names_CF[i]].min())
for i in range(2, len(column_names_KFC)):
    mean_kfc.append(df_KFC[column_names_KFC[i]].mean())
    max_kfc.append(df_KFC[column_names_KFC[i]].max())
    min_kfc.append(df_KFC[column_names_KFC[i]].min())
    q1_kfc.append(np.percentile(df_KFC[column_names_KFC[i]].values.tolist(), 25))
    q3_kfc.append(np.percentile(df_KFC[column_names_KFC[i]].values.tolist(), 75))
    iqr_kfc.append(np.percentile(df_KFC[column_names_KFC[i]].values.tolist(), 75) - np.percentile(df_KFC[column_names_KFC[i]].values.tolist(), 25))
    range_kfc.append(df_KFC[column_names_KFC[i]].max()-df_KFC[column_names_KFC[i]].min())
all_mean_cf=list(zip(column_names_CF[2:], mean_cf))
all_max_cf=list(zip(column_names_CF[2:], max_cf))
all_min_cf=list(zip(column_names_CF[2:], min_cf))
all_range_cf=list(zip(column_names_CF[2:],range_cf))
all_mean_kfc=list(zip(column_names_KFC[2:], mean_kfc))
all_max_kfc=list(zip(column_names_KFC[2:], max_kfc))
all_min_kfc=list(zip(column_names_KFC[2:], min_kfc))
all_range_kfc=list(zip(column_names_KFC[2:],range_kfc))
#Calculating Points for each eatery after comparing the Computed statistical data
points_cf=0
points_kfc=0
#For IQR
for i in range (len(iqr_cf)):
    if(iqr_cf[i]>iqr_kfc[i]):
        points_cf+=1
    elif(iqr_kfc[i]>iqr_cf[i]):
        points_kfc+=1
#For net range
for i in range (len(range_cf)):
    if(range_cf[i]>range_kfc[i]):
        points_cf+=1
    elif(range_kfc[i]>range_cf[i]):
        points_kfc+=1
#For mean
for j in range (len(all_mean_cf)):
    if(all_mean_cf[j][0]=='Calories' and all_mean_kfc[j][0]=='Calories'):
        if(all_mean_cf[j][1]>all_mean_kfc[j][1]):
            points_kfc+=1
        elif(all_mean_cf[j][1]<all_mean_kfc[j][1]):
           points_cf+=1
    elif(all_mean_cf[j][0]=='Fat (G)' and all_mean_kfc[j][0]=='Total Fat (g)'):
        if (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Sat. Fat (G)' and all_mean_kfc[j][0] == 'Saturated Fat (g)'):
        if (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Trans Fat (G)' and all_mean_kfc[j][0] == 'Trans Fat (g)'):
        if (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Cholesterol (MG)' and all_mean_kfc[j][0] == 'Cholesterol (mg)'):
        if (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Sodium (G)' and all_mean_kfc[j][0] == 'Sodium (g)'):
        if (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Carbohydrates (G)' and all_mean_kfc[j][0] == 'Total Carbohydrates (g)'):
        if (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Fiber (G)' and all_mean_kfc[j][0] == 'Dietary Fiber (g)'):
        if (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Sugar (G)' and all_mean_kfc[j][0] == 'Sugars (g)'):
        if (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_cf += 1
    elif (all_mean_cf[j][0] == 'Protein (G)' and all_mean_kfc[j][0] == 'Protein (g)'):
        if (all_mean_cf[j][1] < all_mean_kfc[j][1]):
            points_kfc += 1
        elif (all_mean_cf[j][1] > all_mean_kfc[j][1]):
            points_cf += 1
#common items-nutrient comparison
item_pts_cf=0
item_pts_kfc=0
df_chicksand_kfc= df_KFC[df_KFC['Item_name'].str.contains('Chicken Sandwich')]
mean=list(df_chicksand_kfc.iloc[:,2:].mean())
for i in range (0,len(df_chicksand_kfc)):
    for j in range(2, len(df_chicksand_kfc.columns)):
        df_chicksand_kfc.iloc[i,j]=mean[j-2]
df_chicksand_kfc = df_chicksand_kfc.loc[df_chicksand_kfc.drop_duplicates(subset=['Calories'], keep='first').index]
df_chicksand_cf=df_CF[df_CF['Item_name']=='Chick-fil-A Deluxe Sandwich w/ American']
df_milk_cf=df_CF[df_CF['Item_name']=='Chocolate Milkshake']
df_milk_kfc=df_KFC[df_KFC['Item_name']=='Chocolate Milk 1%']
df_kids_cf=df_CF[df_CF['Item_name']=="5 Ct Nuggets Kid's Meal"]
df_kids_kfc=df_milk_kfc=df_KFC[df_KFC['Item_name']=='Kentucky Fried Chicken Nuggets Kids Meal']
df_biscuit_cf=df_CF[df_CF['Item_name']=='Spicy Chicken Biscuit']
df_biscuit_kfc=df_KFC[df_KFC['Item_name']=='Spicy Crispy Chicken Breast']
list_cf=[df_chicksand_cf,df_milk_cf,df_kids_cf,df_biscuit_cf]
list_kfc=[df_chicksand_kfc,df_milk_kfc,df_kids_kfc,df_biscuit_kfc]
for i in range (len(list_cf)):
    if(list_cf[i]['Calories'].tolist()[0]>list_kfc[i]['Calories'].tolist()[0]):
        item_pts_kfc+=1
    elif(list_cf[i]['Calories'].tolist()[0]<list_kfc[i]['Calories'].tolist()[0]):
        item_pts_cf += 1
    elif (list_cf[i]['Fat (G)'].tolist()[0] >list_kfc[i]['Total Fat (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif(list_cf[i]['Fat (G)'].tolist()[0] <list_kfc[i]['Total Fat (g)'].tolist()[0]):
        item_pts_cf += 1
    elif (list_cf[i]['Sat. Fat (G)'].tolist()[0] > list_kfc[i]['Saturated Fat (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif(list_cf[i]['Sat. Fat (G)'].tolist()[0] < list_kfc[i]['Saturated Fat (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Trans Fat (G)'].tolist()[0] > list_kfc[i]['Trans Fat (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif(list_cf[i]['Trans Fat (G)'].tolist()[0] < list_kfc[i]['Trans Fat (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Cholesterol (MG)'].tolist()[0] > list_kfc[i]['Cholesterol (mg)'].tolist()[0]):
        item_pts_kfc += 1
    elif(list_cf[i]['Cholesterol (MG)'].tolist()[0] < list_kfc[i]['Cholesterol (mg)'].tolist()[0]):
        item_pts_cf += 1
    elif (list_cf[i]['Sodium (G)'].tolist()[0] > list_kfc[i]['Sodium (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Sodium (G)'].tolist()[0] < list_kfc[i]['Sodium (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif (list_cf[i]['Carbohydrates (G)'].tolist()[0] > list_kfc[i]['Total Carbohydrates (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Carbohydrates (G)'].tolist()[0] < list_kfc[i]['Total Carbohydrates (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif (list_cf[i]['Fiber (G)'].tolist()[0] > list_kfc[i]['Dietary Fiber (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Fiber (G)'].tolist()[0] < list_kfc[i]['Dietary Fiber (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif (list_cf[i]['Protein (G)'].tolist()[0] > list_kfc[i]['Protein (g)'].tolist()[0]):
        item_pts_cf += 1
    elif(list_cf[i]['Protein (G)'].tolist()[0] < list_kfc[i]['Protein (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif (list_cf[i]['Sugar (G)'].tolist()[0] > list_kfc[i]['Sugars (g)'].tolist()[0]):
        item_pts_kfc += 1
    elif(list_cf[i]['Sugar (G)'].tolist()[0] < list_kfc[i]['Sugars (g)'].tolist()[0]):
        item_pts_cf += 1
#Updating Primary Points counter
if(item_pts_kfc>item_pts_cf):
    points_kfc += 1
elif(item_pts_kfc<item_pts_cf):
    points_cf += 1
else:
    points_kfc += 1
    points_cf += 1

#Application of the preprocessed and analysed data- User Interaction
#Choosing items from chick-fil-a
cf=0
cf_items_dict=dict()
print("Hello User, Enter '1' to view the list of items in Chick-Fil-A or enter '2' to skip Chick-Fil-A")
n=int(input())
if(n==1):
    print("Welcome to Chick-Fil-A,to view the menu card, enter 'view menu'")
    st=input()
    if(st.lower()=="view menu"):
        print("""10 ct Chick-fil-A Chick-n-Minis
Spicy Chicken Biscuit
2 Ct Chick-n-Strips Kid's Meal
2 ct Chick-fil-A Chick-n-Strips
Egg White Grill
Hash Brown Scramble Burrito
Hash Brown Scramble Burrito w/ Nuggets
Bacon, Egg & Cheese Biscuit
Sausage, Egg & Cheese Biscuit
Bacon, Egg & Cheese Muffin
Sausage, Egg & Cheese Muffin
Hash Browns
Greek Yogurt Parfait w/ Cookie Crumbs
Fruit Cup
Small Fruit Cup
Breakfast Breads
English Muffin
Chick-fil-A Chick-n-Minis
Grilled Chicken Club w/ Colby Jack
Grilled Chicken Club w/ American
Chick-fil-A Chicken Biscuit
5 Ct Nuggets Kid's Meal
Chick-fil-A Deluxe Sandwich w/ American
Frosted Coffee
Frosted Peppermint Chip Coffee
Chocolate Chunk Cookie
Peppermint Chip Milkshake
Cookies & Cream Milkshake
Chocolate Milkshake
Vanilla Milkshake""")
        print("""Enter the exact name as per the menu(Including Caps) along with the quantity needed.
        Enter only one item at a time.
        If the user is done with selecting items enter 'exit' instead of the item name 
        """)
        while(True):
            print("enter the item name:")
            item=input()
            if(item.lower()=='exit'):
                break
            else:
                print('enter the quantity of the corresponding item in whole numbers')
                qt=int(input())
            cf_items_dict[item]=qt
            cf=cf+1
            if(cf>len(df_CF)):
                break
            else:
                pass
    else:
        print("wrong entry")
else:
    print("Visit Chick-Fil-A Later")

#Choosing items from KFC
kfc=0
kfc_items_dict=dict()
print("Hello User, Enter '1' to view the list of items in KFC or enter '2' to skip KFC")
n=int(input())
if(n==1):
    print("Welcome to KFC,to view the menu card, enter 'view menu'")
    st_new=input()
    if(st_new.lower()=="view menu"):
        print("""Double Down Sandwich
Spicy Double Down Sandwich
Caf Valley Lemon Cake (1 Slice)
Crispy Twister
Extra Crispy Tender (each)
Extra Crispy Chicken Breast
Kentucky Grilled Chicken Whole Wing
Spicy Crispy Chicken Breast
Original Recipe Chicken Breast
Nashville Hot Spicy Crispy Chicken Breast
BBQ Baked Beans
Macaroni Salad
Mashed Potatoes
Potato Salad
Secret Recipe Fries
Classic Chicken Sandwich
Original Recipe Chicken Drumstick
Spicy Chicken Sandwich
Chicken Pot Pie
Original Recipe Chicken Thigh
BBQ - Dipping Sauce Cup
Buffalo Ranch - Dipping Sauce Cup
Colonel's Buttery Spread
Honey Sauce Packet
KFC Sauce - Dipping Sauce Cup
Lemon Juice Packet
Kentucky Fried Chicken Nuggets Kids Meal
Chocolate Milk 1%""")
        print("""Enter the exact name as per the menu(Including Caps) along with the quantity needed.
        Enter only one item at a time.
        If the user is done with selecting items enter 'exit' instead of the item name 
        """)
        while(True):
            print("enter the item name:")
            item_new=input()
            if(item_new.lower()=='exit'):
                break
            else:
                print('enter the quantity of the corresponding item in whole numbers')
                qt_new=int(input())
            kfc_items_dict[item_new]=qt_new
            kfc=kfc+1
            if(kfc>len(df_KFC)):
                break
            else:
                pass
    else:
        print("wrong entry")
else:
    print("Visit KFC Later")
#Integrating User data with analysed data
keys_cf=cf_items_dict.keys()
values_cf=cf_items_dict.values()
keys_kfc=kfc_items_dict.keys()
values_kfc=kfc_items_dict.values()
with open("C:\\Users\\mania\\Downloads\\project_final_user_cf.csv", 'w', newline='') as csv_cf:
    csv_writer = csv.writer(csv_cf)
    csv_writer.writerow(df_CF.columns[1:])
    for item_user_cf in keys_cf:
        if item_user_cf in df_CF['Item_name'].tolist():
            rows = df_CF[df_CF['Item_name'] == item_user_cf].iloc[:, 1:].values.tolist()[0]
            csv_writer.writerow(rows)

with open("C:\\Users\\mania\\Downloads\\project_final_user_kfc.csv", 'w', newline='') as csv_kfc:
    csv_writer1 = csv.writer(csv_kfc)
    csv_writer1.writerow(df_KFC.columns[1:])
    for item_user_kfc in keys_kfc:
        if item_user_kfc in df_KFC['Item_name'].tolist():
            rows1 = df_KFC[df_KFC['Item_name'] == item_user_kfc].iloc[:, 1:].values.tolist()[0]
            csv_writer1.writerow(rows1)
final_cf_df=pd.read_csv("C:\\Users\\mania\\Downloads\\project_final_user_cf.csv")
final_kfc_df=pd.read_csv("C:\\Users\\mania\\Downloads\\project_final_user_kfc.csv")
final_cf_df['Quantity']=values_cf
final_kfc_df['Quantity']=values_kfc
final_cf_df.to_csv("C:\\Users\\mania\\Downloads\\project_final_user_cf.csv")
final_kfc_df.to_csv("C:\\Users\\mania\\Downloads\\project_final_user_kfc.csv")

for i in range(1, len(final_cf_df.columns)-1):
    column_name = final_cf_df.columns[i]
    column_values = final_cf_df[column_name].values.tolist()
    values_cf_lst = list(values_cf)
    column_values  = list([values_cf_lst[j]*column_values[j] for j in range(len(final_cf_df))])
    final_cf_df[column_name]=column_values

for k in range(1, len(final_kfc_df.columns)-1):
    column_name1 = final_kfc_df.columns[k]
    column_values1 = final_kfc_df[column_name1].values.tolist()
    values_kfc_lst = list(values_kfc)
    column_values1  = list([values_kfc_lst[m]*column_values1[m] for m in range(len(final_kfc_df))])
    final_kfc_df[column_name1]=column_values1
#Calculate the Recommended amount of calories and nutrients
print("Enter the required details to find the recommended amount of nutrients/food components")
print('enter your weight in pounds')
weight=int(input())
print("Select a goal: ‘weight_loss’, ‘maintenance’, ‘weight_gain’ ")
goal=input()
print("Select a body type: ‘endomorph’, ‘ectomorph’, ‘mesomorph’ ")
print(""" For Clarity: Endomorphs typically have a round or soft physique with a higher percentage of body fat. They tend to have a wider waist and hips.
Ectomorphs have a slender and lean build with narrow shoulders and hips. They often have a fast metabolism and may find it difficult to gain weight or muscle mass.
Mesomorphs are characterized by a more muscular and athletic physique. They have a naturally higher proportion of muscle mass and may have a broader chest and shoulders.  
""")
body_type=input()
print("Select an activity level, ‘sedentary’, ‘moderate’, ‘very’ ")
activity_level=input()
obj = MakeMeal(weight, goal=goal, activity_level= activity_level,body_type=body_type)
min_cal=obj.daily_min_calories()
max_cal=obj.daily_max_calories()
min_fat=obj.daily_min_fat()
max_fat=obj.daily_max_fat()
min_prot=obj.daily_min_protein()
max_prot=obj.daily_max_protein()
min_carbs=obj.daily_min_carbs()
max_carbs=obj.daily_max_carbs()
print("Minimum recommended calorie is",min_cal)
print("Maximum recommended calorie is",max_cal)
print("Minimum recommended fat in grams is",min_fat)
print("Maximum recommended fat in grams is",max_fat)
print("Minimum recommended protein in grams is",min_prot)
print("Maximum recommended protein in grams is",max_prot)
print("Minimum recommended carbohydrates in grams is",min_carbs)
print("Maximum recommended carbohydrates in grams is",max_carbs)
user_cal_cf=final_cf_df['Calories'].sum()
user_fat_cf=final_cf_df['Fat (G)'].sum()
user_prot_cf=final_cf_df['Carbohydrates (G)'].sum()
user_carb_cf=final_cf_df['Protein (G)'].sum()
user_cal_kfc=final_kfc_df['Calories'].sum()
user_fat_kfc=final_kfc_df['Total Fat (g)'].sum()
user_carb_kfc=final_kfc_df['Total Carbohydrates (g)'].sum()
user_prot_kfc=final_kfc_df['Protein (g)'].sum()
min_list=[min_cal,min_fat,min_prot,min_carbs]
max_list=[max_cal,max_fat,max_prot,max_carbs]
user_list_cf=[user_cal_cf,user_fat_cf,user_prot_cf,user_carb_cf]
user_list_kfc=[user_cal_kfc,user_fat_kfc,user_prot_kfc,user_carb_kfc]
#updating points as per user's case
#Based on the comparison between recommended calories and users calorie intake
user_cf=0
user_kfc=0
for i in range(len(min_list)):
    if(min_list[i]<user_list_cf[i]<max_list[i]):
        user_cf+=1
    elif(min_list[i]<user_list_kfc[i]<max_list[i]):
        user_kfc+=1
if(user_cf>user_kfc):
    print("Chick-Fil-A is recommended for the user")
    points_cf_user=points_cf+1
elif(user_kfc>user_cf):
    print("KFC is recommended for the user")
    points_kfc_user = points_kfc + 1
else:
    points_cf_user = points_cf + 1
    points_kfc_user = points_kfc + 1
    if(points_cf_user>points_kfc_user):
        print("Both the eateries align with the user's recommended range of nutrients, however Chick-Fil-A is prefered as its food items are nutritionally better")
    elif (points_cf_user < points_kfc_user):
        print("Both the eateries align with the user's recommended range of nutrients, however KFC is prefered as its food items are nutritionally better")
    else:
        print("Both the eateries align with the user's recommended range of nutrients")

print("points earned by Chick-Fil-A is",points_cf)
print("points earned by KFC is",points_kfc)
if(points_cf>points_kfc):
    print("Chick-Fil-A is better than KFC")
elif(points_kfc>points_cf):
    print("KFC is better than Chick-Fil-A")
else:
    print("Both are equally good, the most important parameter- IQR of nutritional parameters must be considered as a tie breaker")

print("points of Chick-Fil-A after user interaction is ",points_cf_user)
print("points of KFC after user interaction is", points_kfc_user)


#VISUALISATION
#boxplot for range representation
fig,ax=plt.subplots(2,5,figsize=(40, 16))
counter = 2
for i in range(0,5):
    sns.boxplot(x=df_CF.columns[counter], data=df_CF,ax=ax[0,i])
    sns.boxplot(x=df_KFC.columns[counter],data=df_KFC,ax=ax[1,i])
    ax[0,i].set_title('amount of' +df_CF.columns[counter]+'in the items provided by Chick-fil-A',fontsize=6)
    ax[1,i].set_title('amount of' +df_CF.columns[counter]+'in the items provided by KFC',fontsize=6)
    counter+=1
plt.tight_layout(pad=10)
plt.show()
fig,ax1=plt.subplots(2,5,figsize=(40, 16))
counter = 7
for i in range(0,5):
    sns.boxplot(x=df_CF.columns[counter], data=df_CF,ax=ax1[0,i])
    sns.boxplot(x=df_KFC.columns[counter],data=df_KFC,ax=ax1[1,i])
    ax1[0,i].set_title('amount of' +df_CF.columns[counter]+ 'in the items provided by Chick-fil-A',fontsize=6)
    ax1[1,i].set_title('amount of' +df_CF.columns[counter]+  'in the items provided by KFC',fontsize=6)
    counter+=1
plt.tight_layout(pad=10)
plt.show()
#visualise mean of all food components
#calories
eatery=['Chick-Fil-A','KFC']
mean_cal=[mean_cf[0],mean_kfc[0]]
plt.bar(eatery,mean_cal,width=0.5)
plt.title('Average calorie content of items provided by each eatery')
plt.xlabel("Eatery")
plt.ylabel("Amount of calories")
plt.show()
plt.tight_layout()
#fat and its types
X=['Fat','Sat. Fat','Trans Fat']
n=3
r = np.arange(n)
width = 0.25
mean_cf_fat=[df_CF['Fat (G)'].mean(),df_CF['Sat. Fat (G)'].mean(),df_CF['Trans Fat (G)'].mean()]
mean_kfc_fat=[df_KFC['Total Fat (g)'].mean(),df_KFC['Saturated Fat (g)'].mean(),df_KFC['Trans Fat (g)'].mean()]
plt.bar(r, mean_cf_fat, color = 'b',width = width, edgecolor = 'black',label='Chick-Fil-A')
plt.bar(r + width, mean_kfc_fat, color = 'g',width = width, edgecolor = 'black',label='KFC')
plt.xticks(r,X)
plt.xlabel("Fat and its types")
plt.ylabel("Amount in grams")
plt.title("Fat level(Avg.)comparison")
plt.legend()
plt.show()
#additional food components
X1=["Cholesterol","Sodium"]
n=2
r = np.arange(n)
width = 0.25
mean_cf_add=[df_CF['Cholesterol (G)'].mean(),df_CF['Sodium (G)'].mean()]
mean_kfc_add=[df_KFC['Cholesterol (g)'].mean(),df_KFC['Sodium (g)'].mean()]
plt.bar(r, mean_cf_add, color = 'b',width = width, edgecolor = 'black',label='Chick-Fil-A')
plt.bar(r + width, mean_kfc_add, color = 'g',width = width, edgecolor = 'black',label='KFC')
plt.xticks(r,X1)
plt.xlabel("Additional food component levels of every eatery")
plt.ylabel("Amount in grams")
plt.title("Additional food components(Avg.) comparison")
plt.legend()
plt.show()
#main food components
X2=['Carbs','fibre','sugar','protein']
n=4
r = np.arange(n)
width = 0.25
plt.bar(r, mean_cf[6:], color = 'b',width = width, edgecolor = 'black',label='Chick-Fil-A')
plt.bar(r + width, mean_kfc[6:], color = 'g',width = width, edgecolor = 'black',label='KFC')
plt.xticks(r,X2)
plt.xlabel("Main food component levels of every eatery")
plt.ylabel("Amount in grams")
plt.title("Main food components(Avg.) comparison")
plt.legend()
plt.show()
#Visualise food component values of common items in both eateries
categories=['chicken sandwich','chocolate milkshake','kids meal','chicken biscuit']
#Calories
calories_cf=[]
calories_kfc=[]
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(40,16))
for i in range(len(list_cf)):
    calories_cf.append(list_cf[i]['Calories'].values.tolist()[0])
    calories_kfc.append(list_kfc[i]['Calories'].values.tolist()[0])
ax[0].bar(categories, calories_cf, width=0.5)
ax[1].bar(categories, calories_kfc, width=0.5)
ax[0].set_title('calorie of common items in Chick-Fil-A')
ax[1].set_title('calorie of common items in KFC')
plt.setp(ax[0].get_xticklabels(), fontsize=8, rotation=90)
plt.setp(ax[1].get_xticklabels(), fontsize=8, rotation=90)
ax[0].set_xlabel("common item name")
ax[0].set_ylabel("amount of calories")
plt.tight_layout(pad=20)
plt.show()
#Fat and its types
fig, ax = plt.subplots(nrows=1,ncols=4,figsize=(20,8))
for i in range(len(list_cf)):
    columns = list_cf[i].columns.tolist()[3:6]
    ax[i].bar(columns,list_cf[i].values[0][3:6],label='Chick Fil A')
    bottom = list_cf[i].values[0][3:6]
    ax[i].bar(columns, list_kfc[i].values[0][3:6], label='KFC',bottom=bottom)
    plt.setp(ax[i].get_xticklabels(), fontsize=8, rotation=90)
    ax[i].set_xlabel(categories[i])
    ax[i].set_ylabel('Values')
    ax[i].set_title('Stacked Bar Chart for common items-fat',loc='center',fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
#Additional Food components
fig, ax1 = plt.subplots(nrows=1,ncols=4,figsize=(40,16))
for i in range(len(list_cf)):
    columns = list_cf[i].columns.tolist()[6:8]
    ax1[i].bar(columns,list_cf[i].values[0][6:8],label='Chick Fil A')
    bottom = list_cf[i].values[0][6:8]
    ax1[i].bar(columns, list_kfc[i].values[0][6:8], label='KFC',bottom=bottom)
    plt.setp(ax1[i].get_xticklabels(), fontsize=8, rotation=90)
    ax1[i].set_ylim(0.0,2.7)
    ax1[i].set_xlabel(categories[i])
    ax1[i].set_ylabel('Values')
    ax1[i].set_title('Stacked Bar Chart for common items-Add.components',loc='center',fontsize=6)
plt.legend()
plt.tight_layout(pad=20)
plt.show()
#Main Food components
fig, ax2 = plt.subplots(nrows=1,ncols=4,figsize=(20,8))
for i in range(len(list_cf)):
    columns = list_cf[i].columns.tolist()[8:12]
    ax2[i].bar(columns,list_cf[i].values[0][8:12],label='Chick Fil A')
    bottom = list_cf[i].values[0][8:12]
    ax2[i].bar(columns, list_kfc[i].values[0][8:12], label='KFC',bottom=bottom)
    plt.setp(ax2[i].get_xticklabels(), fontsize=8, rotation=90)
    ax2[i].set_ylim(0.0,120.0)
    ax2[i].set_xlabel(categories[i])
    ax2[i].set_ylabel('Values')
    ax2[i].set_title('Stacked Bar Chart for common items-Main components',loc='center',fontsize=6)
plt.legend()
plt.tight_layout()
plt.show()
#Correlation heat map to show relationship between food component parameters
df_CF_new=df_CF.drop(columns=['Item_name','Unnamed: 0'])
correlation=df_CF_new.corr()
sns.heatmap(correlation,annot=True)
plt.title('correlation heatmap for food components')
plt.show()
#pie-chart for main food components weightage
fig,ax=plt.subplots(1,2,figsize=(50, 32))
cf_pie=[]
kfc_pie=[]
for i in range(6,len(mean_cf)):
    cf_pie.append((all_mean_cf[i][1]/sum(mean_cf[6:]))*100)
    kfc_pie.append((all_mean_kfc[i][1] / sum(mean_kfc[6:])) * 100)
labels_cf=column_names_CF[8:12]
ax[0].pie(cf_pie)
ax[1].pie(kfc_pie)
ax[0].set_title("% weightage of main components in food items of Chick-Fil-A")
ax[1].set_title("% weightage of main components in food items of KFC")
plt.legend(loc='upper right',labels=labels_cf)
plt.show()
plt.tight_layout(pad=40,w_pad=20)