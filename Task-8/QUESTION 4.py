import pandas as pd
end=''
ser = pd.Series(['amrita', 'school', 'of', 'engineering','chennai', 'campus'])
for i in range(len(['amrita', 'school', 'of', 'engineering','chennai', 'campus'])):
    end+=(" "+ser[i])
print(end.title())
