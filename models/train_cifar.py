import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision import models
import os

# -------------------------------
# 1. DEVICE
# -------------------------------
device = torch.device("cpu")

# -------------------------------
# 2. DATA TRANSFORMS
# -------------------------------
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

# -------------------------------
# 3. LOAD DATA
# -------------------------------
trainset = torchvision.datasets.CIFAR10(
    root='./dataset', train=True, download=True, transform=transform_train)

trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=16, shuffle=True, num_workers=0)

testset = torchvision.datasets.CIFAR10(
    root='./dataset', train=False, download=True, transform=transform_test)

testloader = torch.utils.data.DataLoader(
    testset, batch_size=16, shuffle=False, num_workers=0)

# -------------------------------
# 4. MODEL
# -------------------------------
model = models.resnet18(weights=None)

# Make it CIFAR-friendly
model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
model.maxpool = nn.Identity()

model.fc = nn.Linear(model.fc.in_features, 10)
model = model.to(device)

# -------------------------------
# 5. LOSS + OPTIMIZER
# -------------------------------
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# -------------------------------
# 6. TRAINING (WITH LIVE PRINT)
# -------------------------------
epochs = 10

for epoch in range(epochs):
    model.train()
    running_loss = 0.0

    for i, (inputs, labels) in enumerate(trainloader):
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # 🔥 LIVE PROGRESS
        if i % 200 == 0:
            print(f"Epoch {epoch+1}/{epochs}, Batch {i}, Loss: {loss.item():.4f}", flush=True)

    print(f"✅ Epoch {epoch+1} Completed, Total Loss: {running_loss:.4f}", flush=True)

# -------------------------------
# 7. TEST ACCURACY
# -------------------------------
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for inputs, labels in testloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f"\n🎯 Final Test Accuracy: {accuracy:.2f}%", flush=True)

# -------------------------------
# 8. SAVE MODEL
# -------------------------------
os.makedirs("models/saved", exist_ok=True)
torch.save(model.state_dict(), "models/saved/cifar_model.pth")

print("💾 Model saved successfully!", flush=True)