import pygame
import mido

# Start pygame
pygame.init()

# Create MIDI output
outport = mido.open_output()

# Klavye girişi için Pygame ekranı oluştur
screen = pygame.display.set_mode((1800, 400))

# Title
pygame.display.set_caption('Keyboard to MIDI')

# Font set
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

# Note matching
note_mapping = {
    pygame.K_F1: 48,  # C3
    pygame.K_F2: 50,  # D3
    pygame.K_F3: 52,  # E3
    pygame.K_F4: 53,  # F3
    pygame.K_F5: 55,  # G3
    pygame.K_F6: 57,  # A3
    pygame.K_F7: 59,  # B3
    pygame.K_1: 60,  # C4
    pygame.K_2: 61,  # C#4/Db4
    pygame.K_3: 62,  # D4
    pygame.K_4: 63,  # D#4/Eb4
    pygame.K_5: 64,  # E4
    pygame.K_6: 65,  # F4
    pygame.K_7: 66,  # F#4/Gb4
    pygame.K_q: 67,  # G4
    pygame.K_w: 68,  # G#4/Ab4
    pygame.K_e: 69,  # A4
    pygame.K_r: 70,  # A#4/Bb4
    pygame.K_t: 71,  # B4
    pygame.K_y: 72,  # C5
    pygame.K_u: 73,  # C#5/Db5
    pygame.K_o: 74,  # D5
    pygame.K_a: 75,  # D#5/Eb5
    pygame.K_s: 76,  # E5
    pygame.K_d: 77,  # F5
    pygame.K_f: 78,  # F#5/Gb5
    pygame.K_g: 79,  # G5
    pygame.K_h: 80,  # G#5/Ab5
    pygame.K_j: 81,  # A5
    pygame.K_k: 82,  # A#5/Bb5
    pygame.K_l: 83,  # B5
    pygame.K_i: 84,  # C6
    pygame.K_z: 85,  # C#6/Db6
    pygame.K_x: 86,  # D6
    pygame.K_c: 87,  # D#6/Eb6
    pygame.K_v: 88,  # E6
    pygame.K_b: 89,  # F6
    pygame.K_n: 90,  # F#6/Gb6
    pygame.K_m: 91,  # G6
}

# Note names
note_names = {
    48: "C3",
    50: "D3",
    52: "E3",
    53: "F3",
    55: "G3",
    57: "A3",
    59: "B3",
    60: "C4",
    61: "C#4/Db4",
    62: "D4",
    63: "D#4/Eb4",
    64: "E4",
    65: "F4",
    66: "F#4/Gb4",
    67: "G4",
    68: "G#4/Ab4",
    69: "A4",
    70: "A#4/Bb4",
    71: "B4",
    72: "C5",
    73: "C#5/Db5",
    74: "D5",
    75: "D#5/Eb5",
    76: "E5",
    77: "F5",
    78: "F#5/Gb5",
    79: "G5",
    80: "G#5/Ab5",
    81: "A5",
    82: "A#5/Bb5",
    83: "B5",
    84: "C6",
    85: "C#6/Db6",
    86: "D6",
    87: "D#6/Eb6",
    88: "E6",
    89: "F6",
    90: "F#6/Gb6",
    91: "G6",
}

# key names
key_names = {
    pygame.K_F1: "F1",
    pygame.K_F2: "F2",
    pygame.K_F3: "F3",
    pygame.K_F4: "F4",
    pygame.K_F5: "F5",
    pygame.K_F6: "F6",
    pygame.K_F7: "F7",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_q: "Q",
    pygame.K_w: "W",
    pygame.K_e: "E",
    pygame.K_r: "R",
    pygame.K_t: "T",
    pygame.K_y: "Y",
    pygame.K_u: "U",
    pygame.K_o: "O",
    pygame.K_a: "A",
    pygame.K_s: "S",
    pygame.K_d: "D",
    pygame.K_f: "F",
    pygame.K_g: "G",
    pygame.K_h: "H",
    pygame.K_j: "J",
    pygame.K_k: "K",
    pygame.K_l: "L",
    pygame.K_i: "I",
    pygame.K_z: "Z",
    pygame.K_x: "X",
    pygame.K_c: "C",
    pygame.K_v: "V",
    pygame.K_b: "B",
    pygame.K_n: "N",
    pygame.K_m: "M",
}

# dictionary to following pressed keys
key_states = {key: False for key in note_mapping.keys()}

# volume
velocity = 127  # 0-127 arasında bir değer

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in note_mapping:
                note = note_mapping[event.key]
                msg = mido.Message('note_on', note=note, velocity=velocity)
                outport.send(msg)
                key_states[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in note_mapping:
                note = note_mapping[event.key]
                msg = mido.Message('note_off', note=note)
                outport.send(msg)
                key_states[event.key] = False


    screen.fill((0, 0, 0))

    # screen buttons
    x = 20
    y = 20
    for key, note in note_mapping.items():
        key_name = key_names.get(key, "Unknown")
        note_name = note_names.get(note, "Unknown")
        text_surface = font.render(f"{key_name}: {note_name}", True, (255, 255, 255))

        # Background
        if key_states[key]:
            rect_color = (100, 100, 255)  # active button
        else:
            rect_color = (50, 50, 50)  # passive button

        rect_width = text_surface.get_width() + 10
        rect_height = text_surface.get_height() + 10
        pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))


        screen.blit(text_surface, (x + 5, y + 5))

        x += rect_width + 20
        if x > screen.get_width() - 200:
            x = 20
            y += rect_height + 20

    pygame.display.flip()

pygame.quit()
