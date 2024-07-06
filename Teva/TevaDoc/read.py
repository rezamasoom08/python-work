import os

def create_folder_structure(base_dir, path):
    try:
        #print(base_dir)
        # Create the base directory if it doesn't exist
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        # Iterate over folder names and create folders
        #for folder_name in path:
        folder_path = os.path.join(base_dir, path)
        #print(folder_name)
        print(folder_path)
        #os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{path}' created successfully at '{base_dir}'")

    except OSError as error:
        print(f"Failed to create folder structure: {error}")

with open('folder_list.txt') as f:
    base_dir = "C:/Users/Mreza/Documents/Matthew/Tevadoc"
    lines = f.readlines()
    for line in lines:
        path = line.strip()
        print(path)
        query = f"select r_object_id, object_name from dm_document where folder('{path}', descend)"
        print(query)
        modify = path[1:]
        modify += "/"
        print(modify)
        create_folder_structure(base_dir, modify)
        #exec_query(JObject(query),session)