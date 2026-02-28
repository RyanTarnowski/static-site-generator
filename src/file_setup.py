import os
import shutil
from htmlhelpers import generate_page
# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    # It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    # It should copy all files and subdirectories, nested files, etc.
    # I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
def setup_public(publicpath, staticpath):
    if os.path.isdir(publicpath):
        shutil.rmtree(publicpath)

    os.mkdir(publicpath)
    
    if os.path.isdir(staticpath): 
        for item in os.listdir(staticpath):
            copy_tree(item, staticpath, publicpath)

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

def generate_content(publicpath, contentpath, staticpath, basepath):
    print("Setting up public folder")
    setup_public(publicpath, staticpath)
    
    if os.path.isdir(contentpath):
        for item in os.listdir(contentpath):
            generate_page_tree(item, contentpath, publicpath, basepath)

def generate_page_tree(name, src, dst, basepath):
    src_path = os.path.join(src, name)
    dst_path = os.path.join(dst, name)
    if os.path.isfile(src_path):
        generate_page(src_path, "template.html", dst, basepath)
        return

    os.makedirs(dst_path, exist_ok=True)
    print(f"mkdir: {dst_path}") 
    for item in os.listdir(src_path):
        generate_page_tree(item, src_path, dst_path, basepath)
