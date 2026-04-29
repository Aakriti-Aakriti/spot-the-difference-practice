import cv2
import random

img = cv2.imread("images/sample.jpg")
clone = img.copy()

height, width, _ = img.shape

# store all differences here
differences = []

# check overlap function
def is_overlapping(new_rect, existing_rects):
    x1, y1, w1, h1 = new_rect

    for (x2, y2, w2, h2) in existing_rects:
        if not (x1 + w1 < x2 or x2 + w2 < x1 or
                y1 + h1 < y2 or y2 + h2 < y1):
            return True
    return False

# generate 5 differences
while len(differences) < 5:

    x = random.randint(50, width - 150)
    y = random.randint(50, height - 150)
    w, h = 80, 80

    new_diff = (x, y, w, h)

    # ensure no overlap
    if not is_overlapping(new_diff, differences):
        differences.append(new_diff)

        # choose a random modification type
        diff_type = random.choice(["color", "blur", "shape"])

        region = clone[y:y+h, x:x+w]

        if diff_type == "color":
            clone[y:y+h, x:x+w] = region + 60

        elif diff_type == "blur":
            clone[y:y+h, x:x+w] = cv2.GaussianBlur(region, (15, 15), 0)

        elif diff_type == "shape":
            cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 0, 255), -1)

# draw rectangles (DEBUG view)
for (x, y, w, h) in differences:
    cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show images
cv2.imshow("Original", img)
cv2.imshow("Modified (5 Differences)", clone)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print for debugging
print("All differences:")
for d in differences:
    print(d)
