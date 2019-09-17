# Run as "python automated_summary.py <run_no>"
#
# Assumes the existance of krCalib_TPLT.tex, and slides/runTPLT.tex.
# Creates version of those two files where TPLT is replaced by the
# run number. krCalib_ABCD.tex should be typesetable by TeXShop.
import sys

run_number = int(sys.argv[1])
tag = sys.argv[2]
if len(sys.argv) > 3:
    input_tag = sys.argv[3]
else:
    input_tag = tag

# Read in the variables and their values
vals_file_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/data_'
vals_file_location = vals_file_location+str(run_number)+input_tag+'/vals_'+str(run_number)+'.txt'
vals_file = open(vals_file_location, "r")


vars = []
vals = []

line = vals_file.readline()
while line:
    line = line.replace('\n', '')
    new_var = line[:line.find('=')]
    new_val = line[line.find('=')+1:]
    vars.append(new_var)
    vals.append(new_val)
    line = vals_file.readline()

# Read in the template, replacing all of the dummy variables with their values
template_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/runTPLT_TAG.tex'
template = open(template_location, "r")
mod_contents = template.read()
for i in range(len(vars)):
    name_to_replace = '<<'+vars[i]+'>>'
    mod_contents = mod_contents.replace(name_to_replace, vals[i])
mod_contents = mod_contents.replace('<<ANALYSISTAG>>', tag)
template.close()

# Save the new file
output_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/run'+str(run_number)+'_'+tag+'.tex'
output = open(output_location, "w")
output.write(mod_contents)
output.close()

# Duplicate the krCalib template with the correct run number
wrap_template_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/krCalib_TPLT_TAG.tex'
wrap_template = open(wrap_template_location, "r")
wrap_mod_contents = wrap_template.read()
wrap_mod_contents = wrap_mod_contents.replace('<<RUNNUMBER>>', str(run_number))
wrap_mod_contents = wrap_mod_contents.replace('<<ANALYSISTAG>>', tag)
wrap_template.close()
wrap_output_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/krCalib_'+str(run_number)+'_'+tag+'.tex'
wrap_output = open(wrap_output_location, "w")
wrap_output.write(wrap_mod_contents)
wrap_output.close()

# Duplicate the LaTeX template
# wrap_template_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/runTPLT_TAG.tex'
# wrap_template = open(wrap_template_location, "r")
# wrap_mod_contents = wrap_template.read()
# wrap_mod_contents = wrap_mod_contents.replace('<<ANALYSISTAG>>', tag)
# wrap_template.close()
# wrap_output_location = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/run'+str(run_number)+'_'+tag+'.tex'
# wrap_output = open(wrap_output_location, "w")
# wrap_output.write(wrap_mod_contents)
# wrap_output.close()
