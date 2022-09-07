import os

for im_size in [128]:
    for l_rate in [0.1]:
        for d_rate in [0.5]:
            for nb_blocks_1_path in [1,2,3,4,5,6,7,8.9,10,11,12,13,14,15,16,17,18,19,20]:
                for nb_blocks_2_path in [3]:
                    for filter_nb in [64]:
                        for filter_size in [7]:
                            for strides in [4]:
                                for pooling_size in [2]:
                                    for filter_nb_residual in [64]:
                                        for filter_size_residual in [3]:

                                            #PTH=f"/mnt/storage/ifilipiuk/tuned_ara_cnn_greedy_approach/im_size_{im_size}_lr_rate_{l_rate}_dr_rate_{d_rate}_nb_bocks_1_path_{nb_blocks_1_path}_nb_blocks_2_path_{nb_blocks_2_path}_filter_nb_{filter_nb}_filter_size_{filter_size}_strides_{strides}_pooling_size_{pooling_size}_filter_nb_residual_{filter_nb_residual}_filter_size_residual_{filter_size_residual}/"

                                            PTH=f"/home/ifilipiuk/cell_classfication/ARA-CNN_tuned_alternative/ARA-CNN/tuned_ara_cnn_greedy_approach/im_size_{im_size}_lr_rate_{l_rate}_dr_rate_{d_rate}_nb_bocks_1_path_{nb_blocks_1_path}_nb_blocks_2_path_{nb_blocks_2_path}_filter_nb_{filter_nb}_filter_size_{filter_size}_strides_{strides}_pooling_size_{pooling_size}_filter_nb_residual_{filter_nb_residual}_filter_size_residual_{filter_size_residual}/"


                                            os.system(f"mkdir {PTH}")


                                            os.system(f"CUDA_VISIBLE_DEVICES=1 python src/ara_cnn_tuned.py --output-path {PTH} --dataset-path /mnt/storage/ifilipiuk/masters_thesis/ara_cnn_data/lung_input_data/ --epochs 50 --image_size {im_size} --learning_rate {l_rate} --dropout_rate {d_rate} --nb_of_residual_blocks_in_first_path {nb_blocks_1_path} --nb_of_residual_blocks_in_second_path {nb_blocks_2_path} --filter_nb {filter_nb} --filter_size {filter_size} --strides {strides} --pooling_size {pooling_size} --filter_nb_residual {filter_nb_residual} --filter_size_residual {filter_size_residual} > tuned_logs/im_size_{im_size}_lr_rate_{l_rate}_dr_rate_{d_rate}_nb_bocks_1_path_{nb_blocks_1_path}_nb_blocks_2_path_{nb_blocks_2_path}_filter_nb_{filter_nb}_filter_size_{filter_size}_strides_{strides}_pooling_size_{pooling_size}_filter_nb_residual_{filter_nb_residual}_filter_size_residual_{filter_size_residual}_log.txt")
