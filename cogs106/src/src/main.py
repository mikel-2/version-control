from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md in the docs folder
with open("../docs/version.md", "w") as version_file:
    version_file.write(f"Last updated: {current_datetime}\n")

print("version.md has been updated with the current date and time.")
