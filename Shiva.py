import turtle
import math
import time

# Sacred Shiva Namalu - Beautiful selections from 108 names
SHIVA_NAMALU = [

    "ఓం నమః శివాయ",
    "శ్రీ మహాదేవాయ నమః",
    "శ్రీ శంకరాయ నమః",
    "శ్రీ నీలకంఠాయ నమః",
    "శ్రీ త్రినేత్రాయ నమః",
    "శ్రీ పశుపతయే నమః",
    "శ్రీ మహేశ్వరాయ నమః",
    "శ్రీ రుద్రాయ నమః",
    "శ్రీ శంభవే నమః",
    "శ్రీ చంద్రశేఖరాయ నమః",
    "శ్రీ గంగాధరాయ నమః",
    "శ్రీ విశ్వనాథాయ నమః"
]

for mantra in SHIVA_NAMALU:
    print(mantra)


# Setup screen
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.title('Shivalingam 🙏 - code_with_vibe')
screen.bgcolor('#0a1628')  # Deep dark blue background

try:
    root = screen.getcanvas().winfo_toplevel()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()
    root.bind('<Escape>', lambda e: root.destroy())
except Exception:
    pass

# Create turtle for drawing
pen = turtle.Turtle()
pen.shape('circle')
pen.shapesize(0.3, 0.3)
pen.color('white')
pen.speed(0)
screen.tracer(0)

# Drawing parameters - Adjusted for realistic proportions
CENTER_X = 0
CENTER_Y = -20
LINGAM_HEIGHT = 160
LINGAM_WIDTH = 80
YONI_WIDTH = 240
YONI_HEIGHT = 50
BASE_WIDTH = 200
BASE_HEIGHT = 35


def draw_filled_shape(points, fill_color, outline_color=None, animate=True, update_interval=3):
    """Draw a filled polygon from list of points with optional animation."""
    if outline_color is None:
        outline_color = fill_color
    pen.fillcolor(fill_color)
    pen.pencolor(outline_color)
    pen.pensize(1)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.begin_fill()

    if animate:
        for i, (x, y) in enumerate(points[1:]):
            pen.goto(x, y)
            if i % update_interval == 0:
                screen.update()
    else:
        for x, y in points[1:]:
            pen.goto(x, y)

    pen.goto(points[0])
    pen.end_fill()
    pen.penup()
    screen.update()


def draw_blue_glow():
    """Draw the cyan/blue glow effect around and behind the Shivalingam."""
    for r in range(250, 30, -5):
        intensity = (250 - r) / 250.0
        blue = int(40 + intensity * 80)
        green = int(20 + intensity * 60)
        color = f'#0a{green:02x}{blue:02x}'

        points = []
        for angle in range(0, 361, 5):
            rad = math.radians(angle)
            x = CENTER_X + r * math.cos(rad)
            y = CENTER_Y + 30 + r * 0.6 * math.sin(rad)
            points.append((x, y))
        draw_filled_shape(points, color, color, animate=False)
    screen.update()


def draw_base_glow():
    """Draw the cyan glow at the base."""
    for r in range(8, 0, -1):
        intensity = r / 8.0
        cyan_val = int(200 * intensity)
        color = f'#00{cyan_val:02x}{cyan_val:02x}'

        points = []
        for angle in range(0, 361, 5):
            rad = math.radians(angle)
            x = CENTER_X + (BASE_WIDTH / 2 + 15 + r * 2) * math.cos(rad)
            y = CENTER_Y - 120 + (20 + r) * math.sin(rad)
            points.append((x, y))
        draw_filled_shape(points, color, color, animate=False)

    # Glow around yoni rim
    for r in range(6, 0, -1):
        intensity = r / 6.0
        cyan_val = int(180 * intensity)
        color = f'#00{cyan_val:02x}{cyan_val:02x}'

        points = []
        for angle in range(0, 361, 5):
            rad = math.radians(angle)
            x = CENTER_X + (YONI_WIDTH / 2 + r * 2) * math.cos(rad)
            y = CENTER_Y - 20 + (25 + r) * math.sin(rad)
            points.append((x, y))
        draw_filled_shape(points, color, color, animate=False)
    screen.update()


def draw_bottom_base():
    """Draw the bottom circular base with glow."""
    base_y = CENTER_Y - 120
    # Main base - dark black
    points = []
    for angle in range(0, 361, 3):
        rad = math.radians(angle)
        x = CENTER_X + BASE_WIDTH / 2 * math.cos(rad)
        y = base_y + BASE_HEIGHT / 2 * math.sin(rad)
        points.append((x, y))
    draw_filled_shape(points, '#1a1a1a', '#1a1a1a', animate=True, update_interval=2)

    # Slight highlight on top edge
    highlight_points = []
    for angle in range(160, 381, 3):
        rad = math.radians(angle)
        x = CENTER_X + (BASE_WIDTH / 2 - 5) * math.cos(rad)
        y = base_y + 5 + (BASE_HEIGHT / 2 - 5) * math.sin(rad)
        highlight_points.append((x, y))
    if len(highlight_points) > 2:
        draw_filled_shape(highlight_points, '#252525', '#252525', animate=False)
    screen.update()


