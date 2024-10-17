# DEFINE FUNCTION "extensions"
def extensions(ext):

    # MATCH FILE EXTENSIONS
    match ext:
        case "gif" | "jpg" | "jpeg" | "png" | "pdf" | "txt" | "zip":
            return True

        case _:
            return False


# DEFINE FUNCTION "main"
def main():
    # INPUT FILE NAME FROM USER AND SAVE IT TO "f_name" VARIABLE
    # REMOVE ANY LEADING WHITESPACE AND CONVERT TO LOWERCASE
    # SPLIT EXTENSION FROM FILE NAME
    f_name = input("File name: ").strip().lower().split(".")[-1]

    # CHECK WHETHER extensions() RETURN True or False
    # DISPAY FILE EXTENSION TO USER
    if extensions(f_name):
        match f_name:
            case "jpg":
                print("image/jpeg")
            case "gif" | "jpeg" | "png":
                print("image/"+f_name)
            case "txt":
                print("text/plain")
            case _:
                print("application/"+f_name)

    else:
        print("application/octet-stream")


# FUNCTION CALL
main()
