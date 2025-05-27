import cv2
import easyocr
import time

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Initialize webcam
cap = cv2.VideoCapture(0)

# Delay before checking (in seconds)s
delay = 1

# Read license plates from registration_plates.txt
with open('registration_plates.txt', 'r') as plates_file:
    plates = set(plate.strip() for plate in plates_file)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for the delay before checking the plate
    start_time = time.time()
    while time.time() - start_time < delay:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR
    result = reader.readtext(gray, detail=0)

    # Process the recognized plate
    plate_number = ' '.join(result)

    # print("Original License Plate Number:", plate_number)

    # Split the plate into three parts
    parts = plate_number.split('-')
    if len(parts) == 3:
        first_part = parts[0]
        middle_part = parts[1]
        last_part = parts[2]
        if len(first_part) == 3 and first_part[0] == '0':
            # Replace zero with letter O
            first_part = 'O' + first_part[1:]
            plate_number = f"{first_part}-{middle_part}-{last_part}"
            # print("Processed License Plate Number:", plate_number)
        if len(middle_part) == 1 and middle_part == '0':
            # Replace zero with letter O
            middle_part = 'O'
            plate_number = f"{first_part}-{middle_part}-{last_part}"

    print("License plate:", plate_number)

    # Write to test.txt
    with open('test.txt', 'a') as test_file:
        test_file.write(plate_number + '\n')

    # Check if the plate is in the database (registration_plates.txt)
    if plate_number in plates:
        print("ACCESS GRANTED! LICENSE PLATE FOUND IN DATABASE.")
        # Log access to entries.txt
        with open('entries.txt', 'a') as entries_file:
            timestamp = time.strftime("%H:%M:%S %d-%m-%Y")
            entries_file.write(f"{timestamp} - {plate_number} - ENTRY\n")
    else:
        print("ACCESS DENIED! LICENSE PLATE NOT FOUND IN DATABASE.")

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
