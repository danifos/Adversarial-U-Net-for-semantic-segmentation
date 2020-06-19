for dir in *U-net*
do
    echo $dir
    python ../scripts/eval_acc.py -i $dir/eval/class_1_image_*.tif -l ../dataset/new_test_set/test_label/*
done
