import os,shutil
ASONAM17_Damage_Image_Dataset/ecuador_eq
ASONAM17_Damage_Image_Dataset/nepal_eq

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
    

def sort_files():
    """
    This method combines the dataset 
    """
    category_dict = {}
    categories = {'none': 0,'mild': 1,'severe': 2}
    with open('damage_intensity_data_combined') as file:
        for line in file:
            for category in categories:
                if(line.find(category)!=-1):
                    category_dict.setdefault(category,[]).append(line)
    

    for category in category_dict:
        images = category_dict[category]
        print(categories[category])
        if not os.path.exists(categories[category]):
            os.makedirs(str(categories[category]))
        for img in images:
            from_path = 'earthquake/' + img.split(' ')[0]
            first_split = (img[img.find("/")+1:]).split(' ')[0]
            to_path = str(category) + "/" + first_split[first_split.find("/")+1:]
            print("from" + from_path)
            print("to" + to_path)
            shutil.move(from_path,to_path)
            #train_input.write(to_path + img.split(' ')[1])



def image_statistics():
    category_dict = {}
    categories = {'none': 0,'mild': 1,'severe': 2}
    with open('test_earthquake') as file:
        for line in file:
            bol = False
            for category in categories:
                #print(category)
                #print(line)
                #print(line.find(category)!=-1)
                if(line.find(category)!=-1):
                    bol = True
                    category_dict.setdefault(category,[]).append(line)
                elif((not bol)):
                    continue
                else:
                    continue

    with open('train_earthquake') as file:
        for line in file:
            bol = False
            for category in categories:
                #print(category)
                #print(line)
                #print(line.find(category)!=-1)
                if(line.find(category)!=-1):
                    bol = True
                    category_dict.setdefault(category,[]).append(line)
                elif((not bol)):
                    continue
                else:
                    continue

    for key in category_dict:
        print(key)
        print(len(category_dict[key]))


    for key in category_dict:
        print(key)
        nepal = 0
        ecudador = 0
        for element in category_dict[key]:
            if element.find('nepal'):
                nepal+=1
            elif element.find('ecudador'):
                ecudador+=1
        print("Nepal", nepal)
        print("Ecudaor",ecudador)


def damage_stats():
    category_dict = {}
    categories = {'none': 0,'mild': 1,'severe': 2}
    damage = ['road','bridge','building']
    with open('train_damage_type') as file:
        for line in file:
            for category in damage:
                label = line.split(' ')[1]
                path = line.split(' ')[0]
                if(label.find("0")!=-1):
                    if os.path.exists(path):
                        os.remove(path)
                        print("remove")
                elif(line.find(category)!=-1):
                    category_dict.setdefault(category,[]).append(line)
                else:
                    continue

    for key in category_dict:
        print(key)
        print(len(category_dict[key]))



if __name__== "__main__":
    damage_stats()