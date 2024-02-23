# iceberg thickness at calving point

**Input data file**: 
 - Ice shelf thickness file: Bedmachine Antarctic v3 https://nsidc.org/data/nsidc-0756/versions/3
 
**NEMO input file**:
Required:
 - A NEMO mesh mask
Optional:
 - A NEMO calving file (useful to check if there is still calving point with 0 thickness)

## Step 1: 

 - add lat/lon to the Bedmachine file
 - compute the ice mask (ie grounded or floating ice)

``` 
BedMachine2NEMOBAT.py -f bedmachinefile -epsg dataprojection (3031 for Bedmachine v3)
```

**Method:**
 - Find all the coastal point in NEMO
 - Find all the coastal point in Bedmachine (based on ice mask)
 - For each NEMO coastal point, compute the mean of all the bedmachine points within a raduis of d+5 [km]. d is the min distance between the NEMO coastal point and the list of Bedmachine coastal points. 

## Step 2: build the thickness file
- Run the notebook `Get_ICB_thickness.ipynb`

Note: the notebook is not generic. It will need to be adapted depending of your input file name and variable name.


