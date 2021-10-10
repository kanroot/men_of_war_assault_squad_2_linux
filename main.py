import zipfile as zi
import os

# Edit line number seven
# EXAMPLE OF PATH
# /media/2A/SteamLibrary/steamapps/common/Men of War Assault Squad 2/

path = "EDIT THIS LINE"


def ExtractPAK():
    global path
    path_zip = path + "resource/map.pak"
    if os.path.exists(path_zip):
        with zi.ZipFile(path_zip, 'r') as zip_ref:
            zip_ref.extractall(path + "resource")
        folders = FoldersMissions()
        missions = MissionFactions(folders)
        ReadFileZero(missions)
        DeletePAK(path_zip)
    else:
        print("PATH DO NOT EXISTS")


def DeletePAK(path_zip: str):
    if os.path.exists(path_zip):
        os.remove(path_zip)


def FoldersMissions():
    path_folder_factions = path + "resource/map/single/"
    dirs = os.listdir(path_folder_factions)
    directories = []
    for directory in dirs:
        n = directory
        directory = path_folder_factions + directory + "/"
        if os.path.isdir(directory):
            directories.append(n)
    directories.sort()
    path_missions = []
    for m in directories:
        path_missions.append(path_folder_factions + m + "/")
    return path_missions


def MissionFactions(folder: []):
    missions = []
    for faction in folder:
        dirs = os.listdir(faction)
        for mission in dirs:
            if os.path.isdir(faction + mission + "/"):
                missions.append(faction + mission + "/")
    return missions


def ReadFileZero(mission: []):
    for zero in mission:
        zero_path = zero + "0.mi"
        with open(zero_path, "r") as f:
            lines = f.readlines()
        with open(zero_path, "w") as f:
            for line in lines:
                if line.__contains__('{"autosave"}') is False:
                    f.write(line)


def Message():
    print("it's done! by kan")


if __name__ == '__main__':
    ExtractPAK()
    print("DONE!!!!")
