import os

count = 0

for im_size in [128]:
    for l_rate in [0.1]:
        for d_rate in [0.1,0.5]:
            for nb_blocks_1_path in [8,12]:
                for nb_blocks_2_path in [8,12]:
                    for filter_nb in [64]:
                        for filter_size in [8,12]:
                            for strides in [4]:
                                for pooling_size in [2]:
                                    for filter_nb_residual in [64]:
                                        for filter_size_residual in [8,12]:
                                            if os.path.exists("src/ara_cnn_architecture_config.py"):
                                                os.remove("src/ara_cnn_architecture_config.py")

                                            f = open("src/ara_cnn_architecture_config.py", "w")
                                            f.write("IM_SIZE = {}\n".format((im_size,im_size)))
                                            f.write("\n")
                                            f.write("L_RATE = {}\n".format(l_rate))
                                            f.write("\n")
                                            f.write("D_RATE = {}\n".format(d_rate))
                                            f.write("\n")
                                            f.write("NB_BLOCKS_1_PATH = {}\n".format(nb_blocks_1_path))
                                            f.write("\n")
                                            f.write("NB_BLOCKS_2_PATH = {}\n".format(nb_blocks_2_path))
                                            f.write("\n")
                                            f.write("FILTER_NB = {}\n".format(filter_nb))
                                            f.write("\n")
                                            f.write("FILTER_SIZE = {}\n".format((filter_size,filter_size)))
                                            f.write("\n")
                                            f.write("STRIDES = {}\n".format((strides,strides)))
                                            f.write("\n")
                                            f.write("POOLING_SIZE = {}\n".format((pooling_size,pooling_size)))
                                            f.write("\n")
                                            f.write("FILTER_NB_RESIDUAL = {}\n".format(filter_nb_residual))
                                            f.write("\n")
                                            f.write("FILTER_SIZE_RESIDUAL = {}\n".format((filter_size_residual,filter_size_residual)))
                                            f.write("\n")
                                            f.close()

                                            PTH=f"/mnt/storage/ifilipiuk/tuned_ara_cnn/im_size_{im_size}_lr_rate_{l_rate}_dr_rate_{d_rate}_nb_bocks_1_path_{nb_blocks_1_path}_nb_blocks_2_path_{nb_blocks_2_path}_filter_nb_{filter_nb}_filter_size_{filter_size}_strides_{strides}_pooling_size_{pooling_size}_filter_nb_residual_{filter_nb_residual}_filter_size_residual_{filter_size_residual}/"


                                            MDL_PTH = PTH + "ara_cnn.h5"

                                            for tissue in ["BRONCHI", "IMMUNE_CELLS", "LUNG_TISSUE", "MIXED_STROMA", "NECROSIS", "STROMA", "TUMOR", "VESSEL_WALL"]:
                                                TISSUE_PTH = "/mnt/storage/ifilipiuk/masters_thesis/ara_cnn_data/lung_input_data/test/" + tissue + "/"
                                                OUT_PTH = PTH + tissue + "/"

                                                if not os.path.exists(OUT_PTH):

                                                    os.system(f"mkdir {OUT_PTH}")

                                                os.system(f"CUDA_VISIBLE_DEVICES=0 python src/test_model.py --input-images {TISSUE_PTH} --model-path {MDL_PTH} --output-path {OUT_PTH} --measure Entropy")

                                            count += 1    

                                            print("##################################################################")
                                            print("##################################################################")
                                            print("##################################################################")
                                            print()
                                            print()
                                            print(count)
                                            print()
                                            print()
                                            print("##################################################################")
                                            print("##################################################################")
                                            print("##################################################################")
