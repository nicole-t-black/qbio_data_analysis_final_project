import cptac
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

wd = os.getcwd()

### download BRCA dataset from CPTAC ###
cptac.download(dataset="Brca")
br = cptac.Brca()

# set protein (1 level), rna, clinical dataframes #
proteomic_CPTAC = br.get_proteomics()
proteomic_CPTAC = proteomic_CPTAC.droplevel(1, axis=1)
transcriptomic_CPTAC = br.get_transcriptomics()
clinical_CPTAC = br.get_clinical()

# save data for future use #
proteomic_CPTAC.to_csv("final_project_data/proteomic_CPTAC.csv")
transcriptomic_CPTAC.to_csv("final_project_data/transcriptomic_CPTAC.csv")
clinical_CPTAC.to_csv("final_project_data/clinical_CPTAC.csv")
