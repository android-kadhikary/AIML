import seaborn as sbn
import matplotlib.pyplot as plt
#set uniform look for presentation.
#palette : select a color scheme : deep, muted, bright, 
sbn.set_theme(style="whitegrid", context="notebook",palette="deep", font="", font_scale=10,color_codes="red")
tips=sbn.load_dataset("tips") # Important : seaborn load_dataset() method returns pandas dataframe, all the methods lik info, head, tail, describe
# sbn.scatterplot(x= "total_bill", y="tip", data ="tips")
# plt.show()

# print(tips.info())
# print(tips.head())
# print(tips.tail())
# print(tips.describe())
print(tips["smoker"].value_counts())
print(tips["smoker"].values)