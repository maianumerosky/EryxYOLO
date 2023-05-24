from torch import nn
from torchvision.models import resnet34, resnet18

class YOLOResNetFullyConnected(nn.Module):
    """YOLOv1-Resnet model structure
    yolo-v1 resnet = resnet(backbone) + conv + fc
    """

    def __init__(self, S, B, num_classes):
        super(YOLOResNetFullyConnected, self).__init__()
        self.S = S
        self.B = B
        self.num_classes = num_classes
        self.resnet = resnet18()
        #self.resnet = resnet34()

        #Esto estaria bueno tenerlo en un module aparte
        # backbone part, (cut resnet's last two layers)
        self.backbone = nn.Sequential(*list(self.resnet.children())[:-2])
        #We freeze the resnet for training
        for param in self.backbone.parameters():
            param.requires_grad=False

        # full connection part
        self.fc_layers = nn.Sequential(
            nn.Linear(14 * 14 * 512, 4096),
            nn.LeakyReLU(0.1, inplace=True),
            nn.Linear(4096, self.S * self.S * (self.B * 5 + self.num_classes)),
            nn.Sigmoid()  # normalized to 0~1
        )

    def forward(self, x):
        out = self.backbone(x)
        out = out.view(out.size()[0], -1)
        out = self.fc_layers(out)
        out = out.reshape(-1, self.S, self.S, self.B * 5 + self.num_classes)
        return out