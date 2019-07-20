print('hi world')

all_runs = []
all_fracs = []

run_min = 6940
run_max = 7005

for run in range(run_min, run_max):

    outer_path = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/'
    full_path = outer_path + 'data_' + str(run) + '/vals_' + str(run) + '.txt'

    try:

        test_file = open(full_path, "r")
        # print(full_path)
        for line in test_file:
            if not line.find('fracS1S2') == -1:
                fracS1S2 = float(line[9:])
                # print('Frac S1 + S2 = ' + str(fracS1S2))
                all_runs.append(run)
                all_fracs.append(fracS1S2)

    except:
        pass

import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})
plt.grid(True)
plt.grid(linestyle='-')
plt.plot(all_runs, all_fracs, 'o')
plt.ylabel('Efficiency % (inclusive)')
plt.xlabel('Run number')

plt.show()
