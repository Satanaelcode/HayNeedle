import os

def setup():
    if os.path.exists("./files.json"):
        print("File exists")
    else:
        print("File does not exist")
        create_def_files = input("[Y/n] Sould create with Default values?\n» ")
        if create_def_files == "Y":
            with open("files.json", "w") as f:
                f.write("""{
  "files": [
    "upload.php",
    "shell.php"
  ]
}
                """)
            print("File created!")
            print("FINISHED")
            return
        else:
            print("FINISHED")
            return
