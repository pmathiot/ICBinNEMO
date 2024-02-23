import numpy as np
import argparse
import pyproj
from netCDF4 import Dataset as nc

def get_args():
    ''' 
    read arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f"     , metavar='file_name'        , help="names of input files" , type=str  , required=True)
    parser.add_argument("-epsg"  , metavar='epsg code'        , help="epsg code"            , type=str  , required=True)
    return parser.parse_args()

def main():
    args = get_args()

    print('===== open netcdf')
    cinfile=args.f
    print(cinfile)
    ncfile = nc(cinfile,'r+')

    print('===== READ Coordinates' )
    x = ncfile.variables['x'][:]
    y = ncfile.variables['y'][:]

    print('===== Get grid' )
    xin ,yin = np.meshgrid(x,y)

    print('===== Get lat/lon' )
    p = pyproj.Proj('epsg:'+args.epsg)
    lon,lat = p(xin,yin,inverse=True)

    print('===== Print corner data' )
    print(lat[0,0], lon[0,0])
    print(lat[-1,-1], lon[-1,-1])
    print(lat[ 0,-1], lon[ 0,-1])
    print(lat[-1, 0], lon[-1, 0])

    print('===== Compute isf draft' )
    hsurf = ncfile.variables['surface'][:,:]
    hice  = ncfile.variables['thickness'][:,:]
    bed   = ncfile.variables['bed'][:,:]
    msko  = ncfile.variables['mask'][:,:]

    # floating ice is 3
    # ocean is 0
    msko[msko==0]  = -1 # bckup ocean cell
    msko[msko==3]  = -1 # bck up floating ice
    msko[msko>=0]  = 0  # mask everything else
    msko[msko==-1] = 1  # defined floating ice cell and ocean cell as ocean cell
    isfd = (hsurf - hice) * msko + bed * (1 - msko)

    # 
    mski   = ncfile.variables['mask'][:,:]
    mski[mski==1] = 0
    mski[mski>1 ] = 1

    print('===== Write data')
    vlat  = ncfile.createVariable('lat' , 'float',('y', 'x'))
    vlon  = ncfile.createVariable('lon' , 'float',('y', 'x'))
    visfd = ncfile.createVariable('isfd', 'float',('y', 'x'))
    vmsko = ncfile.createVariable('msk_oce', 'float',('y', 'x'))
    vmski = ncfile.createVariable('msk_ice', 'float',('y', 'x'))
    vlat[:,:]  = lat
    vlon[:,:]  = lon
    visfd[:,:] = isfd
    vmsko[:,:] = msko
    vmski[:,:] = mski

    print('===== Close file')
    ncfile.close()
     
if __name__ == '__main__':
    main()
