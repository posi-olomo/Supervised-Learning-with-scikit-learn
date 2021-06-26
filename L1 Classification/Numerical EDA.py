df.head()
"""
Out[1]:

        party  infants  water  budget  physician  salvador  religious  \
0  republican        0      1       0          1         1          1   
1  republican        0      1       0          1         1          1   
2    democrat        0      1       1          0         1          1   
3    democrat        0      1       1          0         1          1   
4    democrat        1      1       1          0         1          1   

   satellite  aid  missile  immigration  synfuels  education  superfund  \
0          0    0        0            1         0          1          1   
1          0    0        0            0         0          1          1   
2          0    0        0            0         1          0          1   
3          0    0        0            0         1          0          1   
4          0    0        0            0         1          0          1   

   crime  duty_free_exports  eaa_rsa  
0      1                  0        1  
1      1                  0        1  
2      1                  0        0  
3      0                  0        1  
4      1                  1        1  
"""

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 435 entries, 0 to 434
Data columns (total 17 columns):
party                435 non-null object
infants              435 non-null int64
water                435 non-null int64
budget               435 non-null int64
physician            435 non-null int64
salvador             435 non-null int64
religious            435 non-null int64
satellite            435 non-null int64
aid                  435 non-null int64
missile              435 non-null int64
immigration          435 non-null int64
synfuels             435 non-null int64
education            435 non-null int64
superfund            435 non-null int64
crime                435 non-null int64
duty_free_exports    435 non-null int64
eaa_rsa              435 non-null int64
dtypes: int64(16), object(1)
memory usage: 57.9+ KB
"""

df.describe()
"""
Out[3]:

          infants       water      budget   physician    salvador   religious  \
count  435.000000  435.000000  435.000000  435.000000  435.000000  435.000000
mean     0.429885    0.558621    0.606897    0.406897    0.521839    0.650575
std      0.495630    0.497123    0.489002    0.491821    0.500098    0.477337
min      0.000000    0.000000    0.000000    0.000000    0.000000    0.000000
25%      0.000000    0.000000    0.000000    0.000000    0.000000    0.000000
50%      0.000000    1.000000    1.000000    0.000000    1.000000    1.000000
75%      1.000000    1.000000    1.000000    1.000000    1.000000    1.000000
max      1.000000    1.000000    1.000000    1.000000    1.000000    1.000000

        satellite         aid     missile  immigration    synfuels  \
count  435.000000  435.000000  435.000000   435.000000  435.000000
mean     0.581609    0.590805    0.526437     0.512644    0.344828
std      0.493863    0.492252    0.499876     0.500416    0.475859
min      0.000000    0.000000    0.000000     0.000000    0.000000
25%      0.000000    0.000000    0.000000     0.000000    0.000000
50%      1.000000    1.000000    1.000000     1.000000    0.000000
75%      1.000000    1.000000    1.000000     1.000000    1.000000
max      1.000000    1.000000    1.000000     1.000000    1.000000

        education   superfund       crime  duty_free_exports     eaa_rsa
count  435.000000  435.000000  435.000000         435.000000  435.000000
mean     0.393103    0.537931    0.609195           0.400000    0.857471
std      0.489002    0.499133    0.488493           0.490462    0.349994
min      0.000000    0.000000    0.000000           0.000000    0.000000
25%      0.000000    0.000000    0.000000           0.000000    1.000000
50%      0.000000    1.000000    1.000000           0.000000    1.000000
75%      1.000000    1.000000    1.000000           1.000000    1.000000
max      1.000000    1.000000    1.000000           1.000000    1.000000
"""