def draw_middle_pedestal():
    """Draw the middle connecting part between base and yoni."""
    mid_bottom = CENTER_Y - 100
    mid_top = CENTER_Y - 50
    left_bottom = CENTER_X - BASE_WIDTH / 2 + 20
    right_bottom = CENTER_X + BASE_WIDTH / 2 - 20
    left_top = CENTER_X - YONI_WIDTH / 2 + 10
    right_top = CENTER_X + YONI_WIDTH / 2 - 10

    for layer in range(10, 0, -1):
        factor = layer / 10.0
        shade = int(25 + (1 - factor) * 15)
        color = f'#{shade:02x}{shade:02x}{shade:02x}'
        offset = (1 - factor) * 10
        points = [
            (left_bottom + offset, mid_bottom),
            (right_bottom - offset, mid_bottom),
            (right_top - offset, mid_top),
            (left_top + offset, mid_top)
        ]
        draw_filled_shape(points, color, color, animate=False)
    screen.update()


def draw_yoni():
    """Draw the Yoni (water collection basin) - dark with rim."""
    yoni_y = CENTER_Y - 25
    # Outer rim
    outer_points = []
    for angle in range(0, 361, 3):
        rad = math.radians(angle)
        x = CENTER_X + YONI_WIDTH / 2 * math.cos(rad)
        y = yoni_y + YONI_HEIGHT / 2 * math.sin(rad)
        outer_points.append((x, y))
    draw_filled_shape(outer_points, '#1a1a1a', '#1a1a1a', animate=True, update_interval=2)

    # Inner depression
    inner_points = []
    for angle in range(0, 361, 3):
        rad = math.radians(angle)
        x = CENTER_X + (YONI_WIDTH / 2 - 15) * math.cos(rad)
        y = yoni_y + (YONI_HEIGHT / 2 - 8) * math.sin(rad)
        inner_points.append((x, y))
    draw_filled_shape(inner_points, '#0d0d0d', '#0d0d0d', animate=False)

    # Rim around lingam opening
    rim_points = []
    for angle in range(0, 361, 3):
        rad = math.radians(angle)
        x = CENTER_X + (LINGAM_WIDTH / 2 + 20) * math.cos(rad)
        y = yoni_y + 5 + (LINGAM_WIDTH / 4 + 8) * math.sin(rad)
        rim_points.append((x, y))
    draw_filled_shape(rim_points, '#252525', '#252525', animate=False)
    screen.update()


def draw_spout():
    """Draw the water spout (Jalhari) extending to the right."""
    spout_y = CENTER_Y - 25
    spout_start = CENTER_X + YONI_WIDTH / 2 - 35
    spout_length = 70
    spout_width = 25

    spout_points = [
        (spout_start, spout_y + spout_width / 2),
        (spout_start + spout_length * 0.7, spout_y + spout_width / 2 - 3),
        (spout_start + spout_length, spout_y + spout_width / 3),
        (spout_start + spout_length + 15, spout_y),
        (spout_start + spout_length, spout_y - spout_width / 3),
        (spout_start + spout_length * 0.7, spout_y - spout_width / 2 + 3),
        (spout_start, spout_y - spout_width / 2)
    ]
    draw_filled_shape(spout_points, '#1a1a1a', '#1a1a1a', animate=True, update_interval=1)

    channel_points = [
        (spout_start + 5, spout_y + spout_width / 3 - 2),
        (spout_start + spout_length - 5, spout_y + spout_width / 4 - 2),
        (spout_start + spout_length - 5, spout_y - spout_width / 4 + 2),
        (spout_start + 5, spout_y - spout_width / 3 + 2)
    ]
    draw_filled_shape(channel_points, '#0a0a0a', '#0a0a0a', animate=False)
    screen.update()


