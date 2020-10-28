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
    print('Notebook: https://github.com/jmhaefner/KrCalibNB/blob/gallery/krSelectionAndFilter/kr_selfilcor_'+run+'_'+tag+'.ipynb')
    print('Maps: https://github.com/jmhaefner/ICAROS/blob/master/maps/'+tag+'/kr_emap_xy_r_'+run+'_'+tag+'.h5')
    print()
