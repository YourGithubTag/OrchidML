import torch
import torch.nn as nn

class AlexNet(nn.Module):

   def __init__(self):
      super(AlexNet, self).__init__()
      self.features = nn.Sequential(
         nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
         nn.ReLU(inplace=True),
         nn.MaxPool2d(kernel_size=3, stride=2),
         nn.Conv2d(64, 192, kernel_size=5, padding=2),
         nn.ReLU(inplace=True),
         nn.MaxPool2d(kernel_size=3, stride=2),
         nn.Conv2d(192, 384, kernel_size=3, padding=1),
         nn.ReLU(inplace=True),
         nn.Conv2d(384, 256, kernel_size=3, padding=1),
         nn.ReLU(inplace=True),
         nn.Conv2d(256, 256, kernel_size=3, padding=1),
         nn.ReLU(inplace=True),
         nn.MaxPool2d(kernel_size=3, stride=2),
      )
      
      self.classifier = nn.Sequential(
         nn.Dropout(),
         nn.Linear(256 * 6 * 6, 4096),
         nn.ReLU(),
         nn.Dropout(),
         nn.Linear(4096, 4096),
         nn.ReLU(),
         nn.Linear(4096, 17)
      )

   # Since this NN is inheriting the nn.Module, it will have forward() and backward() methods.
   # Backward has been implemented in nn.Module (computes gradient descents).
   
   # In this case, forward() link all the layers together.
   def forward(self, x):
      x = self.features(x)
      x = torch.flatten(x, 1)
      x = self.classifier(x)
      return x