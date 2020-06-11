for dir in results/*
do
    echo $dir
    python eval_acc.py -i $dir/test_latest/images/*_fake_B.png -l ../dataset/new_test_set/test_label/*
done
