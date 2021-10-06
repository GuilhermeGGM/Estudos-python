import pandas as pd
perfilm = pd.read_csv('Perfilm.csv', sep=';', encoding='latin1')
perfilm.to_parquet('Perfil.pq')
parquet = pd.read_parquet('Perfil.pq')
parquet.info()
