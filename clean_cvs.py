import pandas as pd

input_file = '/home/kotarum/Documentos/Unit_2/lab-sql-6/files_for_lab/films_2020.csv'
output_file = '/home/kotarum/Documentos/Unit_2/lab-sql-6/files_for_lab/films_2020_clean.csv'

df = pd.read_csv(input_file)


df.fillna(value=0, inplace=True)

df.to_csv(output_file, index=False)