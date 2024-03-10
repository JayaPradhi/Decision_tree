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

#MALE VS FEMALE
f,ax=plt.subplots(1,2,figsize=(10,8))
df["Sex"].value_counts().plot.bar(ax=ax[0],title="gender count")
sns.countplot(x='Sex',hue='Survived',ax=ax[1],data=df)
ax[1].set_title('Male vs female')
plt.show()

#SIBSP VS SURVIVED
f,ax=plt.subplots(1,2,figsize=(10,8))
df['SibSp'].value_counts().plot.bar(ax=ax[0],color='red',edgecolor="black")
ax[0].set_title("sibsp count")
sns.countplot(x='SibSp',data=df,ax=ax[1],hue='Survived')
ax[1].set_title("sibsp vs survived")

#DISTIBUTION FOR AGE AND  FAER
sns.distplot(df['Age'],color='red')
sns.distplot(df["Age"],color='black')


#SURVIVED VS CLASS

f,ax=plt.subplots(1,2,figsize=(10,8))
df["Pclass"].value_counts().plot.bar(ax=ax[0],color='red')
ax[0].set_title("passenger class")
sns.countplot(x="Pclass",data=df,hue='Survived')
ax[1].set_title("survived vs passenger class")
plt.show()

#Embarked vs survived
f,ax=plt.subplots(1,2,figsize=(10,8))
df["Embarked"].value_counts().plot.bar(ax=ax[0],color="skyblue")
ax[0].set_title('embarked')
sns.countplot(x="Embarked",data=df,ax=ax[1])
ax[1].set_title("Embarked vs survived")


#SURVIVED VS AGE VS NOT SURVIVED
f,ax=plt.subplots(1,2,figsize=(10,8))
df[df['Survived']==0]['Age'].plot.hist(bins=20,color='red',edgecolor="black",ax=ax[0])
a=list(range(5,85,5))
ax[0].set_xticks(a)
ax[0].set_title('survived vs age')
df[df['Survived']==1]['Age'].plot.hist(bins=20,ax=ax[1],edgecolor='black')
ax[1].set_xticks(a)
ax[1].set_title("not survived va age")
plt.show()


#grouby

df.groupby(['Sex','Survived'])['Survived'].count()


#CORRELATION
sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.show()


#EMBARKED
f,ax=plt.subplots(2,2,figsize=(10,8))
df['Embarked'].value_counts().plot.bar(color="red",ax=ax[0,0])
sns.countplot(x='Embarked',data=df,hue="Sex",ax=ax[0,1])
sns.countplot(x='Embarked',data=df,hue='Pclass',ax=ax[1,0])
sns.countplot(x='Embarked',data=df,hue='Survived')