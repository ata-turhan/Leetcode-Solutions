class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Initialize a list to store the main folders and a set to track seen folders
        main_folders = []
        seen_folders = set()

        # Sort the folder list to ensure subfolders appear after their parent folders
        folder.sort()

        # Iterate over each folder in the sorted list
        for f in folder:
            sub_folders = f[1:].split("/")  # Remove leading '/' and split into subfolders
            full_name = ""  # To build the folder path incrementally
            
            # Check each subfolder to see if it's already in seen_folders
            for sub_name in sub_folders:
                full_name += "/" + sub_name
                if full_name in seen_folders:
                    break  # If a parent folder is found, stop processing this folder
            
            # If the entire folder path is not a subfolder of any previously seen folder
            if full_name in seen_folders:
                continue  # Skip if already part of seen folders
            else:
                seen_folders.add(full_name)  # Add the current folder to seen
                main_folders.append(f)  # Add the folder to the main list

        return main_folders
