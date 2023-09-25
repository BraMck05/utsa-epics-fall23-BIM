import os

# Directory containing your images
image_directory = 'C:\\Users\\braym\\OneDrive\\Documents\\python'

# Get a list of all image filenames in the directory
image_files = sorted([f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))])

# Rename images sequentially
for index, old_name in enumerate(image_files):
    file_extension = os.path.splitext(old_name)[-1]
    new_name = f'brayden_{index+1:02d}{file_extension}'
    old_path = os.path.join(image_directory, old_name)
    new_path = os.path.join(image_directory, new_name)
    os.rename(old_path, new_path)
    print(f'Renamed {old_name} to {new_name}')

print('All images renamed!')

