def main():

    # ### Module 4 Assignment 1

    # from urllib.request import urlopen
    # from bs4 import BeautifulSoup
    # import ssl

    # # Ignore SSL certificate errors
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE

    # url = input("Enter - ")
    # html = urlopen(url,context=ctx).read()
    # soup = BeautifulSoup(html,"html.parser")

    # # Retrieve all the anchor tags
    # tags = soup("span")

    # counter = 0

    # for tag in tags:
    #     if counter == 0:
    #         counter = int(tag.contents[0])
    #     else:
    #         counter = counter + int(tag.contents[0])
    # print(counter)


    ### Module 4 Assignment 2
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl
    import re

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    url = input("Enter url:")
    count = 0

    while count < 7:
        html = urlopen(url, context=context).read()
        parser = BeautifulSoup(html, "html.parser")

        findAnchorTag = parser("a")[17].get("href",None)

        findName = re.findall(r"\.*?by_(.*?)\.",findAnchorTag)
        url = "http://py4e-data.dr-chuck.net/known_by_" + findName[0]+".html"
        print(findName)
        print(count)
        count = count + 1

if __name__ == "__main__":
    main()
