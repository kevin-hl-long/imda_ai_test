# imda_ai_test

## Folder Structure

```
imda_ai_test/
├── captcha.py                  # Script for CAPTCHA recognition using template matching
├── character_extraction.py     # Script to extract character templates from labeled CAPTCHAs
├── README.md                   
├── requirements.txt            
│
└── data/
    ├── characters/             # Template images for each character (0-9, A-Z)
    │   ├── 0.png
    │   └── ...
    │
    ├── Captchas/
    │   ├── input/              # CAPTCHA images to be recognized
    │   │   ├── input00.jpg
    │   │   └── ...
    │   │
    │   └── output/             # Recognition results
    │       ├── input00.txt
    │       └── ...
    │
    └── sampleCaptchas/
        ├── input/              # Sample CAPTCHA images
        │   ├── input00.jpg
        │   └── ...
        │
        └── output/             # Ground-truth labels
            ├── output00.txt
            └── ...
```
## Usage

### 1. Extract Character Templates

To generate character templates from labeled sample CAPTCHAs, run:

```bash
python character_extraction.py
```

This will populate the `data/characters/` directory with one PNG file per character.

### 2. Recognize CAPTCHA Images

To recognize the characters in the CAPTCHA images in `data/Captchas/input/` and write the results to `data/Captchas/output/`, run:

```bash
python captcha.py
```

Each output `.txt` file will contain the recognized string for the corresponding input image.


