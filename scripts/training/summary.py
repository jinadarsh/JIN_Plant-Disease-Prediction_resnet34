import torch
from torchsummary import summary
from model import Plant_Disease_Model

# Create an instance of your model
model = Plant_Disease_Model()

# Specify the input size (channels, height, width)
input_size = (3, 128, 128)

# Move the model to the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Print the summary of the model
summary(model, input_size=input_size, device=device.type)
