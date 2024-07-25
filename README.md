# 基于亲和向量一致性的弱监督语义分割
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
## 结果（Results）
### 种子（Seed）和伪标签掩码（Mask）质量

| Model        | Dataset Type | Seed | Weights | +CRF | Mask |
|:--------------:|:------------:|:--------------:|:--------------:|:-------:|:---------:|
| AVC | VOC |  | [75.8](https) | [77.5](https) | [77.8](https)|
| AVC | MS COCO |  | 45.8 | - | [48.4](https://drive.google.com/file/d/1UFEk8uN_81E0hLU50oR9FsiL6QvAon_u/view?usp=drive_link) |

<table>
  <tr>
    <th>Model</th>
    <th>Dataset Type</th>
    <th>Seed</th>
    <th>Weights</th>
    <th>+CRF</th>
    <th>Mask</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">AVC</td>
    <td>VOC</td>
    <td></td>
    <td><a href="https://example.com">75.8</a></td>
    <td><a href="https://example.com">77.5</a></td>
    <td><a href="https://example.com">77.8</a></td>
  </tr>
  <tr>
    <td>MS COCO</td>
    <td></td>
    <td>45.8</td>
    <td>-</td>
    <td><a href="https://drive.google.com/file/d/1UFEk8uN_81E0hLU50oR9FsiL6QvAon_u/view?usp=drive_link">48.4</a></td>
  </tr>
</table>



<table>
  <tr>
    <th>Model</th>
    <th>Backbone</th>
    <th>Google Drive</th>
    <th>Dataset Type</th>
    <th>*Test*</th>
    <th>*Val*</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">Deeplab-V1</td>
    <td>ResNet-38</td>
    <td><a href="https://drive.google.com/drive/folders/1b3xzJM6TanoVfff-yIDvfoDe5MfXxKpE">Weights</a></td>
    <td>Pascal VOC 2012</td>
    <td><a href="http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html">75.1</a></td>
    <td><a href="http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html">74.6</a></td>
  </tr>
  <tr>
    <td>ResNet-38</td>
    <td><a href="https://drive.google.com/drive/folders/1b3xzJM6TanoVfff-yIDvfoDe5MfXxKpE">Weights</a></td>
    <td>Pascal VOC 2012</td>
    <td><a href="http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html">75.1</a></td>
    <td><a href="http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html">74.6</a></td>
  </tr>
</table>

### 语义分割质量

| Model        | Backbone   | Google Drive | Dataset Type | *Test* |   *Val*   |
|:--------------:|:------------:|:--------------:|:--------------:|:-------:|:---------:|
| Deeplab-V1 | ResNet-38 |[Weights](https://drive.google.com/drive/folders/1b3xzJM6TanoVfff-yIDvfoDe5MfXxKpE)| Pascal VOC 2012 | [75.1](http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html) | [74.6](http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html) |
