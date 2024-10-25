class Solution:
    def removeSubfolders(self, folder_paths: List[str]) -> List[str]:
        main_folders = []
        folder_tracker = set()

        # Sort folder paths to ensure subfolders appear after their parent folders
        folder_paths.sort()

        # Iterate over each folder in the sorted list
        for folder_path in folder_paths:
            subfolder_parts = folder_path[1:].split("/")  # Remove leading '/' and split into subfolder parts
            accumulated_path = ""  # To build the folder path incrementally
            
            # Check if the current folder is a subfolder of any previously tracked folder
            for part in subfolder_parts:
                accumulated_path += "/" + part
                if accumulated_path in folder_tracker:
                    break  # If a parent folder is found, stop processing this folder
            
            # If the entire folder path is not a subfolder of any previously tracked folder
            if accumulated_path in folder_tracker:
                continue  # Skip if already part of folder_tracker
            else:
                folder_tracker.add(accumulated_path)  # Add the current folder to the tracker
                main_folders.append(folder_path)  # Add the folder to the main folder list

        return main_folders
