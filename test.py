import cgi

form = cgi.FieldStorage()
user = form.getvalue("user", "Guest")

print("Content-Type:text/html\n")
print(f"<h1>Welcome {user}</h1>")