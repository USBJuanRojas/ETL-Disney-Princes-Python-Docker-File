import kagglehub
import pandas as pd
from pymongo import MongoClient

#path = kagglehub.dataset_download("C:\Users\jroja\OneDrive\Documents\big data\Act 1 Cort 3")

df = pd.read_csv("C:/Users/jroja/OneDrive/Documents/big data/Act 1 Cort 3/disney_princess.csv")
dfc = df.copy()

dfc.drop([
    'FirstMovieTitle', 'NumberOfSongs', 'HasSoloSong', 'HasDuet', 'HairColor',
    'EyeColor', 'OutfitPrimaryColor', 'OutfitStyleEra', 'IsRoyalByBirth',
    'MagicType', 'MainSetting', 'FightsVillainDirectly', 'RomanticSubplot',
    'VillainName', 'Top3Hashtags', 'IsIconic'
], axis=1, inplace=True)

URI = "mongodb+srv://jrojasn:jrojasnusbjajaxd@cluster0.h9fcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    connection = MongoClient(URI)
    print("Conexión exitosa a MongoDB")
except Exception as e:
    print("Error al conectarse a la base de datos:", e)

db = connection["Disney"]
collection = db["Princesas"]

data_dict = dfc.to_dict("records")

collection.insert_many(data_dict)
print("Datos insertados en MongoDB")



#Dockerfile




