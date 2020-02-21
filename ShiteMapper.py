from grabLinks import new_links

start = input("Front Page URL: ")
if start.endswith("/"):
    start = start[:-1]

pages_on_site = [start]
pages_scraped = set()


for each in pages_on_site:
    if each not in pages_scraped:
        if not each.startswith(start):
            scrape_link = f"{start}{each}"
        else:
            scrape_link = each
        for link in new_links(scrape_link, start):
            if not link.startswith(start):
                new_link = f"{start}{link}"
            else:
                new_link = link
            pages_on_site.append(new_link)
        pages_scraped.add(scrape_link)
        print(scrape_link)

print("*"*20)
out = open("out.txt", "w+")
for l in pages_scraped:
    print(l)
    out.write(l+"\n")
out.close()



