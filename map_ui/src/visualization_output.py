import os
import shutil
import random
import os
from src.tf_scripts.scripts.label_image import *

def output(file_name):
    temp_dic = {"mild": 0, "severe": 0, "none": 0}
    count = {"mild": 0, "severe": 0, "none": 0}

    model_file = "src/tf_scripts/tf_files/retrained_graph.pb"
    label_file = "src/tf_scripts/tf_files/retrained_labels.txt"

    input_height = 299
    input_width = 299
    input_mean = 128
    input_std = 128
    input_layer = "Mul"
    output_layer = "final_result"

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer

    graph = load_graph(model_file)
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);


    total_time = 0

    t = read_tensor_from_image_file(file_name,
                                  input_height=input_height,
                                  input_width=input_width,
                                  input_mean=input_mean,
                                  input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);

    with tf.Session(graph=graph) as sess:
        start = time.time()
        results = sess.run(output_operation.outputs[0],
                      {input_operation.outputs[0]: t})
    
        end = time.time()
        total_time += (end-start)
    
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)

    #print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
    template = "{} (score={:0.5f})"
    top_index = top_k[0]

    temp_dic[labels[top_index]] += 1
    predicted_word = max(temp_dic.keys(), key=(lambda key: temp_dic[key]))
    print("The Predicted Word Is:", predicted_word)
    print("The Evaluation Time Was:", total_time)
    return predicted_word
