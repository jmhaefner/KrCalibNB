import sys

for i in range(len(sys.argv)-1):

    run = str(sys.argv[i+1])

    print()
    print('Run '+run)
    print()
    print('Link to pdf: https://github.com/jmhaefner/KrCalibNB/blob/gallery/doc/krCalib_'+run+'.pdf')
    print('Selection NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/krSelectionAndFilter/kr_selection_and_filter_'+run+'.ipynb')
    print('Maps NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/ltMaps/single_map_correction_'+run+'.ipynb')
    print('Maps: https://github.com/jmhaefner/ICAROS/blob/master/maps/kr_emap_xy_50_50_r_'+run+'.h5')
    print()
