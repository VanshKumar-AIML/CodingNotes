import turtle
import time
import math
import random
import colorsys

# -------------------------
#  Configuration
# -------------------------
WIDTH, HEIGHT = 800, 800
FPS = 60
FRAME_TIME = 1.0 / FPS

# -------------------------
#  Screen & Pens
# -------------------------
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("I Love You Forever — Soft Glow Heart")
screen.bgcolor("black")
screen.tracer(0, 0)  # manual updates for smooth animation
screen.colormode(1.0)  # use 0..1 floats for RGB

# main drawing pen (heart)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

# overlay pen for glow layers (reused)
glow_pen = turtle.Turtle()
glow_pen.hideturtle()
glow_pen.speed(0)
glow_pen.pensize(1)

# text pen
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.speed(0)
text_pen.penup()
text_pen.color("white")

# small hearts pen (for floating hearts)
mini_pen = turtle.Turtle()
mini_pen.hideturtle()
mini_pen.speed(0)
mini_pen.penup()

# particle pen
part_pen = turtle.Turtle()
part_pen.hideturtle()
part_pen.speed(0)
part_pen.penup()

# -------------------------
# Heart path generator
# -------------------------
def heart_path_points(scale=1.0, steps=400):
    """
    Return a list of points approximating a heart shape centered at (0,0).
    The shape is drawn using the same approach as classic turtle hearts.
    """
    # We'll generate using parametric heart curve for a smooth outline:
    pts = []
    for t in [i * (2 * math.pi / steps) for i in range(steps + 1)]:
        # classic cardioid-like parametric heart
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((x * scale, y * scale))
    # normalize and scale to comfortable pixel size
    # find max absolute
    max_abs = max(max(abs(x), abs(y)) for x, y in pts)
    if max_abs == 0:
        return pts
    target = 8 * 12 * scale  # roughly ~960/80 scaling baseline
    factor = target / max_abs
    return [(x * factor, y * factor) for x, y in pts]

# Precompute base points (scale = 1)
BASE_POINTS = heart_path_points(scale=1.0, steps=600)

# -------------------------
# Drawing helpers
# -------------------------
def draw_filled_path(turtle_obj, points, fill_color, pen_color=None):
    turtle_obj.penup()
    if not points:
        return
    turtle_obj.goto(points[0])
    turtle_obj.pendown()
    if pen_color:
        turtle_obj.color(pen_color)
    else:
        turtle_obj.color(fill_color)
    turtle_obj.begin_fill()
    for x, y in points[1:]:
        turtle_obj.goto(x, y)
    turtle_obj.end_fill()
    turtle_obj.penup()

def scaled_points(points, cx=0, cy=0, scale=1.0, dx=0, dy=0):
    return [((x * scale) + cx + dx, (y * scale) + cy + dy) for x, y in points]

# -------------------------
# Particles & floating hearts
# -------------------------
particles = []  # each: [x, y, vx, vy, life, size, hue]
mini_hearts = []  # each: [x, y, vy, start_size, age, hue, drift_phase]

def spawn_particle(x, y, hue, count=6):
    for _ in range(count):
        ang = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.6, 2.6)
        vx = math.cos(ang) * speed
        vy = math.sin(ang) * speed
        life = random.uniform(0.6, 1.6)
        size = random.uniform(1.0, 3.6)
        particles.append([x, y, vx, vy, life, size, hue])

def spawn_mini_heart():
    # spawn near top half, drift upward from around center
    x = random.uniform(-160, 160)
    y = -40 + random.uniform(20, 100)
    vy = random.uniform(0.2, 0.9)
    start_size = random.uniform(0.08, 0.18)
    hue = random.uniform(0.95, 0.02)  # pinkish-red region (wrap allowed)
    phase = random.uniform(0, 2 * math.pi)
    mini_hearts.append([x, y, vy, start_size, 0.0, hue, phase])

# -------------------------
# Rainbow helper
# -------------------------
def hue_to_rgb(h):
    # expects h in 0..1
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, 0.9, 0.95)
    return (r, g, b)

# -------------------------
# Typing message
# -------------------------
message = "I Love You Forever"
typed_chars = 0
typing_timer = 0.0
typing_interval = 0.08  # seconds per character

def update_typing(dt):
    global typed_chars, typing_timer
    typing_timer += dt
    while typing_timer >= typing_interval and typed_chars < len(message):
        typed_chars += 1
        typing_timer -= typing_interval

def draw_typing_text():
    text_pen.clear()
    text_pen.goto(0, 230)
    text_pen.write(message[:typed_chars], align="center", font=("Arial", 26, "bold"))

