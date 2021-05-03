# qbio_data_analysis_final_project
QBIO Public Data Analysis Final Project (Spring 2021): Correlation Between Differentially Expressed Genes in mRNA Transcripts and Protein Abundance in Relation to Survivability

# Setup and Bash

 Setup: Prior to running code, set up a conda environemnt with the necessary packages using the steps below
 
  1) conda create -n <env_name> --file requirements.txt
  2) conda activate <env_name>
  3) install cptac
  4) pip install cptac


 Bash: To produce all figures and data, run ./final_project_bash.sh
 
 


# Code

  Languages: Python and R
  
  1) CPTAC.py
  2) differential_analysis.R
  3) spearman.py
  
# Output

  Types: Raw Data (rd) and Figures (f)
  
  Organization: final_project_data (contains csv raw data files), final_project_figures (contains jpg figure files), and GDCdata (contains all data from GDC query)
  
  1) CPTAC.py
  
      a) clinical_CPTAC.csv (rd, final_project_data)
      
      b) proteomics_CPTAC.csv (rd, final_project_data)
      
      c) transcriptomics_CPTAC.csv (rd, final_project_data)
      
  2) differential_analysis.R
  
      a) GDC query data (rd, GDCdata)
      
      b) DEseq2 volcano plot (f, final_project_figures)
      
      c) DEseq2 results (rd, final_project_data)
      
      d) DEseq2 up-regulated results (rd, final_project_data)
      
      e) DEseq2 down-regulated results (rd, final_project_data)
      
      f) Deseq2 kaplan-meier plots for the top 5 up and down regulated genes (f, final_project_figures)
      
      g) limma volcano plot (f, final_project_figures)
      
      h) limma results (rd, final_project_data)
      
      i) limma up-regulated results (rd, final_project_data)
      
      j) limma down-regulated results (rd, final_project_data)
      
      k) limma kaplan-meier plots for the top 5 up and down regulated genes (f, final_project_figures)
      
  3) spearman.py
  
      a) spearman correlation plots for the top 5 up and down regulated genes from DEseq2 and limma (f, final_project_figures)
      
      
