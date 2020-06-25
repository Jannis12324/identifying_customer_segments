import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snsy

# magic word for producing visualizations in notebook
#%matplotlib inline

# Load in the general demographics data.
azdias = pd.read_csv("Udacity_CUSTOMERS_Subset.csv", delimiter = ";")


# Load in the feature summary file.
feat_info = pd.read_csv("AZDIAS_Feature_Summary.csv", delimiter = ";")

# Identify missing or unknown data values and convert them to NaNs.
def list_convert(line):
    line = line.replace("[", "")
    line = line.replace("]", "")
    a = line.split(",")
    return a
feat_info["missing_or_unknown"] = feat_info["missing_or_unknown"].apply(list_convert)
# Sets the attribute as index so it is easier to handle with the .loc mehtod
feat_info.set_index("attribute", inplace = True)



# Iterates through the columns of azdias
for column in azdias.columns:
    # saves the values as a list which are nan in this colum
    null_values = feat_info.loc[str(column), "missing_or_unknown"]
    for entry in null_values:
        # Some columns do not have an indicator for null values,
        if (entry != "") & (entry.isdigit()):
            # replaces every null value with an np.nan in the column
            azdias[column] = azdias[column].replace(int(entry), np.nan)
        # 3 rows have "X", for marking missing values
        elif (entry != "") & (entry.isalpha()):
            # replaces every null value with an np.nan in the column
            azdias[column] = azdias[column].replace(entry, np.nan)