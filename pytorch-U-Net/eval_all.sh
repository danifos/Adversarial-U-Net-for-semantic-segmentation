for dir in Orig_U-net*
do
    echo $dir
    python ../eval_acc.py -i $dir/eval/class_1_image_*.tif -l ../dataset/new_test_set/test_label/*
done