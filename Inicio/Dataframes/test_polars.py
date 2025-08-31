import polars as pl
import datetime as dt

df = pl.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "birthdate": [
            dt.date(1990, 5, 1),
            dt.date(1985, 8, 12),
            dt.date(2000, 1, 23),
            dt.date(1995, 3, 15),
            dt.date(1988, 7, 30),
        ],
        "weight": [68, 75, 80, 90, 55], # (kg)
        "height": [165, 180, 175, 190, 160], # (cm)
       
    }
)

#print(df)
 
df.write_csv("docs/assets/data/people.csv")  
df_csv = pl.read_csv("docs/assets/data/people.csv")
print(df_csv) 

