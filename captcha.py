import cv2
import os
import numpy as np

class Captcha(object):
    def __init__(self, char_dir="data/characters"):
        self.char_masks = {}
        for filename in os.listdir(char_dir):
            if filename.endswith(".png"):
                char = os.path.splitext(filename)[0]
                mask = cv2.imread(os.path.join(char_dir, filename), cv2.IMREAD_GRAYSCALE)
                self.char_masks[char] = mask

        # each character is 8x10 pixels, separated by 1 pixel, 5 from the left, 11 from the top
        self.char_positions = [(5 + i * 9, 11, 8, 10) for i in range(5)]

    def create_mask(self, img_path):
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Image not found or cannot be read: {img_path}")
        _, mask = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
        return mask

    def match_character(self, char_img):
        for char, mask in self.char_masks.items():
            print(mask)
            if np.array_equal(char_img, mask):
                return char
        return "?"  # no exact match found

    def __call__(self, im_path, save_path):
        mask = self.create_mask(im_path)
        result = ""
        
        for (x, y, w, h) in self.char_positions:
            char_img = mask[y:y+h, x:x+w]
            matched_char = self.match_character(char_img)
            result += matched_char

        with open(save_path, "w") as f:
            f.write(result)

# test folders
input_dir = "data/Captchas/input"
output_dir = "data/Captchas/output"

captcha = Captcha()

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        img_path = os.path.join(input_dir, filename)
        basename = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, f"{basename}.txt")
        captcha(img_path, output_path)