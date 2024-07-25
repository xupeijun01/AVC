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

<table>
  <tr>
    <th>Model</th>
    <th>Dataset Type</th>
    <th>Weights</th>
    <th>Seed</th>
    <th>+CRF</th>
    <th>Mask</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">AVC</td>
    <td align="center">VOC</td>
    <td align="center"><a href="https://drive.google.com/file/d/1GOAl3B3bywI5plCI3o7YLeEmeTCIAMdq/view?usp=drive_link">Weights</a></td>
    <td align="center"><a href="https">75.8</a></td>
    <td align="center"><a href="https">77.5</a></td>
    <td align="center"><a href="https">77.8</a></td>
  </tr>
  <tr>
    <td align="center">MS COCO</td>
    <td align="center"><a href="https://drive.google.com/file/d/1yRzMH-LbsK3IidONspOJYuZaNTgdxM96/view?usp=drive_link">Weights</a></td>
    <td align="center">45.8</td>
    <td align="center">-</td>
    <td align="center"><a href="https://drive.google.com/file/d/1UFEk8uN_81E0hLU50oR9FsiL6QvAon_u/view?usp=drive_link">48.4</a></td>
  </tr>
</table>

### 语义分割质量

<table>
  <tr>
    <th>Model</th>
    <th>Backbone</th>
    <th>Google Drive</th>
    <th>Dataset Type</th>
    <th>Test</th>
    <th>Val</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">Deeplab-V1</td>
    <td rowspan="2" align="center">ResNet-38</td>
    <td align="center"><a href="https://drive.google.com/file/d/1Wsru6lHMhh8gYdO3Uep6XSq8f9BzHghT/view?usp=drive_link">Weights</a></td>
    <td align="center">VOC</td>
    <td align="center"><a href="http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html">75.1</a></td>
    <td align="center"><a href="http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html">74.6</a></td>
  </tr>
  <tr>
    <td align="center">-</td>
    <td align="center">MS COCO</td>
    <td align="center">-</td>
    <td align="center"><a href="https://drive.google.com/file/d/1NarR6JQArhc7gLuSZ1wEDH--HZgY-rRU/view?usp=drive_link">47.2</a></td>
  </tr>
</table>

