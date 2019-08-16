import sys

runs = sys.argv[1:]
runs.reverse()

for i in range(len(runs)):

    run = str(runs[i])

    print()
    print('Run '+run)
    print()
    print('Link to pdf: https://github.com/jmhaefner/KrCalibNB/blob/gallery/doc/krCalib_'+run+'_rms.pdf')
    print('Selection NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/krSelectionAndFilter/kr_selection_and_filter_'+run+'_z_rms.ipynb')
    print('Maps NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/ltMaps/single_map_correction_'+run+'_z_rms.ipynb')
    print('Maps: https://github.com/jmhaefner/ICAROS/blob/master/maps/z_rms/kr_emap_xy_50_50_r_'+run+'.h5')
    print()
