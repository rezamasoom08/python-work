import os
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file), arcnames=os.path.join(rel_path, file))

zip_all('my_stuff', ['.jpg', '.tyxt'], 'my_stuff.zip')