# -------------------------
# Heart draw (glow layers)
# -------------------------
def draw_glowing_heart(center_x, center_y, base_scale, hue, intensity):
    """
    Draw multiple layers from faint large to bright small to simulate a soft glow.
    intensity: 0..1 controls brightness
    hue: 0..1 rainbow hue
    """
    # glow layers (larger faint layers first)
    glow_pen.penup()
    n_layers = 6
    for i in range(n_layers, 0, -1):
        s = base_scale * (1.0 + i * 0.022 * (1 + intensity))
        alpha_factor = (i / n_layers) * (0.25 + 0.75 * intensity)  # simulated brightness
        # make hue slightly shift across layers for gentle rainbow
        layer_h = hue + (i - n_layers/2) * 0.01
        r, g, b = hue_to_rgb(layer_h)
        # simulate softer color by mixing with black via lower saturation (we can't alpha)
        glow_pen.color((r * alpha_factor, g * alpha_factor, b * alpha_factor))
        pts = scaled_points(BASE_POINTS, cx=center_x, cy=center_y, scale=s)
        draw_filled_path(glow_pen, pts, fill_color=(r, g, b))

    # solid core
    r, g, b = hue_to_rgb(hue)
    pen.color((r, g, b), (min(1, r + 0.2), min(1, g + 0.12), min(1, b + 0.12)))
    pen.pensize(2 + intensity * 2)
    core_pts = scaled_points(BASE_POINTS, cx=center_x, cy=center_y, scale=base_scale * (0.98 - 0.02 * intensity))
    draw_filled_path(pen, core_pts, fill_color=(r, g, b), pen_color=None)

# -------------------------
# Update & render loop
# -------------------------
def update(dt, t):
    # 1) breathing and hue (gentle rainbow wave)
    beat = (math.sin(t * 1.6) + 1) / 2  # 0..1, slower smooth breathing
    scale = 0.95 + beat * 0.22
    hue = (t * 0.02) % 1.0  # slow rainbow rotation
    intensity = 0.45 + 0.55 * beat  # glow intensity

    # 2) spawn particles occasionally on beat peaks
    if random.random() < 0.6 * (0.5 + beat):
        # spawn from near tip of heart (approx bottom)
        spawn_particle(0, -220 * scale, hue, count=random.randint(4, 10))

    # occasionally spawn mini hearts
    if random.random() < 0.03:
        spawn_mini_heart()

    # update particles
    for p in particles[:]:
        p[0] += p[2]  # x += vx
        p[1] += p[3]  # y += vy
        p[3] -= 0.02  # gravity-like slow down upward particles
        p[4] -= dt    # life decreases
        p[5] *= 0.995  # size slowly shrinks
        p[6] += 0.002  # hue shift for color fade
        if p[4] <= 0 or p[5] < 0.3:
            particles.remove(p)

    # update mini hearts
    for m in mini_hearts[:]:
        m[1] += m[2]  # y += vy
        m[3] *= 1.0005  # slight growth
        m[4] += dt     # age
        m[6] += dt * 2.0  # drift phase
        m[0] += math.sin(m[6]) * 0.3  # horizontal drift
        if m[4] > 6.0 or m[1] > HEIGHT / 2 + 40:
            mini_hearts.remove(m)

    # typing update
    update_typing(dt)

    # draw everything (clear per-frame)
    pen.clear()
    glow_pen.clear()
    part_pen.clear()
    mini_pen.clear()
    text_pen.clear()

    # draw glow heart at center
    draw_glowing_heart(center_x=0, center_y=-40, base_scale=scale * 6.0, hue=hue, intensity=intensity)

    # draw particles
    for p in particles:
        x, y, vx, vy, life, size, ph = p
        alpha = max(0.0, life / 1.6)
        r, g, b = hue_to_rgb(ph)
        part_pen.goto(x, y)
        # simulated fade by dimming color
        part_pen.dot(max(1, size * 2.2), (r * alpha, g * alpha, b * alpha))

    # draw mini hearts
    for m in mini_hearts:
        x, y, vy, start_size, age, hue_m, ph = m
        s = start_size * (1.0 + 0.3 * math.sin(age * 2.0))
        pts = scaled_points(BASE_POINTS, cx=x, cy=y - 50, scale=s * 6.0)
        r, g, b = hue_to_rgb(hue_m)
        # a tiny bright core and a softer outer to simulate glow
        mini_pen.color((max(0.6, r), max(0.2, g), max(0.2, b)))
        draw_filled_path(mini_pen, pts, fill_color=(r, g, b))

    # draw typed text
    draw_typing_text()

# -------------------------
# Run loop
# -------------------------
def main_loop():
    t0 = time.time()
    t = 0.0
    try:
        while True:
            now = time.time()
            dt = now - t0
            # cap dt for stability
            if dt > 0.1:
                dt = 0.1
            t += dt
            update(dt, t)
            screen.update()
            t0 = now
            time.sleep(max(0.0, FRAME_TIME - (time.time() - now)))
    except turtle.Terminator:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    # pre-seed a few mini hearts and particles for immediate visual interest
    for _ in range(6):
        spawn_mini_heart()
    for _ in range(40):
        spawn_particle(random.uniform(-80, 80), random.uniform(-120, -40), random.uniform(0.95, 0.05), count=1)
    main_loop()