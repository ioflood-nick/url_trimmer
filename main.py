
def url_cleaner(url):
    strip_list = ["[", "]", "(", ")"]
    clean_url = "".join(url.split())
    for char in strip_list:
        clean_url = clean_url.replace(char, "")
    clean_url = clean_url.replace("hxxp", "http")
    return clean_url

if __name__ == "__main__":
    url = input("Enter a URL: ")
    print(url_cleaner(url))

