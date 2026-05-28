text = "   hello world  "
print(text.strip())

print(text.lstrip())
print(text.rstrip())


url= "https://www.codenaddepug.com/"
clean_url = url.strip("https:/")

print(clean_url)