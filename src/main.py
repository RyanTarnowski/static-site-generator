from htmlhelpers import generate_page

def main():
    #NOTE:Paths here need to be relative the the main.sh file which lives up one level from src
    generate_page("content/index.md", "template.html", "public/")




if __name__ == "__main__":
    main()

