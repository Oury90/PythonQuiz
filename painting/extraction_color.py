import colorgram
colors = colorgram.extract('image-2.jpg', 50)

# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
# print(rgb)

list_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_color.append(new_color)

print(list_color)