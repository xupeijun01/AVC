# 基于亲和向量一致性的弱监督语义分割
## 单阶段流程（Single-Stage Process）
步骤1：

步骤2：
## 多阶段流程（Multi-Stage Process）
步骤1：

步骤2：

步骤3：
训练全监督语义分割模型DeeplabV1-ResNet38
```
python train_deeplab.py
```
测试评估模型
```
python test_deeplab.py
```
| Model        | Backbone   | Google Drive | Dataset Type | *Test* |   *Val*   |
|:--------------:|:------------:|:--------------:|:--------------:|:-------:|:---------:|
| Deeplab-V1 | ResNet-38 |[Weights](https://drive.google.com/drive/folders/1b3xzJM6TanoVfff-yIDvfoDe5MfXxKpE)| Pascal VOC 2012 | [75.1](http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html) | [74.6](http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html) |
