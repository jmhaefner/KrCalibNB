#!/bin/bash
# To be run as 'sh kr_automated_full.sh <run_no>'

# Find list of all data we have

# Go ten forward from that

run_no=$1
if sshpass -p "djshmooshmoo2323&" ssh -q jhaefner@neutrinos1.ific.uv.es "[ -d /analysis/$run_no/hdf5/prod/v0.9.9/20190111/kdst/trigger1/ ]"
then
  {
    #echo Found run $run_no

    #cd /Volumes/NEXT_data/IC_Data/kdst/ && python move_kdsts.py $run_no
    #cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles
    #python automated_selection.py $run_no

    python automated_correction.py $run_no

    cd ~/Development/KryptonCalibration/KrCalib2.0/ICAROS/
    git checkout master
    cp /Volumes/NEXT_data/IC_Data/maps/kr_emap_xy_50_50_r_$run_no.h5 /Users/jmhaefner/Development/KryptonCalibration/KrCalib2.0/ICAROS/maps/kr_emap_xy_50_50_r_$run_no.h5
    git add *
    commit -m "Add run $run_no"

    # works
    # cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/
    # python automated_summary.py $run_no
    # open -a TeXshop krCalib_$run_no.tex
  }
else
  {
    echo Could not find the requested run $run_no
  }
fi
