import glob
import csv

import numpy as np


def global2local(global_origin, global_coordinates):
    """Converts a point in a global coordinate system to a local coordinate 
    system.  

    Args:
        global_origin (array): The origin of the global coordinate 
        system.
        
        global_coordinates (array): The global coordinates to be 
        converted to local coordinates.

    Returns:
        local_coordinates (array):  The local coordinates corresponding to the 
        input global coordinates.
    """
    # Define the global and local coordinate system
    global_origin = np.array([global_origin])
    global_x_axis = np.array([1, 0, 0])
    global_y_axis = np.array([0, 1, 0])
    global_z_axis = np.array([0, 0, 1])

    # Define the local coordinate system. Based on IVION standard.
    local_origin = np.array([0, 0, 0])
    local_x_axis = np.array([1, 0, 0])
    local_y_axis = np.array([0, 1, 0])
    local_z_axis = np.array([0, 0, 1])

    # Define the transformation matrix
    T = np.column_stack((local_x_axis, local_y_axis, local_z_axis))

    # Convert the global coordinates to the local coordinate system
    global_coordinates = np.array(global_coordinates)
    local_coordinates = T @ (global_coordinates - global_origin) + local_origin

    return local_coordinates

 
def merger_txt(input_folder, output_filename = "output_file.txt"):
    """Merges all text files in the input folder

    Args:
        input_folder (str): The path to the input folder containing the text 
        files to be merged.
        output_filename (str, optional): The desired name of the output text 
        file. Defaults to "output_file.txt".
    """
    
    filenames = glob.glob(input_folder + '*.txt')
    combined_text = ""

    # Adds all text into the combined_text string
    for filename in filenames:
        with open(filename, 'r') as file:
            file_text = file.read()
            combined_text += file_text

    # Write the file
    with open(output_filename, 'w') as file:
        file.write(combined_text)


def merger_csv(input_folder, output_filename = "output_file.csv", delimiter = ","):
    """Merges all CSV files in the input folder

    Args:
        input_folder (str): The path to the input folder containing the CSV 
        files to be merged.
        output_filename (str, optional): The desired name of the output CSV 
        file. Defaults to "output_file.csv".
        delimiter (str, optional): The delimiter used in the CSV files. 
        Defaults to ",".
    """

    filenames = glob.glob(input_folder + '*.csv')
    combined_rows = []

    # Read the file
    for filename in filenames:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            rows = list(reader)
            combined_rows += rows

    # Write to the file
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(combined_rows)


def remove_duplicate(filepath):
    """Removes rows with duplicate identifiers in a text file
    Args:
        filepath (str): The filepath of the text file
    """

    identifiers = set()
    rows = []

    with open(filepath, 'r') as file:
        for line in file:
            row = line.split('\t')
            identifier = row[0]
            if identifier not in identifiers:
                identifiers.add(identifier)
                rows.append(row)

    # Write to the file
    with open(filepath, 'w') as file:
        for row in rows:
            line = '\t'.join(row)
            file.write(line)
            
            
    
