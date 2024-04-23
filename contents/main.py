import re


# Đọc nội dung của tệp HTML
with open('input.html', 'r', encoding='utf-8') as file_read:
    html_contents = file_read.readlines()

# print(f"🚀 {html_contents}")


for i in range(len(html_contents)):
    modified_line = re.sub(r'<H3 .*?>', '<H3>', html_contents[i])
    html_contents[i] = modified_line


for i in range(len(html_contents)):
    if re.search(re.compile(r'<A .*?>'), html_contents[i]):
        # print("Dòng hiện tại chứa '<A .*?>'")
        # print(f"🚀 {html_contents[i]}")
        links = re.compile(r'<A HREF="(.*?)".*?>(.*?)</A>').findall(html_contents[i])

        url = links[0][0]
        text = links[0][1]

        # print(f"🚀 {url}")
        # print(f"🚀 {text}")

        # Xóa ?fbclid của thẻ <a>
        if "?fbclid" in url:
            url = url.split("?fbclid")[0]

        # Xóa dấu / của thẻ <a>
        if url.endswith("/"):
            url = url[:-1]

        # print(f"🚀 {url}")

        modified_line = "<DT><A HREF=\""+url+"\">"+text+"</A>"+"\n"
        html_contents[i] = modified_line


with open('output.html', 'w', encoding='utf-8') as file:
    for i in html_contents:
        file.write(i)
