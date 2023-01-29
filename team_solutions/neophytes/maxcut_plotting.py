from pytket.backends.backendresult import BackendResult
import matplotlib.pyplot as plt


def plot_maxcut_results(result: BackendResult,
                        n_strings: int,
                        filename: str) -> None:
    """
    Plots Maxcut results in a barchart with the two most common bitstrings highlighted in green.
    """
    counts_dict = result.get_counts()
    sorted_shots = counts_dict.most_common()
    n_shots = sum(counts_dict.values())

    n_most_common_strings = sorted_shots[:n_strings]
    x_axis_values = [str(entry[0]) for entry in n_most_common_strings]  # basis states
    y_axis_values = [entry[1] for entry in n_most_common_strings]  # counts
    num_successful_shots = sum(y_axis_values[:2])
    success = num_successful_shots / n_shots
    success_string = f"Success ratio {success}"
    print(success_string)

    fig = plt.figure()
    # ax = fig.add_axes([0, 0, 1.5, 1])
    color_list = ["green"] * 2 + (["orange"] * (len(x_axis_values) - 2))
    plt.bar(
        x=x_axis_values,
        height=y_axis_values,
        color=color_list,
    )
    plt.title(label=f"Maxcut Results: Success ratio {success}")
    plt.ylim([0, 0.25 * n_shots])
    plt.xlabel("Basis State")
    plt.ylabel("Number of Shots")
    plt.xticks(rotation=15)
    plt.savefig(filename)
    plt.show()
