# 基于亲和向量一致性的弱监督语义分割(Weakly Supervised Semantic Segmentation Based on Affnity Vector Consistency)
## Download datasets
* For the PASCAL VOC 2012 dataset, you can download it from the [official website](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar).
+ For the PASCAL VOC 2012 dataset, you can download it from the [official website](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar).
- For the PASCAL VOC 2012 dataset, you can download it from the [official website](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar).
```
```
## Usage

Step 1: Train AVC

```
```

Step 2: Generate initial seed label (Seed)

```
```

Step 3: Use CRF or [PSA](https://github.com/jiwoon-ahn/psa) to refine the initial seed label (Seed) and generate a pseudo mask label (Mask)

```
```

Step 4: To further evaluate the performance of the method, we followed previous workflows such as [MCTformer](https://github.com/xulianuwa/MCTformer) and [ACR](https://github.com/sangrockEG/ACR). Replace the Ground Truth label with a pseudo-label mask and use the RN38 backbone network to train a fully supervised semantic segmentation model [DeeplabV1](https://github.com/YudeWang/semantic-segmentation-codebase/tree/main/experiment/seamv1-pseudovoc).
```
python train_deeplab.py
```
Generate segmentation results and evaluate semantic segmentation models
```
python test_deeplab.py
```
## Experimental Results
Initial Seed and Pseudo-Label Mask Quality

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

Semantic Segmentation Quality

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


