import os
import shutil
from sklearn.model_selection import train_test_split

def organize_dataset(base_dir, val_ratio=0.2):
    classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
    sets = ['Train', 'Validation']

    # Creating directories
    for set_name in sets:
        for class_name in classes:
            new_dir = os.path.join(base_dir, set_name, class_name)
            os.makedirs(new_dir, exist_ok=True)

    # Splitting and moving files
    for class_name in classes:
        class_dir = os.path.join(base_dir, 'Training', class_name)
        files = [os.path.join(class_dir, f) for f in os.listdir(class_dir) if f.endswith('.jpg') or f.endswith('.png')]
        
        train_files, val_files = train_test_split(files, test_size=val_ratio, random_state=42)
        
        # Move files
        for file in train_files:
            shutil.move(file, os.path.join(base_dir, 'Train', class_name))
        for file in val_files:
            shutil.move(file, os.path.join(base_dir, 'Validation', class_name))

# Usage
base_dir = 'dataset/'  # Adjust this path
organize_dataset(base_dir)