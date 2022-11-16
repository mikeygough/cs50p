# get input
input = input("File name: ").strip().lower()
# split on .
file_extension = input.split(".")[-1]
# match
match file_extension:
    case "gif":
        print("image/gif", end='')
    case "jpg":
        print("image/jpeg", end='')
    case "jpeg":
        print("image/jpeg", end='')
    case "png":
        print("image/png", end='')
    case "pdf":
        print("application/pdf", end='')
    case "txt":
        print("text/plain", end='')
    case "zip":
        print("application/zip", end='')
    case _:
        print("application/octet-stream", end='')
