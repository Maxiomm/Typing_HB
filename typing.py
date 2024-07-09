import pytesseract
import pyautogui
import keyboard
import mss
from PIL import Image
import os

# Définir les coordonnées de la zone à capturer
left = 351
top = 525
width = 1197
height = 181

pyautogui.click(1550, 615)

# Attendre jusqu'à ce que le pixel à la position (387, 560) ne soit plus de couleur noire (0, 0, 0)
while pyautogui.pixelMatchesColor(387, 560, (0, 0, 0)):
    pass

# Capturer la zone spécifiée avec mss
with mss.mss() as sct:
    monitor = {"top": top, "left": left, "width": width, "height": height}
    screenshot = sct.grab(monitor)

# Enregistrer la capture d'écran temporairement
screenshot_path = "temp_screenshot.png"
Image.frombytes("RGB", screenshot.size, screenshot.rgb).save(screenshot_path)

# Utiliser Pytesseract pour extraire le texte de l'image
extracted_text = pytesseract.image_to_string(Image.open(screenshot_path))

# Remplacer les cas exceptionnels
extracted_text = extracted_text.replace('\n', ' ')
extracted_text = extracted_text.replace('|', 'I')
extracted_text = extracted_text.replace('[', '')

if extracted_text[0] == "I":
    # Supprimer le premier caractère
    extracted_text = extracted_text[1:]

# Afficher le texte extrait
print("Texte extrait:", extracted_text)

# Simuler la saisie automatique du texte extrait
keyboard.write(extracted_text)

# Supprimer l'image temporaire
os.remove(screenshot_path)
