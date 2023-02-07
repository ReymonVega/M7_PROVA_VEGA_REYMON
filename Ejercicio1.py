import pandas as pd
import matplotlib.pyplot as plt

def plot_notes_by_student(csv_file):
    df = pd.read_csv(csv_file)
    df.dropna(inplace=True) # Remove NULL values
    student_notes = df.groupby(['NAME', 'SURNAME']).mean()['NOTES']
    student_notes.plot(kind='bar')
    plt.title(f"{student_notes.index[0][0]} {student_notes.index[0][1]}")
    plt.xlabel('Nombre y Apellido del Alumno')
    plt.ylabel('Nota Media')
    plt.show()

if __name__ == '__main__':
    plot_notes_by_student('Listado.csv')