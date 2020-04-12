from torchsummary import summary
import torch
import torch.nn as nn
import torch.nn.functional as F
from eva4modeltrainer import ModelTrainer
from eva4models import Net

class BasicBlock(Net):
	def ResNetLayer(self,in_planes,out_planes):
		return nn.Sequential(nn.Conv2d(in_planes,out_planes,3,stride=1,padding=1,bias=False),nn.BatchNorm2d(out_planes),nn.ReLU(),nn.Conv2d(out_planes,out_planes,3,stride=1,padding=1,bias=False),nn.BatchNorm2d(out_planes),nn.ReLU())
	def ConvLayer(self,in_planes,out_planes,maxpool=True):
		l=[nn.Conv2d(in_planes,out_planes,3,stride=1,padding=1,bias=False)]
		if(maxpool):
			l.append(nn.MaxPool2d(2))
		l.append(nn.BatchNorm2d(out_planes))
		l.append(nn.ReLU())
		return nn.Sequential(*l)
	def __init__(self):
		super(BasicBlock,self).__init__()
class ResNetforS11(BasicBlock):
	def __init__(self,name="modified ResNet",device="cuda"):
		super(ResNetforS11,self).__init__()
		self.trainer=None
		self.name=name
		self.device=device
		self.layer1=self.ConvLayer(3,64,False)
		self.layer2a=self.ConvLayer(64,128)
		self.layer2b=self.ResNetLayer(128,128)
		self.layer3=self.ConvLayer(128,256)
		self.layer4a=self.ConvLayer(256,512)
		self.layer4b=self.ResNetLayer(512,512)
		self.maxpool=nn.MaxPool2d(4)
		self.fc=nn.Conv2d(512,10,1,padding=0)
	def forward(self,x):
		x=self.layer1(x)
		x1=self.layer2a(x)
		r1=self.layer2b(x1)
		x=x1+r1
		x=self.layer3(x)
		x2=self.layer4a(x)
		r2=self.layer4b(x2)
		x=x2+r2
		x=self.fc(self.maxpool(x))
		x = x.view(-1, 10)
		return F.log_softmax(x, dim=-1)
		