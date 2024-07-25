# 基于亲和向量一致性的弱监督语义分割
## 多阶段流程（Multi-Stage Process）
步骤1：下载训练数据集

步骤2：生成初始种子标签（Seed）

步骤3：细化初始种子标签(Seed)，生成语义分割掩码（Mask）

步骤4：
为了进一步评估方法性能，遵循先前研究工作[MCTformer](https://github.com/xulianuwa/MCTformer)和[ACR](https://github.com/sangrockEG/ACR)，采用RN38骨干网络训练全监督语义分割模型[DeeplabV1](https://github.com/YudeWang/semantic-segmentation-codebase/tree/main/experiment/seamv1-pseudovoc)
```
python train_deeplab.py
```
步骤4：生成分割效果并评估语义分割模型
```
python test_deeplab.py
```
## 实验结果（Experimental Results）
### 种子（Seed）和伪标签掩码（Mask）质量

<table>
  <tr>
    <th>Model</th>
    <th>Dataset Type</th>
    <th>Google Drive</th>
    <th>Seed</th>
    <th>+CRF</th>
    <th>Mask</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">AVC</td>
    <td align="center">VOC</td>
    <td align="center"><a href="https://drive.google.com/file/d/1GOAl3B3bywI5plCI3o7YLeEmeTCIAMdq/view?usp=drive_link">Weights</a></td>
    <td align="center"><a href="https://drive.google.com/file/d/1fEtLiFbvgT3cOGr2hCT7qMZGjD6iDl-p/view?usp=drive_link">75.8</a></td>
    <td align="center"><a href="https://drive.google.com/file/d/1v1HsX_Lc00TnEPveQGl7LlLJLbE5CNiE/view?usp=drive_link">77.5</a></td>
    <td align="center"><a href="https://drive.google.com/file/d/14-1WR1V6zm3RFAwDnuABeDUZCQkkULYu/view?usp=drive_link">77.8</a></td>
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
    <th>Dataset Type</th>    
    <th>Google Drive</th>
    <th>Test</th>
    <th>Val</th>
  </tr>
  <tr>
    <td rowspan="2" align="center">Deeplab-V1</td>
    <td rowspan="2" align="center">ResNet-38</td>
    <td align="center">VOC</td>
    <td align="center"><a href="https://drive.google.com/file/d/1Wsru6lHMhh8gYdO3Uep6XSq8f9BzHghT/view?usp=drive_link">Weights</a></td>
    <td align="center"><a href="http://host.robots.ox.ac.uk:8080/anonymous/NHKQPH.html">75.1</a></td>
    <td align="center"><a href="http://host.robots.ox.ac.uk:8080/anonymous/OE2YQO.html">74.6</a></td>
  </tr>
  <tr>
    <td align="center">MS COCO</td>
    <td align="center">-</td>
    <td align="center">-</td>
    <td align="center"><a href="https://drive.google.com/file/d/1NarR6JQArhc7gLuSZ1wEDH--HZgY-rRU/view?usp=drive_link">47.2</a></td>
  </tr>
</table>


