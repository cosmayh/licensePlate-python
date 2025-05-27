**License Plate Access System**

This is a pilot project built with Python, OpenCV, and EasyOCR. It simulates a basic license plate recognition system for access control. The system captures video from a webcam, reads license plates using OCR, and checks if the detected plate exists in a predefined list. If the plate is found, access is granted and logged; otherwise, access is denied.

---

**Note on License Plate Format**

This project is designed to recognize Bosnian license plates.  
It specifically checks for plate formats such as: `A21-K-578` or `A61-O-050`, which are commonly used in Bosnia and Herzegovina.  
Some corrections are applied in code, such as replacing the digit `0` with the letter `O` where appropriate, to better match expected plate styles.

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
