import pandas as pd
#PRE-PROCESSING CHICK-FIL-A DATA
#read data in csv
df=pd.read_csv("C:\\Users\\mania\\Downloads\\chick_fil_a_raw.csv",encoding='latin1')
#drop the column which is not needed for analysis
df.drop(['Serving size'],axis=1,inplace=True)
#rename the first column
df.rename(columns={'Breakfast':'Item_name'},inplace=True)
#remove redundant items with escape characters
df = df[~df["Item_name"].str.contains('\n')]
#drop duplicates based on item name:repeated items
df.drop_duplicates(subset=['Item_name'],keep='first',inplace=True)
#re-index the Data Frame
df.index=pd.RangeIndex(1,len(df)+1,1)
#convert calorie data to int data type and update the Dataframe with the new_cal values
l=df['Calories'].values
new_cal=[]
for i in range (len(l)):
    new_cal.append(int(l[i]))
df.iloc[:,1]=new_cal
#Convert the unit of Sodium and cholesterol data and rename the column
x = []
for i in range(len(df['Sodium (MG)'])):
    x.append(df['Sodium (MG)'].values.tolist()[i] / 1000)
df['Sodium (MG)'] = x
df.rename(columns={'Sodium (MG)': 'Sodium (G)'}, inplace=True)

y = []
for i in range( len(df['Cholesterol (MG)'])):
    y.append(df['Cholesterol (MG)'].values.tolist()[i] / 1000)
df['Cholesterol (MG)'] = y
df.rename(columns={'Cholesterol (MG)': 'Cholesterol (G)'}, inplace=True)

#Group items with same substring and put the group names in a list
df_filtered_hashbrown = df[df['Item_name'].str.contains('Hash Brown Scramble Burrito')]
df_filtered_hashbrown1 = df[df['Item_name'].str.contains('Hash Brown Scramble Bowl')]
df_filtered_deluxe= df[df['Item_name'].str.contains('Deluxe Sandwich')]
df_filtered_chicken= df[df['Item_name'].str.contains('Chicken Sandwich')]
df_filtered_nuggets= df[df['Item_name'].str.contains('Nuggets')]
df_filtered_strips= df[df['Item_name'].str.contains('Chick-n-Strips')]
substrings_list=[df_filtered_hashbrown,df_filtered_hashbrown1,df_filtered_deluxe,df_filtered_chicken,df_filtered_nuggets,df_filtered_strips]
#Create empty lists to store its mean values
mean_hashbrown=[]
mean_hashbrown1=[]
mean_deluxe=[]
mean_chicken=[]
mean_nuggets=[]
mean_strips=[]
mean_list=[mean_hashbrown,mean_hashbrown1,mean_deluxe,mean_chicken,mean_nuggets,mean_strips]
#find mean value for each attribute of the grouped items
column_names=df.iloc[1,:].index
for a in range (len(substrings_list)):
        for b in range (1,len(column_names)):
            x=substrings_list[a][column_names[b]].mean()
            mean_list[a].append(x)
        df.iloc[substrings_list[a].index,1:]=mean_list[a]
#drop duplicates based on analysis attributes :repeated values
df.drop_duplicates(subset=['Calories'],keep='first',inplace=True)
df.index=pd.RangeIndex(1,len(df)+1,1)
#final-removal of data
df_filtered_hashbrown_new = df[df['Item_name'].str.contains('Hash Brown Scramble Burrito')]
df_filtered_chicken_new=df[df['Item_name'].str.contains('Grilled Chicken Club')]
df.iloc[df_filtered_hashbrown_new.index[1:], 1:] = 0
df.iloc[df_filtered_chicken_new.index[1:],1:]=0
df.drop(df[df['Calories']==0].index,axis=0,inplace=True)
df.index=pd.RangeIndex(1,len(df)+1,1)
#removing special characters from the names and updating the csv
spl_names=[]
spl_names_new=[]
spl_chr_cf=[]
for j in range (1,len(df['Item_name'])):
    for char in df['Item_name'][j]:
        if ord(char)>127:
            spl_names.append(df['Item_name'][j])
            spl_chr_cf.append(char)
for word in spl_names:
    name=''
    for ch in word:
        if ch not in spl_chr_cf:
            name=name+ch
    spl_names_new.append(name)
index = []
for j in range(len(df['Item_name'])):
    for word in sorted(list(set(spl_names))):
        indices = df.loc[df['Item_name'] == word].index.tolist()
        index.extend(indices)
index = list(set(index))
for k in range(len(index)):
    df.loc[index[k], ['Item_name']] = sorted(list(set(spl_names_new)))[k]
df.index=pd.RangeIndex(1,len(df)+1,1)
final_csv=df.to_csv("C:\\Users\\mania\\Downloads\\project_final_chickfila.csv")


