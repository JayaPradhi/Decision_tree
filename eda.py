#LOAD A TITANIC DATA SET
df=pd.read_csv("D:\\GIT\\titanic.csv")

#BASIC ANALSYS:
print(df.head(5))
print(df.info())
print(df.columns)
print(len(df))
print(df.describe)
print(df.isnull().sum())

#PIE CHART FOR SURVIVIED COLUMN
f,ax=plt.subplots(1,2,figsize=(10,8))
explode=[0.1] * len(df['Survived'].value_counts())
df['Survived'].value_counts().plot.pie(ax=ax[0],explode=explode,autopct='%1.1f%%')
ax[0].set_title('pie chart')
sns.countplot(x="Survived",data=df,ax=ax[1])
ax[1].set_title("Count plot")
plt.show()



