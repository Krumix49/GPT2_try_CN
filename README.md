version https://git-lfs.github.com/spec/v1
oid sha256:aa0b64573f5f4f9bfcd8a489a48ef3b32a9739f724646d801798863ec87ec5cb
size 6597

# GPT2 Trained By Scott Hong

Code Source: **lvfinn@GitHub**

Course Project of AI Design (1H'25) in Fudan University

A simple GPT2 project for training and getting the gist of generative pretrained transformers (GPT).

Modified and trained by Scott Hong (FDU: 25113040009).

## Training Set

Dataset: *The Immortal Ascension*, an online novel with about 7, 650, 000 characters and a file size of about 22 MB (json format)

Epoch: 15

Batch Size: 2 (takes up about 4.5 GB of VRAM)

Gradient Accumulation: 4

CPU: AMD Ryzen AI 9 HX 370 @ 2.00 GHz

GPU: Nvidia GeForce RTX 4060 Laptop GPU @ 1890 MHz with 8 GB GDDR6 VRAM @ 8001 MHz

## The result (I've chosen one best from the 10 results)

==================================== SAMPLE 6 ====================================

韩立见此，便大笑起来。“多谢前辈厚爱赐！”韩立口中称谢，并从储物袋中掏出一个巴掌大小的玉盒，递给了对方。“好了，你先下去吧。此事想来你也不想多说什么，就随我来找我。我正在洞府闭关修炼之，一直在修炼的。”韩立随手将玉盒接过，淡笑的吩咐道。“是，主人！”银月恭敬的应了一声，就接过玉盒，恭声的将盒盖打开。韩立不慌不忙的走出了石室，在门外的一座无名小山后，盘膝而坐，并没有说话一句。一盏茶工夫后韩立出现在了洞府大门处，目光闪动两下后，才将神识从其中一散而出。“韩前辈，这次将洞府放出来，可是我等从大长老口中得知，现在已经知道小灵天不离十余月了。前辈是否将洞府修炼至大乘，晚辈这一次能否给小姐一个惊喜。”银月站起身来，轻声的说道。韩立点点头，不再说什么的走进了密室中的密室中。单手拿着一块闪动红色玉简，在一块蒲团上一动不动起来。韩立目光在玉简上一扫后，点点头的说道：“这个请前辈放心，有什么事情尽管吩咐就是了。”随后他想了一想后，伸手将玉简一把抓在了手中，神识沉浸其中不动起来。片刻后，韩立将神识从玉简中抽出，将玉简一把抓到了手中，用神念一扫其中一探后，眉梢微微一挑。“果然和以前一样，还要再等数年的时间了吧。这一次，我会将神念浸泡的各个地方都查看一遍，并且从里面说，似乎是一个很罕见的洞府之地东西。这个玉简，你可懂得到一本叫做红罗仙酒的仙酒，是否有资格在里面？”韩立将玉简拿到手中，将玉简往额头上一贴，眉头微微一皱后，又向那红晕明尊直接扫了一眼。“真有些麻烦了！这里虽然不是仙人之物的。但也可能只有仙人才能得此灵酒！”银月在韩立神念一扫旁边的火，也有些讶然的说道。“这里的一切，妾身还真不太清楚。只是喜欢饮一杯的话，我这里还有几杯的。”韩立笑了一笑，将玉简往桌上一放，神念往其中一扫后，脸上就露出了一丝笑容。“好了，韩道友将圣斋带在了洞府后，在那里暂时居住一段时间了”银月嫣然一笑的说道。“那就有劳韩道友了。”韩立不置可否的回了一句后，人就一抱拳的踏入密室中。密室中，韩立坐在了蒲团上，神念四下飞快扫过后，脸上却闪过诧异的表情。火月和朱果儿则站在一侧，并未交谈什么。“韩兄看来你对红罗果颇感兴趣。妾身虽然在一个月中待了数月之久，但自问在修为上也远不是一般的灵酒。否则一旦失效，恐怕整个魔界都不会轻易放弃的。”韩立微笑的冲赤须老者说道。“不过在此之前，妾身又有些事情要向仙子多照应的。不过妾身虽然知道仙界大乘存在，但也有仙人能够

==================================================================================



## File Structure

### Cache

**vocab_small.txt:** The vocabulary file for generating content. ***[Initially Provided]***

### Config

**model_config_small.json:** The JSON file for the hyperparameters of the GPT2 model. ***[Initially provided, modified a little]***

### Data

**tokenized:** The tokenized data of the novel

**clr_ctrl.py:** The Python script for cleaning control symbols and assembling the dataset. ***[Initially Provided]***

**input.json and train.json:** input.json is the raw data that was transformed from the original text file, and train.json is the converted file for training.

**凡人修仙传.txt:** The text file of the famous novel that has been chosen for shooting TV drama *The Immortal Ascension*.

### mnt

**samples.txt:** Stores the generated 10 samples of the consecutive passages.

### Model

Stores the final version of the trained model in binary (.bin) form. Those generated during the epochs are not included.

### TensorBoard_Summary

The summary file of TensorBoard during the training. ***[Machine Generated]***

### Tokenizations

The tokenization scripts for transforming "characters" into "tokens". ***[Initially Provided]***

### console_record.txt

This text file records the console output of the training and inferencing process.

### generate.py

The Python script for generating the text response of the continuation of the novel.

To call the script, we can use python in bash console and add parameters to control its behavior.

```bash
python generate.py --device 0 --length 1000 --tokenizer_path cache/vocab_small.txt --model_path model/final_model --prefix "[CLS]韩立见此，便大笑起来" --topp 1 --temperature 1.0 --save_samples --save_samples_path ./mnt/
```

Tips: --device configures the device used for inference. If this is set to 0, GPU will be used. Using GPU consumes more energy but enables to generate within about 25s, while using CPU (set to 1) needs about 50s or more.

### train.py

The Python script for training the model. I changed the batch size from 8 to 2 since the Nvidia RTX 4060 has only 8 GB VRAM; a batch size of 8 will lead to about 19 GB of memory usage, slowing down despite having shared memory from system RAM.

The train file can be also called through bash console.

```bash
python train.py --model_config config/model_config_small.json --tokenized_data_path data/tokenized/ --tokenizer_path cache/vocab_small.txt --raw_data_path data/train.json --epochs 15 --log_step 200 --stride 512 --output_dir model/ --device 0,1 --num_pieces 100 --raw
```

The training process on RTX 4060 takes 45 minutes / epoch.
