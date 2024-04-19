# import torch
# import sys

# model = torch.load('logs/market1501/sbs_R101-ibn/model_final.pth', map_location=torch.device('cpu'))
# original_stdout = sys.stdout # Save a reference to the original standard output

# with open('model_test.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print(model)
#     sys.stdout = original_stdout # Reset the standard output to its original value
k = 'heads.bnneck.weight'
if k.startswith('heads.bnneck.'):
    print(k.replace('bnneck', 'bottleneck.0'))