def draw_lingam():
    """Draw the sacred Shivalingam."""
    lingam_bottom = CENTER_Y - 15
    lingam_top = lingam_bottom + LINGAM_HEIGHT
    dome_height = LINGAM_WIDTH * 0.5
    dome_center_y = lingam_top - dome_height
    w = LINGAM_WIDTH

    pen.penup()
    pen.goto(CENTER_X - w / 2, lingam_bottom)
    pen.pendown()
    pen.fillcolor('#1a1a1a')
    pen.pencolor('#1a1a1a')
    pen.begin_fill()

    # Left side up
    pen.goto(CENTER_X - w / 2, dome_center_y)
    # Dome arc
    for angle in range(180, -1, -2):
        rad = math.radians(angle)
        x = CENTER_X + (w / 2) * math.cos(rad)
        y = dome_center_y + dome_height * math.sin(rad)
        pen.goto(x, y)
    # Right side down
    pen.goto(CENTER_X + w / 2, lingam_bottom)
    pen.goto(CENTER_X - w / 2, lingam_bottom)
    pen.end_fill()
    pen.penup()
    screen.update()

    # Add subtle 3D shading
    highlight_points = []
    for y in range(int(lingam_bottom + 5), int(dome_center_y - 5), 3):
        highlight_points.append((CENTER_X + w / 2 - 8, y))
    for y in range(int(dome_center_y - 5), int(lingam_bottom + 5), -3):
        highlight_points.append((CENTER_X + w / 2 - 3, y))
    if len(highlight_points) > 3:
        draw_filled_shape(highlight_points, '#282828', '#282828', animate=False)

    shadow_points = []
    for y in range(int(lingam_bottom + 5), int(dome_center_y - 5), 3):
        shadow_points.append((CENTER_X - w / 2 + 3, y))
    for y in range(int(dome_center_y - 5), int(lingam_bottom + 5), -3):
        shadow_points.append((CENTER_X - w / 2 + 8, y))
    if len(shadow_points) > 3:
        draw_filled_shape(shadow_points, '#121212', '#121212', animate=False)

    dome_shine = []
    for angle in range(120, 60, -3):
        rad = math.radians(angle)
        x = CENTER_X + (w / 2 - 15) * math.cos(rad)
        y = dome_center_y + (dome_height - 10) * math.sin(rad)
        dome_shine.append((x, y))
    for angle in range(60, 120, 3):
        rad = math.radians(angle)
        x = CENTER_X + (w / 2 - 20) * math.cos(rad)
        y = dome_center_y + (dome_height - 15) * math.sin(rad)
        dome_shine.append((x, y))
    if len(dome_shine) > 3:
        draw_filled_shape(dome_shine, '#252525', '#252525', animate=False)
    screen.update()


def draw_tripundra():
    """Draw the three sacred horizontal lines (Tripundra) with red tilak."""
    tripundra_y = CENTER_Y + 60
    line_width = 35
    line_height = 4
    line_gap = 12

    for i in range(3):
        y = tripundra_y + (1 - i) * line_gap
        line_points = []
        for t in range(0, 101, 5):
            t_norm = (t - 50) / 50.0
            x = CENTER_X + t_norm * line_width / 2
            curve = -2 * (1 - t_norm ** 2)
            ly = y + curve
            line_points.append((x, ly + line_height / 2))
        for t in range(100, -1, -5):
            t_norm = (t - 50) / 50.0
            x = CENTER_X + t_norm * line_width / 2
            curve = -2 * (1 - t_norm ** 2)
            ly = y + curve
            line_points.append((x, ly - line_height / 2))
        draw_filled_shape(line_points, '#d4d4d4', '#d4d4d4', animate=True, update_interval=1)

    # Red tilak
    tilak_y = tripundra_y
    tilak_points = []
    for angle in range(0, 361, 10):
        rad = math.radians(angle)
        x = CENTER_X + 6 * math.cos(rad)
        y = tilak_y + 5 * math.sin(rad)
        tilak_points.append((x, y))
    draw_filled_shape(tilak_points, '#cc2200', '#aa1100', animate=True, update_interval=1)
    screen.update()


def cycle_namalu():
    """Cycle through the sacred Shiva namalu with animation."""
    namalu_pen = turtle.Turtle()
    namalu_pen.hideturtle()
    namalu_pen.speed(0)
    namalu_pen.penup()

    for i, namam in enumerate(SHIVA_NAMALU):
        namalu_pen.clear()
        # Draw current namam
        namalu_pen.goto(0, 290)
        namalu_pen.pencolor('#FFFFFF')
        namalu_pen.write(namam, align='center', font=('Arial', 24, 'bold'))

        # Progress indicator
        namalu_pen.goto(0, -300)
        namalu_pen.pencolor('#00CCCC')
        progress = "◈ " * (i + 1) + "◇ " * (len(SHIVA_NAMALU) - i - 1)
        namalu_pen.write(progress, align='center', font=('Arial', 10, 'normal'))

        screen.update()
        time.sleep(1.8)

    # Final display
    namalu_pen.clear()
    namalu_pen.goto(0, 290)
    namalu_pen.pencolor('#00FFFF')
    namalu_pen.write('🙏 ॐ नमः शिवाय 🙏', align='center', font=('Arial', 28, 'bold'))
    namalu_pen.goto(0, -300)
    namalu_pen.pencolor('#00CCCC')
    namalu_pen.write('|| हर हर महादेव ||', align='center', font=('Arial', 16, 'bold'))
    screen.update()


# Main drawing sequence
print("=" * 50)
print("🙏 Drawing Sacred Shivalingam 🙏")
print("=" * 50)

draw_blue_glow()
draw_base_glow()
draw_bottom_base()
draw_middle_pedestal()
draw_yoni()
draw_spout()
draw_lingam()
draw_tripundra()

pen.hideturtle()
screen.update()

print("\n" + "=" * 50)
print("🙏 Cycling through Shiva Namalu...")
print("Press ESC to close at any time.")
print("=" * 50 + "\n")

try:
    cycle_namalu()
except turtle.Terminator:
    pass

try:
    screen.mainloop()
except turtle.Terminator:
    pass