class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        main_folders = []
        seen_folders = set()
        folder.sort()

        for f in folder:
            sub_folders = f[1:].split("/")
            full_name = ""
            for f_name in sub_folders:
                full_name += "/" + f_name
                if full_name in seen_folders:
                    break
                    
            if full_name in seen_folders:
                    continue
            else:
                seen_folders.add(full_name)
                main_folders.append(full_name)

        return main_folders

