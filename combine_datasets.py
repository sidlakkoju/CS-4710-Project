import os
import shutil

def combine_datasets(source_dir1, source_dir2, target_dir):
    # Create target directory structure if it doesn't exist
    for category in ['Training', 'Testing']:
        for tumor_type in ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']:
            os.makedirs(os.path.join(target_dir, category, tumor_type), exist_ok=True)
    
    # Function to copy files from a source to a target directory
    def copy_files(source, target):
        for file in os.listdir(source):
            src_file = os.path.join(source, file)
            if os.path.isfile(src_file):
                # Construct target file path
                target_file = os.path.join(target, file)
                # Check if file already exists at target
                if os.path.exists(target_file):
                    # Generate a new file name to prevent overwriting
                    base, extension = os.path.splitext(file)
                    counter = 1
                    new_file = f"{base}_{counter}{extension}"
                    target_file = os.path.join(target, new_file)
                    # Ensure the new file name is also unique
                    while os.path.exists(target_file):
                        counter += 1
                        new_file = f"{base}_{counter}{extension}"
                        target_file = os.path.join(target, new_file)
                # Copy file to target directory
                shutil.copy(src_file, target_file)

    # Iterate over each category and tumor type and copy files
    for category in ['Training', 'Testing']:
        for tumor_type in ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']:
            src1 = os.path.join(source_dir1, category, tumor_type)
            src2 = os.path.join(source_dir2, category, tumor_type)
            tgt = os.path.join(target_dir, category, tumor_type)
            if os.path.exists(src1):
                copy_files(src1, tgt)
            if os.path.exists(src2):
                copy_files(src2, tgt)

# Example usage
combine_datasets('dataset_1', 'dataset_2', 'combined_dataset')
