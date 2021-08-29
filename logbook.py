import pandas as pd

df = pd.read_csv('logbook_2020.csv')

# Set column headers to the values in row [2]
# df.columns = df.iloc[2]

# drop the header rows (between column headers and data)
headers = df.iloc[2]
new_df  = pd.DataFrame(df.values[3:], columns=headers)
filtered_df = new_df[new_df['Orig'].notnull()]
df1 = filtered_df[['Date', 'Orig', 'Dest', 'RON']]

# Setup access to next and previous row data
df1['nextOrig'] = df1['Orig'].shift(-1)
df1['nextDest'] = df1['Dest'].shift(-1)
df1['lastRON'] = df1['RON'].shift(1)

# Mission continues if next origin is same as current destination
df1['Continues'] = (df1['Dest']==df1['nextOrig']) & (df1['Dest']!='STL')
df1['nextContinues'] = df1['Continues'].shift(-1)

r =[]
temp = ""

for index, row in df1.iterrows():
    # test next origin for match with current destination
    # if (row['Continues']== False):
    if (df1.loc[index, 'Continues']== False)  & (row['Orig']!= row['Dest']):
        if (index!=0):
            if (df1.loc[index, 'LastRON'].isalpha()==False):
                temp = row['Orig']
            else:
                temp = df1.loc[index, 'lastRON']
            r.append(temp + '-' + row['Dest'])

        # LastRON = null



        # if (df1['Dest']==df1['nextDest']):
        # join Orig and Dest strings
        # row['Leg'] = row['Orig'].str.cat(df1['Dest'],sep="-")
    # elif (df1.loc[index, 'Continues']==True) & (row['Dest']!= 'STL'):
        # df1.loc[index, 'RON'] = (row['Orig']+ '-' + row['Dest'])
    else:
        # row['Leg'] = row['Orig'].str.cat(row[["Dest", "nextDest"]].astype(str), sep="-")
        if (df1.loc[index, 'Dest']=='STL'):
            if (df1.loc[index, 'RON'].isalpha()==False):
                temp = row['Orig']
            else:
                temp = df1.loc[index, 'lastRON']
            r.append(temp + '-' + row['Dest'])
        else:
            if (df1.loc[index, 'RON'].isalpha()==False):
                temp = (df1.loc[index, 'Orig'])
            else:
                temp = (df1.loc[index, 'LastRON'])

        df1.loc[index, 'RON'] = (row['Orig']+ '-' + row['Dest'] + '-' + row['nextDest'])
# df1['nextDest'] = df1['Dest'].shift(-1)

print(df1)


# df1['leg'] = df1["Orig"] + '-' + df1["Dest"]
print(r)
# for row in df1.itertuples():
    # print (row.Orig + '-' + row.Dest)
