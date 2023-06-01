
import zipfile
# create function to zip files
def create_zip(files_path,zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for files in files_path:
            zipf.write(files + "\n") 
            # files_lis.append(files)


files_lis=[]
while True:

  files_to_zip= input("Enter the file to zip or press Enter to stop ")
  if files_to_zip == '':
      break
  files_lis.append(files_to_zip)

zip_file_name= input("Enter the  name of zip you want")
# calling function
create_zip(files_to_zip,zip_file_name)
