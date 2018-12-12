import os
import shutil
import random
import os
from scripts.label_image import *

def listdir_fullpath(d):
    """
    Returns list of all files in a defined directory d 
    """
    return [os.path.join(d, f) for f in os.listdir(d)]

def test():

    loc_list = ["Kathmandu","Sankhu","Sindhupalchok District","Bhaktapur"]
    for location in loc_list:
        images = listdir_fullpath(location)
        for image in images:
            if image == '.DS_Store':
                continue 

            path = os.path.join(image)
            print(path)



if __name__== "__main__":
    test()


# import os
# import shutil
# import random
# import os
# from scripts.label_image import *

# def listdir_fullpath(d):
#     """
#     Returns list of all files in a defined directory d 
#     """
#     return [os.path.join(d, f) for f in os.listdir(d)]

# def test():
    

#     model_file = "tf_files/retrained_graph.pb"
#     label_file = "tf_files/retrained_labels.txt"

#     input_height = 224
#     input_width = 224
#     input_mean = 128
#     input_std = 128
#     input_layer = "input"
#     output_layer = "final_result"

#     input_name = "import/" + input_layer
#     output_name = "import/" + output_layer

#     graph = load_graph(model_file)
#     input_operation = graph.get_operation_by_name(input_name);
#     output_operation = graph.get_operation_by_name(output_name);


#     loc_list = ["Kathmandu","Sankhu","Sindhupalchok District","Bhaktapur"]
#     for location in loc_list:
#         images = listdir_fullpath(location)
#         for image in images:
#             if image == '.DS_Store':
#                 continue 

#             path = os.path.join(image)

#             t = read_tensor_from_image_file(path, input_height=input_height, input_width=input_width, input_mean=input_mean, input_std=input_std)

#             with tf.Session(graph=graph) as sess:
#                 start = time.time()
#                 results = sess.run(output_operation.outputs[0],
#                       {input_operation.outputs[0]: t})
#                 end=time.time()
#                 total_time += (end-start)
#                 results = np.squeeze(results)

#             top_k = results.argsort()[-5:][::-1]
#             labels = load_labels(label_file)

#             #print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
#             template = "{} (score={:0.5f})"
#             top_index = top_k[0]

#             temp_dic[labels[top_index]] += 1

#     print("Word Counts: ", temp_dic)
#     predicted_word = max(temp_dic.keys(), key=(lambda key: temp_dic[key]))
#     print("The Predicted Category Is:", predicted_word)
#     print("The Evaluation Time Was:", total_time)
#     print(' ')
#     return name_dic[predicted_word]


# if __name__== "__main__":
    test()