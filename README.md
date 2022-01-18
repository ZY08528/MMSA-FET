# MMSA-Feature Extraction Toolkit

[![](https://badgen.net/badge/license/GPL-3.0/green)](#License) [![](https://badgen.net/github/release/FlameSky-S/MMSA-FET)](https://github.com/FlameSky-S/M-SENA-frontend/releases) [![](https://badgen.net/badge/contact/THUIAR/purple)](https://thuiar.github.io/)

MMSA-Feature Extraction Toolkit extracts multimodal features for Multimodal Sentiment Analysis Datasets. It integrates several commonly used tools for visual, acoustic and text modality. The extracted features are compatible with the [MMSA](https://github.com/thuiar/MMSA) Framework and thus can be used directly. The tool can also extract features for single videos.

## 1. Installation

MMSA-Feature Extraction Toolkit is available from Pypi:

```bash
$ pip install MMSA-FET
```

For the OpenFaceExtractor to work, a few system-wide dependancies are needed. See [Dependency Installation](https://github.com/FlameSky-S/MMSA-FET/wiki/Dependency-Installation) for more information.

## 2. Quick Start

MMSA-FET is fairly easy to use. Below is a basic example on how to extract features for a single video file and a dataset folder.

> **Note:** The dataset folder should be arranged the same way as the MMSA Framework does, see [Dataset Folder Structure](https://github.com/FlameSky-S/MMSA-FET/wiki/Dataset-Folder-Structure) for details. Arranged datasets can be downloaded [here](https://pan.baidu.com/s/1oksuDEkkd3vGg2oBMBxiVw) with code `ctgs`

```python
from MSA_FET import FeatureExtractionTool

# initialize with config file
fet = FeatureExtractionTool("config.json")

# extract features for single video
feature = fet.run_single("input.mp4")
print(feature)

# extract for dataset & save features to file
feature = fet.run_dataset(dataset_dir="~/MOSI", out_file="output/feature.pkl")
```

The `config.json` is the path to a custom config file, the format of which is introduced [here](#3-Config-File).

For more details, please read [APIs](https://github.com/FlameSky-S/MMSA-FET/wiki/APIs).

## 3. Config File

MMSA-FET comes with a few example configs which can be used like below.

```python
# Each supported tool has an example config
fet = FeatureExtractionTool(config="librosa")
fet = FeatureExtractionTool(config="opensmile")
fet = FeatureExtractionTool(config="wav2vec")
fet = FeatureExtractionTool(config="openface")
fet = FeatureExtractionTool(config="mediapipe")
fet = FeatureExtractionTool(config="bert")
fet = FeatureExtractionTool(config="xlnet")
```

For customized features, you'll have to provide a config file which is in the following format.

```json
{
  "audio": {
    "tool": "librosa",
    "sample_rate": null,
    "args": {
      "mfcc": {
        "n_mfcc": 20,
        "htk": true
      },
      "rms": {},
      "zero_crossing_rate": {},
      "spectral_rolloff": {},
      "spectral_centroid": {}
    }
  },
  "video": {
    "tool": "openface",
    "fps": 25,
    "average_over": 3,
    "args": {
      "hogalign": false,
      "simalign": false,
      "nobadaligned": false,
      "landmark_2D": true,
      "landmark_3D": false,
      "pdmparams": false,
      "head_pose": true,
      "action_units": true,
      "gaze": true,
      "tracked": false
    }
  },
  "text": {
    "model": "bert",
    "device": "cpu",
    "pretrained": "models/bert_base_uncased",
    "args": {}
  }
}
```

## 4. Supported Tools & Features

### 4.1 Audio Tools

- **Librosa** ([link](https://librosa.org/doc/latest/index.html))

  Supports all librosa features listed [here](https://librosa.org/doc/latest/feature.html), including: [mfcc](https://librosa.org/doc/latest/generated/librosa.feature.mfcc.html#librosa.feature.mfcc), [rms](https://librosa.org/doc/latest/generated/librosa.feature.rms.html#librosa.feature.rms), [zero_crossing_rate](https://librosa.org/doc/latest/generated/librosa.feature.zero_crossing_rate.html#librosa.feature.zero_crossing_rate), [spectral_rolloff](https://librosa.org/doc/latest/generated/librosa.feature.spectral_rolloff.html#librosa.feature.spectral_rolloff), [spectral_centroid](https://librosa.org/doc/latest/generated/librosa.feature.spectral_centroid.html#librosa.feature.spectral_centroid), etc. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#11-librosa).

- **openSMILE** ([link](https://audeering.github.io/opensmile-python/))

  Supports all feature sets listed [here](https://audeering.github.io/opensmile-python/api-smile.html#featureset), including: [ComParE_2016](http://www.tangsoo.de/documents/Publications/Schuller16-TI2.pdf), [GeMAPS](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf), [eGeMAPS](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf), emobase, etc. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#12-opensmile).

- **Wav2vec2** ([link](https://huggingface.co/docs/transformers/model_doc/wav2vec2))

  Integrated from huggingface transformers. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#13-wav2vec2).

### 4.2 Video Tools

- **OpenFace** ([link](https://github.com/TadasBaltrusaitis/OpenFace))

  Supports all features in OpenFace's FeatureExtraction binary, including: facial landmarks in 2D and 3D, head pose, gaze related, facial action units, HOG binary files. Details of these features can be found in the OpenFace Wiki [here](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format) and [here](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Action-Units). Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#21-openface).

- **MediaPipe** ([link](https://google.github.io/mediapipe/))

  Supports [face](https://google.github.io/mediapipe/solutions/face_mesh.html) mesh and [holistic](https://google.github.io/mediapipe/solutions/holistic)(face, hand, pose) solutions. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#22-mediapipe).

### 4.3 Text Tools

- **BERT** ([link](https://huggingface.co/docs/transformers/model_doc/bert))

  Integrated from huggingface transformers. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#31-bert).

- **XLNet** ([link](https://huggingface.co/docs/transformers/model_doc/xlnet))

  Integrated from huggingface transformers. Detailed configurations can be found [here](https://github.com/FlameSky-S/MMSA-FET/wiki/Configurations#32-xlnet).