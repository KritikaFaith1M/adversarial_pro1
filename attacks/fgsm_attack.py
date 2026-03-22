import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torchvision import models
from torchvision.utils import save_image
import os
import json
import hashlib
import time

# -------------------------------
# 1. SETUP
# -------------------------------
device = torch.device("cpu")  # Use CPU
epsilon = 0.1  # Attack strength
batch_size = 1  # One image at a time for attack
num_images = 50  # Number of test images to attack (change as needed)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# -------------------------------
# 2. LOAD MODEL
# -------------------------------
model = models.resnet18(weights=None)
model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
model.maxpool = nn.Identity()
model.fc = nn.Linear(model.fc.in_features, 10)

model_path = "models/saved/cifar_model.pth"
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path, map_location=device))
    print("✅ Model loaded successfully!")
else:
    print("❌ Model not found. Train the model first.")
    exit()

model = model.to(device)
model.eval()

# -------------------------------
# 3. LOAD CIFAR-10 TEST DATA
# -------------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

testset = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=True)

# -------------------------------
# 4. CREATE FOLDERS
# -------------------------------
os.makedirs("attacks/saved_images", exist_ok=True)
os.makedirs("audit_logs", exist_ok=True)

# -------------------------------
# 5. FGSM ATTACK FUNCTION
# -------------------------------
def fgsm_attack(image, epsilon, data_grad):
    return torch.clamp(image + epsilon * data_grad.sign(), -1, 1)

# -------------------------------
# 6. LOOP THROUGH TEST IMAGES
# -------------------------------
count = 0
for image, label in testloader:
    if count >= num_images:
        break

    image, label = image.to(device), label.to(device)
    image.requires_grad = True

    # 6a. Original Prediction
    output = model(image)
    _, pre_pred = torch.max(output, 1)

    # Skip if model already wrong
    if pre_pred.item() != label.item():
        print(f"⚠️ Skipping image {count+1}: model already wrong ({classes[pre_pred.item()]})")
        count += 1
        continue

    # 6b. FGSM Attack
    loss = F.cross_entropy(output, label)
    model.zero_grad()
    loss.backward()
    data_grad = image.grad.data
    perturbed_image = fgsm_attack(image, epsilon, data_grad)

    # 6c. Prediction after attack
    output_adv = model(perturbed_image)
    _, post_pred = torch.max(output_adv, 1)

    # 6d. Save images
    save_image(image, f"attacks/saved_images/original_{count+1}.png")
    save_image(perturbed_image, f"attacks/saved_images/adv_{count+1}_eps{epsilon}.png")

    # 6e. Create audit log
    audit_log = {
        "timestamp": time.ctime(),
        "image_index": count+1,
        "model_type": "ResNet18",
        "dataset": "CIFAR-10",
        "attack_method": "FGSM",
        "epsilon": epsilon,
        "original_label": classes[pre_pred.item()],
        "adversarial_label": classes[post_pred.item()],
        "status": "SUCCESS" if pre_pred.item() != post_pred.item() else "FAILED"
    }

    # Create hash
    log_string = json.dumps(audit_log, sort_keys=True).encode()
    content_hash = hashlib.sha256(log_string).hexdigest()
    audit_log["content_hash"] = content_hash

    log_filename = f"audit_logs/attack_log_{count+1}_{int(time.time())}.json"
    with open(log_filename, "w") as f:
        json.dump(audit_log, f, indent=4)

    print(f"✅ Image {count+1} attacked | Original: {classes[pre_pred.item()]} | After Attack: {classes[post_pred.item()]} | Log: {log_filename}")

    count += 1

print(f"\n🏁 FGSM attack completed for {count} images!")