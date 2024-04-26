# counts the number of files in the dataset and creates a figure to visualize the distribution of the classes in the dataset.

import os
import matplotlib.pyplot as plt

import os
import matplotlib.pyplot as plt

def count_and_plot_num_files(base_dir):
    classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
    sets = ['Train', 'Validation', 'Test']
    data = {set_name: [] for set_name in sets}

    # Count the number of files
    for set_name in sets:
        counts = []
        for class_name in classes:
            class_dir = os.path.join(base_dir, set_name, class_name)
            num_files = len([f for f in os.listdir(class_dir) if f.endswith('.jpg') or f.endswith('.png')])
            counts.append(num_files)
            print(f'{set_name} set: {class_name}: {num_files} files')
        data[set_name] = counts

    # Plot the results
    fig, ax = plt.subplots(1, 3, figsize=(18, 5))  # Create 3 subplots for Train, Validation, Test
    for i, set_name in enumerate(sets):
        ax[i].bar(classes, data[set_name], color=['blue', 'green', 'red', 'purple'])
        ax[i].set_title(f'{set_name} Set Distribution')
        ax[i].set_xlabel('Classes')
        ax[i].set_ylabel('Number of Images')
        ax[i].set_xticklabels(classes, rotation=45)
    plt.tight_layout()

    # Save the figure
    plt.savefig('figures/dataset_class_distribution.png', dpi=300)  # Save as PNG with high resolution
    plt.show()

if __name__ == '__main__':
    base_dir = 'dataset/'  # Adjust this path
    count_and_plot_num_files(base_dir)
