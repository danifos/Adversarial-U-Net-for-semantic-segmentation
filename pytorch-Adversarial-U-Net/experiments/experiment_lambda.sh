lambda_GAN=(1 1 0.1 0.01 1 1 0.1 0.01)
lambda_L1=(1000 10000 100 100 1000 10000 100 100)
lr=(0.0005 0.0005 0.005 0.05 0.00005 0.000005 0.0005 0.0005)

for i in {0..7}
do
    dir_name=ISBI2012_exp_lambda$i
    python train.py --dataroot ../paired_dataset/ --name $dir_name --loss_type L1 --lambda_GAN ${lambda_GAN[$i]} --lambda_L1 ${lambda_L1[$i]} --gan_mode lsgan --lr ${lr[$i]} --n_epochs 400 --n_epochs_decay 200 --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
    python test.py --dataroot ../paired_dataset/ --name $dir_name --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
    rm -r checkpoints/$dir_name
done

bash eval_all.sh >> experiment_lambda.log
