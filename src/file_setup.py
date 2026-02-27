import os
import shutil
# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    # It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    # It should copy all files and subdirectories, nested files, etc.
    # I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
def setup_public():
    public_path = "public/"
    static_path = "static/"

    if os.path.isdir(public_path):
        shutil.rmtree(public_path)

    os.mkdir(public_path)
    
    if os.path.isdir(static_path): 
        for item in os.listdir(static_path):
            copy_tree(item, static_path, public_path)

def copy_tree(name, src, dst):
    src_path = os.path.join(src, name)
    dst_path = os.path.join(dst, name)
    if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copy {src_path} to {dst_path}")
        return

    os.makedirs(dst_path, exist_ok=True)
    print(f"mkdir: {dst_path}") 
    for item in os.listdir(src_path):
        copy_tree(item, src_path, dst_path)

