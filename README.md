**License Plate Access System**

This is a pilot project built with Python, OpenCV, and EasyOCR. It simulates a basic license plate recognition system for access control. The system captures video from a webcam, reads license plates using OCR, and checks if the detected plate exists in a predefined list. If the plate is found, access is granted and logged; otherwise, access is denied.

---

**Features**

- Real-time license plate recognition using webcam
- OCR with EasyOCR (supports multiple languages)
- Compares recognized plates against a list (`registration_plates.txt`)
- Logs entry time and plate number to `ulaz.txt` when access is granted
- Simple and lightweight, designed as a prototype

---

**Dependencies**

The following Python libraries are required:

- opencv-python
- easyocr`
