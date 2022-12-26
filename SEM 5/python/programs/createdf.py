import pandas as pd
data={'cars':['BMW','VOLVO','ALTO'],'owner':['rishabh','jaka','mina']}

df1=pd.DataFrame(data)
print(df1)


print("\n\n")

book_store={'book':['python','java','AI','python'],'author':['abc','xyz','jkl','abc']}
df2=pd.DataFrame(book_store)
print(df2)

print("\n\n")

print("removing duplicates from the data frame")
df3=df2.drop_duplicates(keep='last')
print(df3)


df4=pd.DataFrame(data, index = ["day1","day2","day3"])
print(df4)

#to read file in the dataframe we use df=pd.read_csv('filename.csv')