# Data Preprocessing 

# 1) Handling Null Values
# 2) Handling Duplicates Rows
# 3) Checking the data types - Data that ML model will utilize will not be object(str)
# a) Encoding methods
# 4) Coorelation
# a) It represent the magnitude and direction of linear relationship between 2 variables
# b) It ranges from -1 to +1.
# c) -1 indicates strong negative correlation.
# d) If corr(x,y) is Positive as x increases y increases and vice versa.
# d) If corr(x,y) is Negative as x increases y decreases and vice versa.


# Data Transformation
# 1) Encoding categorical Columns
# a) Find and Replace - replace or map or apply or np.where
#     np.where(coondition,true,false)
# b) LabelEncoder
# c) OneHotEncoder (Get_Dummies)

# 2) Scaling the Features
# a) StandardScaler
# b) MinMaxScalar

# Cross Validation
# 1) It is a resampling technique
# 2) Drawback of train_test_split - There is no variation in train and 
# test data at a given random_state

import numpy as np
from sklearn.model_selection import cross_val_score,KFold

x = np.array([43,21,5,65,82,39,23,14,70,56])
kf = KFold(n_splits=6)

for Train,Test in kf.split(x):
    print('Train',x[Train],'Test',x[Test])
