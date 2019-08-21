import sys

tag = sys.argv[1]
runs = sys.argv[2:]
runs.reverse()

for i in range(len(runs)):

    run = str(runs[i])

    print()
    print('Run '+run)
    print()
    print('Link to pdf: https://github.com/jmhaefner/KrCalibNB/blob/gallery/doc/krCalib_'+run+'_'+tag+'.pdf')
    print('Selection NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/krSelectionAndFilter/kr_selection_and_filter_'+run+'_'+tag+'.ipynb')
    print('Maps NB: https://github.com/jmhaefner/KrCalibNB/blob/gallery/ltMaps/single_map_correction_'+run+'_'+tag+'.ipynb')
    print('Maps: https://github.com/jmhaefner/ICAROS/blob/master/maps/'+tag+'/kr_emap_xy_50_50_r_'+run+'.h5')
    print()