#PRE-PROCESSING KFC DATA
#read data in csv
df_kfc=pd.read_csv("C:\\Users\\mania\\Downloads\\KFC_Raw.csv")
#Removing data that is not needed for analysis
x=df_kfc[df_kfc['Item_name']=='Beverages'].index
df_unwanted=df_kfc.iloc[x[0]+1:,:]
df_kfc.drop(df_unwanted.index,axis=0,inplace=True)
df_kfc.drop(columns=['Sodium (Mg)','Added Sugars (g)'],axis=1,inplace=True)
#Checking for NaN
print(df_kfc.isna().sum())
#Removing NaN Data
df_Nan=df_kfc[df_kfc.isna().any(axis=1)]
df_kfc.drop(df_Nan.index,axis=0,inplace=True)
#convert calorie and sodium data to int data type and update the Dataframe with the new_cal values
l_kfc=df_kfc['Calories'].values
l1_kfc=df_kfc['Sodium (g)'].values
new_cal_kfc=[]
new_cal_kfc1=[]
for i in range (len(l_kfc)):
    new_cal_kfc.append(int(l_kfc[i]))
    new_cal_kfc1.append(int(l1_kfc[i]))
df_kfc.iloc[:,1]=new_cal_kfc
df_kfc.iloc[:,6]=new_cal_kfc1
#convert the values of cholesterol to g and rename the column
m=[]
for k in range( len(df_kfc['Cholesterol (mg)'])):
    m.append(df_kfc['Cholesterol (mg)'].values.tolist()[k] / 1000)
df_kfc['Cholesterol (mg)'] = m
df_kfc.rename(columns={'Cholesterol (mg)': 'Cholesterol (g)'}, inplace=True)
#Group items with same substring and put the group names in a list
df_filtered_origichick = df_kfc[df_kfc['Item_name'].str.contains('Original Recipe')]
df_filtered_crispchick = df_kfc[df_kfc['Item_name'].str.contains('Extra Crispy Chicken Breast')]
df_filtered_grillchick = df_kfc[df_kfc['Item_name'].str.contains('Kentucky Grilled Chicken')]
df_filtered_spicychick = df_kfc[df_kfc['Item_name'].str.contains('Spicy Crispy Chicken')]
df_filtered_nashchick = df_kfc[df_kfc['Item_name'].str.contains('Nashville Hot Spicy Crispy Chicken Breast')]
substrings_list_kfc=[df_filtered_origichick,df_filtered_crispchick,df_filtered_grillchick,df_filtered_spicychick,df_filtered_nashchick]
#Create empty lists to store its mean values
mean_origichick=[]
mean_crispchick=[]
mean_grillchick=[]
mean_spicychick=[]
mean_nashchick=[]
mean_list_kfc=[mean_origichick,mean_crispchick,mean_grillchick,mean_spicychick,mean_nashchick]
#find mean value for each attribute of the grouped items
column_names_kfc=df_kfc.iloc[1,:].index
for a in range (len(substrings_list_kfc)):
        for b in range (1,len(column_names_kfc)):
            y=substrings_list_kfc[a][column_names_kfc[b]].mean()
            mean_list_kfc[a].append(y)
        df_kfc.iloc[substrings_list_kfc[a].index,1:]=mean_list_kfc[a]
#drop duplicates based on analysis attributes :repeated values
df_kfc.drop_duplicates(subset=['Calories'],keep='first',inplace=True)
df_kfc.index=pd.RangeIndex(1,len(df_kfc)+1,1)
#remove unwanted special characters from the names of items
spl_names_kfc=[]
spl_names_new_kfc=[]
spl_chr=[]
for j in range (1,len(df_kfc['Item_name'])):
    for char in df_kfc['Item_name'][j]:
        if ord(char)>127:
            spl_names_kfc.append(df_kfc['Item_name'][j])
            spl_chr.append(char)
for word in spl_names_kfc:
    name=''
    for ch in word:
        if ch not in spl_chr:
            name=name+ch
    spl_names_new_kfc.append(name)
index = []
for j in range(len(df_kfc['Item_name'])):
    for word in sorted(list(set(spl_names_kfc))):
        indices = df_kfc.loc[df_kfc['Item_name'] == word].index.tolist()
        index.extend(indices)
index = list(set(index))
for k in range(len(index)):
    df_kfc.loc[index[k], ['Item_name']] = sorted(list(set(spl_names_new_kfc)))[k]
#final preprocessing and removal of unwanted data
df_filtered_family=df_kfc[df_kfc['Item_name'].str.contains('(Family)')]
df_kfc.drop(df_filtered_family.index,axis=0,inplace=True)
df_kfc.drop_duplicates(subset=['Item_name'],keep='first',inplace=True)
df_kfc.index=pd.RangeIndex(1,len(df_kfc)+1,1)
final_csv_KFC=df_kfc.to_csv("C:\\Users\\mania\\Downloads\\project_final_KFC.csv")




