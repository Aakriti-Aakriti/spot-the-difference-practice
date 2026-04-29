import cv2
import random

img = cv2.imread("images/sample.jpg")
clone = img.copy()

height, width, _ = img.shape

differences = []

# generate 5 differences (same logic as before)
def is_overlapping(new_rect, existing_rects):
    x1, y1, w1, h1 = new_rect

    for (x2, y2, w2, h2) in existing_rects:
        if not (x1 + w1 < x2 or x2 + w2 < x1 or
                y1 + h1 < y2 or y2 + h2 < y1):
            return True
    return False

while len(differences) < 5:
    x = random.randint(50, width - 150)
    y = random.randint(50, height - 150)
    w, h = 80, 80

    new_diff = (x, y, w, h)

    if not is_overlapping(new_diff, differences):
        differences.append(new_diff)
        cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 0, 255), -1)

# store found differences
found = []

# 🎯 CLICK HANDLER
def mouse_click(event, x, y, flags, param):
    global clone, found

    if event == cv2.EVENT_LBUTTONDOWN:

        print("Clicked at:", x, y)

        for (dx, dy, dw, dh) in differences:

            # check if already found
            if (dx, dy, dw, dh) in found:
                continue

            if dx <= x <= dx + dw and dy <= y <= dy + dh:
                print("✔ Correct!")

                found.append((dx, dy, dw, dh))

                # mark found visually
                cv2.rectangle(clone, (dx, dy), (dx+dw, dy+dh), (0, 255, 0), 2)
                break

        cv2.imshow("Game", clone)


# show image
cv2.imshow("Game", clone)
cv2.setMouseCallback("Game", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
