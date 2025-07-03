import yaml
import numpy as np
import matplotlib.pyplot as plt

CONFIG =  yaml.load(open('config_global.yaml', 'r'), Loader=yaml.SafeLoader)

input = CONFIG['build']['prepare_data']
build = CONFIG['build']['descriptive']

def main():
    data  = np.genfromtxt(f'{input}data.txt', skip_header = 1)

    with open(f'{build}table.txt', 'w') as f:
        f.write('<tab:table>\n')
        mean, std, max_val, min_val = \
            np.mean(data), np.std(data, ddof=1), np.max(data), np.min(data)
        f.write(f'{mean}\n{std:.3f}\n{max_val:.0f}\n{min_val:.0f}')

    plt.hist(data)
    plt.savefig(f'{build}plot.pdf')

main()
