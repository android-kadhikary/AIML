import pandas as pd
file_data= pd.read_csv("")
df=pd.DataFrame(file_data)
print(df.head())
print (df.tail())
df.info()
df.describe()

df['age'].isNull() # check if the field is isNull
df.sort_values()

df.iloc([0:3]) # display rows, position based indexing
df_index_name=df.set_index("name_column")
df_index_name.loc("Karabi") # display rows, lable based indexing

#filtering data row, by applying condition to a name_column
filtered_data=df[df['age']>35]
#filter row where city is " kolkata"
details_ofMembersFromKolkata=df[df[city]=="kolkata"]

#filtering data with multiple condision &,|, ~
kolkata_below_45AgeMenmers=df[(df['age']<45) & (df['city'=='kolkata')] 

#filter rows with string matching
city_contains_Pur_members=df[df['city'].str.contains("pur")]

#if any city is null then there will be error ,to aviod this use na=False, inside the contains classmethod
city_contains_Pur_members=df[df['city'].str.contains("pur",na=False)]

#filter rows, where any value matching form given alternatives
city_A_B_C_members=df[df['city'].isin("A",'B','C')]


#Handling missing data
df.fillna(0) # replace the nan value with 0
#fill data from previous row
df.fillna(method='ffill')
#fill data from subsequent row, backword fill
df.fillna(method='bfill')
#to delete the entire row of a missing value
df.dropna()

#Rename a colomn name_column
df.rename(columns={"oldValue":"newValue"}, inplace=True)
# new new DF return, performed on original DF , whe inplace = True

#Replace a colomn name_column



df.replace({'karavi':"Karabi"},inplace=False) #dont want to change the original df

#group by(), one or more column, with sum, mean etc
total_Furniture_Sale_in_Kolkata=df.groupby("city").['sales'].sum
## Check if city in kolkata and bangalore is possible
#city_A_B_C_members=df[df['city'].isin("A",'B','C')]
#A_B_C_Total_sale=city_A_B_C_members['sale'].sum() # this must give the total of A,B,C city sale
#A_B_C_groupby_Sale_forEachCity=city_A_B_C_members.groupby('city')[sale].sum # this will display in 

#aggregation funtions, simultaneously
df.groupby("city").["sale"].agg(['sum','mean'])

#agg([]) function accepts a list of methods , like sum, mean, count

#sorting
#sort by age
df.sort_values(by='age', ascending=True)
df.sort_values(by=['age','score'], ascending=[True,False])

#merge 2 df with city name_column
df1=pd.DataFrame(read_csv)
df2=pd.DataFrame({'city':["A","B","C"],'Sales':[2000,5000,1600]})
pd.merge(df1,df2,key='city',how='outer')

#join
df1.join(df2,on='city',how='inner')

