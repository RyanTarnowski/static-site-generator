import sys
from file_setup import generate_content

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    generate_content("docs/", "content/", "static/", basepath)

if __name__ == "__main__":
    main()

