#LOAD A TITANIC DATA SET
df=pd.read_csv("D:\\GIT\\titanic.csv")

#BASIC ANALSYS:
print(df.head(5))
print(df.info())
print(df.columns)
print(len(df))
print(df.describe)
print(df.isnull().sum())

