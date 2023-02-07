import pandas as pd
import matplotlib.pyplot as plt


def plot_graph(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()  # drop NULL values

    daw2_group = df[df["GROUP"] == "DAW2"]  # filter DAW2 group
    module_m07 = daw2_group[daw2_group["MODULE"] == "M07"]  # filter module M07

    plt.plot(module_m07["ID"], module_m07["NOTES"])
    plt.xlabel("Student ID")
    plt.ylabel("Notes")
    plt.title(f"{module_m07['NAME'].iloc[0]} {module_m07['SURNAME'].iloc[0]}")
    plt.show()


if __name__ == "__main__":
    plot_graph("Listado.csv")