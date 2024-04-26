# count the number of files in each of the splits
import os

def count_num_files(base_dir):
    classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
    sets = ['Train', 'Validation', 'Test']

    for set_name in sets:
        print(f'\n{set_name} set:')
        for class_name in classes:
            class_dir = os.path.join(base_dir, set_name, class_name)
            num_files = len([f for f in os.listdir(class_dir) if f.endswith('.jpg') or f.endswith('.png')])
            print(f'{class_name}: {num_files} files')


if  __name__ == '__main__':
    base_dir = 'dataset/'  # Adjust this path
    count_num_files(base_dir)