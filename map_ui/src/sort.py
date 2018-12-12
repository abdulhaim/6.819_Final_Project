import os,shutil

def listdir_fullpath(d):
    """
    Returns list of all files in a defined directory d 
    """
    return [os.path.join(d, f) for f in os.listdir(d)]

def combine_text_files(filenames,filename):
    """
    Combineds the Nepal and Ecuador Earthquake text files containing image name and label into
    one concise file
    """
    base_path = "ASONAM17_Damage_Image_Dataset/"

    with open(filename, 'w') as outfile:
        for fname in filenames:
            with open(base_path + fname) as infile:
                for line in infile:
                    outfile.write(line)

def sort_files_damage_intensity():
    """
    This method combines the Nepal & Ecudaor Datasets into 3 folders 
    labelled as none, mild, and extreme damage
    """
    base_path = "ASONAM17_Damage_Image_Dataset/"

    nepal_data_path = "ASONAM17_Damage_Image_Dataset/ecuador_eq"
    ecuador_data_path = "ASONAM17_Damage_Image_Dataset/nepal_eq"

    categories = {'none': 0,'mild': 1,'severe': 2}
    category_dict = {}

    with open('damage_intensity_data_combined') as file:
        for line in file:
            for category in categories:
                if(line.find(category)!=-1):
                    category_dict.setdefault(category,[]).append(line)

    for category in category_dict:
        images = category_dict[category]
        folder = "tensorflow-for-poets-2/tf_files/earthquake_damage_intensity/" + category
        if not os.path.exists(folder):
            os.makedirs(folder)
        for img in images:
            from_path = base_path + img.split(' ')[0]
            first_split = (img[img.find("/")+1:]).split(' ')[0]
            to_path = folder + "/" + first_split[first_split.find("/")+1:]
            print("from " + from_path)
            print("to " + to_path)
            shutil.move(from_path,to_path)

# def sort_files_damage_type():
    
    # category_dict = {}
    # categories = {'none': 0,'mild': 1,'severe': 2}
    # damage = ['road','bridge','building']
    # with open('combined_disaster_type') as file:
    #     for line in file:
    #         for category in damage:
    #             label = line.split(' ')[1]
    #             path = line.split(' ')[0]
    #             if(label.find("0")!=-1):
    #                 if os.path.exists(path):
    #                     os.remove(path)
    #             elif(line.find(category)!=-1):
    #                 if(line.find("extra_none_ggIM")!=-1):
    #                 category_dict.setdefault(category,[]).append(line)
    #             else:
    #                 continue

    # for key in category_dict:
    #     print(key)
    #     print(len(category_dict[key]))

if __name__== "__main__":
    combine_text_files(['ecuador.train', 'ecuador.test', 'ecuador.dev', 'nepal.train','nepal.test','nepal.dev'],'damage_intensity_data_combined')
    sort_files_damage_intensity()

    # combine_text_files(['gg.train', 'gg.dev', 'gg.test'],"combined_disaster_type")
    # sort_files()


