import numpy as np
import pandas as pd

def patient_dim_filter():
    
    patient_df = pd.read_csv("./conposcovidloc.csv")

    #null columns will be discarded 
    subset_columns = patient_df[["Age_Group", "Case_AcquisitionInfo", "Outbreak_Related", "Client_Gender"]].dropna()

    print(subset_columns)

    subset_columns.to_csv("filtered_patients.csv")




patient_dim_filter()
