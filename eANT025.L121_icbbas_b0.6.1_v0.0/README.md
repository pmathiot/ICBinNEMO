# How to build the basin file for icebergs

**Input files**:
 - Basin file for Antarctica (if needed)
 - Basin file for Greenland (if needed)
 - NEMO mesh mask
 - NEMO calving file

## Method:

 - run: `Build_icb_basinid_file_ORCA2.ipynb` for global (need to be a bit adapted to add Greenland). For now, Greenland icb have one 1 id and no basin. Use the same idea as the one used for Antarctica.

 For Antarctica only, use `Build_icb_basinid_file.ipynb`

**Method:**
 - Find the NEMO coastal point for Antarcica and Greenland (need to adjust the seed)
 - Find the coastal point from the basin file
 - Set the NEMO basin value to the nearest basinid from the coastal point of the source file.
 - Calving point to far from Antarctica or Greenland are set to a default value (100)
