import cv2
import os

def create_mask(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found or cannot be read: {img_path}")
    _, mask = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
    return mask

def extract_characters(mask, char_positions, chars, out_dir):
    for i, (x, y, w, h) in enumerate(char_positions):
        char_img = mask[y:y+h, x:x+w]
        char = chars[i]
        out_path = os.path.join(out_dir, f"{char}.png")
        cv2.imwrite(out_path, char_img)

# each character is 8x10 pixels, separated by 1 pixel, 5 from the left, 11 from the top
char_positions = [(5 + i * 9, 11, 8, 10) for i in range(5)]

input_dir = "data/sampleCaptchas/input"
output_dir = "data/sampleCaptchas/output"
char_dir = "data/characters"

for idx in range(25):
    if idx == 21: # output21.txt is missing
        continue
    img_path = os.path.join(input_dir, f"input{idx:02d}.jpg")
    txt_path = os.path.join(output_dir, f"output{idx:02d}.txt")
    with open(txt_path, "r") as f:
        chars = f.read()
    mask = create_mask(img_path)
    extract_characters(mask, char_positions, chars, char_dir)
print("DONE")

