
import os
import shutil
from rich import print
import stat
def remove_git():
    path = input("Enter the path of your git repository: ")
    print(path)
    for root, subFolder, files in os.walk(path):
        for folder in subFolder:
            if folder == '.git':
                os.chmod(os.path.join(root, folder), stat.S_IRWXU)
                subfolder_path = os.path.join(root)
                git_folder_path = os.path.join(root,folder)
                print(f'[cyan]folder found: {git_folder_path}')
                shutil.rmtree(git_folder_path, ignore_errors=True)
                shutil.rmtree(subfolder_path, ignore_errors=True)
                if not os.path.exists(git_folder_path):
                    print(f'[red]Removed {subfolder_path}')
    print('[green]Done[/green]')
    print('[green]Done[/green]')
    input('Press Enter to continue')




if __name__ == '__main__':
    remove_git()