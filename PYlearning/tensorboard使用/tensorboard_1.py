from torch.utils.tensorboard import SummaryWriter

write = SummaryWriter('log')  # 实例化一个对象
for epoch in range(100):
    write.add_scalar('flower', 2 * epoch, epoch)  # tap 因变量 自变量

write.close()# 用完后关上

# tensorboard --logdir=logs                #可视化
