import datetime

# date time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# create new file
version_file_path = 'version.md'

# write into new file "version.md"
with open(version_file_path, 'w') as file:
    file.write(f"Version created on {current_time}\n")
