import glob
from zipfile import ZipFile

def find_executable():
  start = "/home"
  file_name = "(?i)ReShade_Setup(_.*)?\\.exe"
  file_directory = glob.glob("/home/ishidaw/Downloads/reshadeTesting/ReShade_Setup_6.6.2.exe", recursive=True)

  # Testing return
  # print(str(file_directory).replace("[", "").replace("]", ""))

  return str(file_directory).replace("[", "").replace("]", "")

def unzip_reshade():
  with ZipFile('/home/ishidaw/Downloads/reshadeTesting/ReShade_Setup_6.6.2.exe', 'r') as zip_object:
    zip_object.extractall("./reshade")

print(find_executable())

unzip_reshade()