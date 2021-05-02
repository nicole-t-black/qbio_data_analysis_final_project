import cptac
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

wd = os.getcwd()

### spearman function ###
def create_spearman(gene):

    assert list(rna_data.index) == list(protein_data.index)

    rna_gene = rna_data.loc[:, gene]
    protein_gene = protein_data.loc[:, gene]

    rho, spear_pvalue = stats.spearmanr( rna_gene, protein_gene )

    plt.figure( figsize=(10,10) )
    plt.scatter( rna_gene, protein_gene )

    title = "rho: {} for {}".format(rho, gene)
    plt.title(title)

    plt.xlabel("Transcriptomic Expression")
    plt.ylabel("Proteomic Expression")

    plt.savefig( "{}/data/{}_Spearman_Correlation_Plot.png".format(wd, gene), bbox_inches="tight" ) #Use this when saving figure in script

#all genes from differential analysis (commented out if not in CPTAC database)

create_spearman("ESR1")
create_spearman("PTGR2")

#create_spearman("TRH")
#create_spearman("ARHGAP36")
#create_spearman("AMER2")
#create_spearman("CHRNA4")
#create_spearman("ELAVL3")

create_spearman("CARTPT")
#create_spearman("DCAF4L2")
#create_spearman("LACRT")
#create_spearman("CYP2A7")
create_spearman("GNAT3")
