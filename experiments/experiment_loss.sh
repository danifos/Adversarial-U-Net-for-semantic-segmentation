loss_type=(BCE BCE BCE BCE L1 L1 L1 L1)
lambda_GAN=(0 1 1 1 0 1 1 1)
gan_mode=(lsgan vanilla lsgan wgangp lsgan vanilla lsgan wgangp)

for i in {0..7}
do
    dir_name=ISBI2012_test$i
    python train.py --dataroot ../paired_dataset/ --name $dir_name --loss_type ${loss_type[$i]} --lambda_GAN ${lambda_GAN[$i]} --gan_mode ${gan_mode[$i]} --lr 0.0005 --n_epochs 400 --n_epochs_decay 200 --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
    python test.py --dataroot ../paired_dataset/ --name $dir_name --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
    rm -r checkpoints/$dir_name
done

bash eval_all.sh >> experiment_loss.log
