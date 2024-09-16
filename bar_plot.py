import numpy as np
import matplotlib as plt
from scipy.stats import ttest_rel

def barplot_annotate_brackets(num1, num2, data, center, height, yerr=None, dh=.05, barh=.05, fs=None, maxasterix=None):
    """
    Annotate barplot with p-values.

    :param num1: number of left bar to put bracket over
    :param num2: number of right bar to put bracket over
    :param data: string to write or number for generating asterixes
    :param center: centers of all bars (like plt.bar() input)
    :param height: heights of all bars (like plt.bar() input)
    :param yerr: yerrs of all bars (like plt.bar() input)
    :param dh: height offset over bar / bar + yerr in axes coordinates (0 to 1)
    :param barh: bar height in axes coordinates (0 to 1)
    :param fs: font size
    :param maxasterix: maximum number of asterixes to write (for very small p-values)
    """

    if type(data) is str:
        text = data
    else:
        # * is p < 0.05
        # ** is p < 0.005
        # *** is p < 0.0005
        # etc.
        text = ''
        p = .05

        while data < p:
            text += '*'
            p /= 10.

            if maxasterix and len(text) == maxasterix:
                break

        if len(text) == 0:
            text = 'n. s.'

    lx, ly = center[num1], height[num1]
    rx, ry = center[num2], height[num2]

    if yerr:
        ly += yerr[num1]
        ry += yerr[num2]

    ax_y0, ax_y1 = plt.gca().get_ylim()
    dh *= (ax_y1 - ax_y0)
    barh *= (ax_y1 - ax_y0)

    y = max(ly, ry) + dh

    barx = [lx, lx, rx, rx]
    bary = [y, y+barh, y+barh, y]
    mid = ((lx+rx)/2, y+barh)

    plt.plot(barx, bary, c='black')

    kwargs = dict(ha='center', va='bottom')
    if fs is not None:
        kwargs['fontsize'] = fs

    plt.text(*mid, text, **kwargs)

def show_barPlot_t_test(sample_array,sample_name_list,correction='Bonferroni'):
    """
    sample_array:       array, (#samples,each sample's size)
    sample_name_list:   list, (#samples), each sample's name
    correction:         str, 'Bonferroni' for Bonferroni correction; else, no correction.

    draws a bar plot with pairwise t test and standard deviation.

    """

    n_samples = len(sample_array)
    means = []
    stds = []
    for i in range(n_samples):
        means.append(np.mean(sample_array[i,:]))
        stds.append(np.std(sample_array[i,:]))

    p_values = np.zeros((4, 4))
    if correction == 'Bonferroni':
        for i in range(4):
            for j in range(i + 1, 4):
                _, p_values[i, j] = ttest_rel(sample_array[i,:], sample_array[j,:])
                p_values[i, j] *= n_samples*(n_samples-1)/2
    else:
        for i in range(4):
            for j in range(i + 1, 4):
                _, p_values[i, j] = ttest_rel(sample_array[i,:], sample_array[j,:])

    fig, ax = plt.subplots()
    bar_positions = np.arange(n_samples)
    plt.bar(bar_positions, means, align='center')

    for i in range(4):
        for j in range(i+1,4):
            barplot_annotate_brackets(i, j, p_values[i, j], bar_positions, means, stds,0.4,0.1, maxasterix=8)

    for i in range(4):
        ax.errorbar(bar_positions[i], means[i], yerr=stds[i], fmt='o', color='purple')

    print(p_values)

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(sample_name_list)
    ax.legend()
    plt.show()

def show_barPlot_simple(means_list, std_list, sample_name_list):
    """
        means_list:         list, (#samples,)
        std_list:           list, (#samples,)
        sample_name_list:   list, (#samples,)

        draws a bar plot indicating means and standard deviations.

        """

    num_samples = len(means_list)

    fig, ax = plt.subplots()

    bar_width = 0.35
    bar_positions = range(num_samples)
    bars = ax.bar(bar_positions, means_list, bar_width)

    for i in range(num_samples):
        ax.errorbar(bar_positions[i], means_list[i], yerr=std_list[i], fmt='o', color='purple')

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(sample_name_list)
    ax.legend()
    plt.show()