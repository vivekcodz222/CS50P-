#when the user enters the file name it should display the file extenction like .jpg, .gif, .txt etc..
x = input("What's the name of a file? ").casefold().strip()

if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg"):
    print("image/jpeg")
elif x.endswith(".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    print("text/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")


