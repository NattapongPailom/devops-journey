web_files = ["index.html", "style.css", "script.js"]

print("Starting system check")

for web_file in web_files:
  if web_file.endswith(".html"):
    print(f"High Priority, Processing: {web_file}")        
  elif web_file != ".html":
    print(f"Processing: {web_file}")

print("finish")     
