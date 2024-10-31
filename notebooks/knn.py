#%%
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import logging

# Ativando o logging
logging.basicConfig(level=logging.INFO)