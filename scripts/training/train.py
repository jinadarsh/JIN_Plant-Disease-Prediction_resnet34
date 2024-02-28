# from torchvision.datasets import ImageFolder
# from  torch.utils.data import random_split,DataLoader
# from helper import DeviceDataLoader, get_default_device, to_device, fit, evaluate
# from model import Plant_Disease_Model
# import torchvision.transforms as transforms
# import torch


# transform = transforms.Compose([transforms.Resize(size = 128),transforms.ToTensor()])

# dataset = ImageFolder('archive/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train',transform=transform)
# test_ds = ImageFolder('archive/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/valid',transform=transform)


# validation_split = 0.3
# val_size = int(len(dataset) * validation_split)
# train_size = len(dataset) - val_size

# train_ds,val_ds = random_split(dataset,[train_size,val_size])

# batch_size = 64
# train_loader = DataLoader(train_ds,batch_size=batch_size,num_workers=2,shuffle=True, pin_memory=True)
# val_loader = DataLoader(val_ds,batch_size=batch_size,num_workers=2,shuffle=True, pin_memory=True)
# test_loader = DataLoader(test_ds,batch_size=batch_size,num_workers=2,shuffle=True, pin_memory=True)

# device = get_default_device()
# print("DEVICE: ",device)

# # Load the training, validation and test dataloader into GPU using DeviceDataLoader function.
# train_loader = DeviceDataLoader(train_loader, device)
# val_loader = DeviceDataLoader(val_loader, device)
# test_loader = DeviceDataLoader(test_loader, device)

# # Create a model using the instantiating the Plant_Disease_Model class.
# model = to_device(Plant_Disease_Model(), device)

# # Call the fit function with its different parameters to train the model for certain number of epochs. We use optimizer “Adam” and and Learning Rate of 0.001 to train the model.

# history = fit(5, 0.001, model, train_loader, val_loader, opt_func = torch.optim.Adam)

# # Evaluate the model
# x = evaluate(model,test_loader)
# print(x)

# # Save the model
# model_name = 'plantDisease-resnet34.pth'
# torch.save(model.state_dict(), model_name)
# print("Model saved: ",model_name)

from torchvision.datasets import ImageFolder
from torch.utils.data import random_split, DataLoader
from helper import DeviceDataLoader, get_default_device, to_device, fit, evaluate
from model import Plant_Disease_Model
import torchvision.transforms as transforms
import torch

if __name__ == '__main__':
    transform = transforms.Compose([transforms.Resize(size=128), transforms.ToTensor()])

    dataset = ImageFolder('archive/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train', transform=transform)
    test_ds = ImageFolder('archive/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/valid', transform=transform)

    validation_split = 0.3
    val_size = int(len(dataset) * validation_split)
    train_size = len(dataset) - val_size

    train_ds, val_ds = random_split(dataset, [train_size, val_size])

    batch_size = 64
    train_loader = DataLoader(train_ds, batch_size=batch_size, num_workers=2, shuffle=True, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size, num_workers=2, shuffle=True, pin_memory=True)
    test_loader = DataLoader(test_ds, batch_size=batch_size, num_workers=2, shuffle=True, pin_memory=True)

    device = get_default_device()
    print("DEVICE: ", device)

    # Load the training, validation, and test dataloader into GPU using DeviceDataLoader function.
    train_loader = DeviceDataLoader(train_loader, device)
    val_loader = DeviceDataLoader(val_loader, device)
    test_loader = DeviceDataLoader(test_loader, device)

    # Create a model using the instantiating the Plant_Disease_Model class.
    model = to_device(Plant_Disease_Model(), device)

    # Call the fit function with its different parameters to train the model for a certain number of epochs.
    # We use the optimizer “Adam” and a learning rate of 0.001 to train the model.
    history = fit(5, 0.001, model, train_loader, val_loader, opt_func=torch.optim.Adam)

    # Evaluate the model
    x = evaluate(model, test_loader)
    print(x)

    # Save the model
    model_name = 'plantDisease-resnet34.pth'
    torch.save(model.state_dict(), model_name)
    print("Model saved: ", model_name)
