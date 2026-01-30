import math

class AsciiArtGenerator:
    def __init__(self, width=80, height=60):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def draw_circle(self, center_x, center_y, radius, char='.', thickness=1, fill=False):
        for y in range(self.height):
            for x in range(self.width):
                dist = self.distance(x, y, center_x, center_y)
                
                if fill:
                    if dist <= radius:
                        self.canvas[y][x] = char
                else:
                    if abs(dist - radius) <= thickness:
                        self.canvas[y][x] = char
    
    def draw_ellipse(self, center_x, center_y, radius_x, radius_y, char=':', thickness=1, fill=False):
        for y in range(self.height):
            for x in range(self.width):
                normalized_dist = ((x - center_x)**2 / radius_x**2) + ((y - center_y)**2 / radius_y**2)
                
                if fill:
                    if normalized_dist <= 1:
                        self.canvas[y][x] = char
                else:
                    if abs(normalized_dist - 1) <= thickness / min(radius_x, radius_y):
                        self.canvas[y][x] = char
    
    def draw_filled_circle(self, center_x, center_y, radius, char='*'):
        self.draw_circle(center_x, center_y, radius, char, fill=True)
    
    def shade_region(self, center_x, center_y, inner_radius, outer_radius, char='-'):
        for y in range(self.height):
            for x in range(self.width):
                dist = self.distance(x, y, center_x, center_y)
                if inner_radius <= dist <= outer_radius:
                    if self.canvas[y][x] == ' ':
                        self.canvas[y][x] = char
    
    def draw_gradient_circle(self, center_x, center_y, radius, chars=['.', ':', '-', '=', '+', '*', '#', '@']):
        for y in range(self.height):
            for x in range(self.width):
                dist = self.distance(x, y, center_x, center_y)
                
                if dist <= radius:
                    ratio = dist / radius
                    char_index = int(ratio * (len(chars) - 1))
                    char_index = min(char_index, len(chars) - 1)
                    
                    if self.canvas[y][x] == ' ':
                        self.canvas[y][x] = chars[char_index]
    
    def clear_circle(self, center_x, center_y, radius):
        for y in range(self.height):
            for x in range(self.width):
                dist = self.distance(x, y, center_x, center_y)
                if dist <= radius:
                    self.canvas[y][x] = ' '
    
    def draw_line(self, x1, y1, x2, y2, char='-', thickness=1):
        for y in range(self.height):
            for x in range(self.width):
                if x2 - x1 == 0:
                    dist = abs(x - x1)
                else:
                    A = y2 - y1
                    B = x1 - x2
                    C = x2 * y1 - x1 * y2
                    dist = abs(A * x + B * y + C) / math.sqrt(A**2 + B**2)
                    
                    min_x, max_x = min(x1, x2), max(x1, x2)
                    min_y, max_y = min(y1, y2), max(y1, y2)
                    
                    if not (min_x - thickness <= x <= max_x + thickness and 
                           min_y - thickness <= y <= max_y + thickness):
                        continue
                
                if dist <= thickness:
                    self.canvas[y][x] = char
    
    def render(self):
        return '\n'.join([''.join(row) for row in self.canvas])
    
    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.render())


def create_character_art():
    art = AsciiArtGenerator(width=100, height=80)
    
    head_center_x, head_center_y = 50, 30
    head_radius = 24
    
    art.draw_gradient_circle(head_center_x, head_center_y, head_radius, 
                            chars=[' ', ' ', '.', '.', ':', ':', '-', '-', '='])
    
    art.draw_circle(head_center_x, head_center_y, head_radius, char='@', thickness=1.5)
    art.draw_circle(head_center_x, head_center_y, head_radius - 1, char='#', thickness=1)
    art.draw_circle(head_center_x, head_center_y, head_radius - 2, char='=', thickness=0.5)
    
    art.draw_circle(head_center_x, head_center_y - head_radius + 6, 9, char=':', thickness=1.2)
    art.draw_circle(head_center_x - 10, head_center_y - head_radius + 9, 7, char=':', thickness=1)
    art.draw_circle(head_center_x + 10, head_center_y - head_radius + 9, 7, char=':', thickness=1)
    
    left_eye_x, left_eye_y = head_center_x - 9, head_center_y - 4
    
    art.draw_circle(left_eye_x, left_eye_y, 4.5, char='o', thickness=1)
    art.draw_filled_circle(left_eye_x, left_eye_y, 4, char='.')
    
    art.draw_filled_circle(left_eye_x, left_eye_y, 3, char='*')
    art.draw_circle(left_eye_x, left_eye_y, 3, char='#', thickness=0.8)
    
    art.draw_filled_circle(left_eye_x, left_eye_y, 1.5, char='@')
    
    if left_eye_y - 1 >= 0 and left_eye_x - 1 >= 0:
        art.canvas[left_eye_y - 1][left_eye_x - 1] = 'o'
        art.canvas[left_eye_y - 1][left_eye_x] = '.'
    
    right_eye_x, right_eye_y = head_center_x + 9, head_center_y - 4
    
    art.draw_circle(right_eye_x, right_eye_y, 4.5, char='o', thickness=1)
    art.draw_filled_circle(right_eye_x, right_eye_y, 4, char='.')
    
    art.draw_filled_circle(right_eye_x, right_eye_y, 3, char='*')
    art.draw_circle(right_eye_x, right_eye_y, 3, char='#', thickness=0.8)
    
    art.draw_filled_circle(right_eye_x, right_eye_y, 1.5, char='@')
    
    if right_eye_y - 1 >= 0 and right_eye_x - 1 >= 0:
        art.canvas[right_eye_y - 1][right_eye_x - 1] = 'o'
        art.canvas[right_eye_y - 1][right_eye_x] = '.'
    
    art.draw_ellipse(left_eye_x, left_eye_y - 6, 5, 1.5, char='=', thickness=0.8)
    art.draw_ellipse(right_eye_x, right_eye_y - 6, 5, 1.5, char='=', thickness=0.8)
    
    nose_x, nose_y = head_center_x, head_center_y + 5
    
    art.draw_circle(nose_x, nose_y + 2, 2, char='o', thickness=0.8)
    art.canvas[nose_y + 2][nose_x] = 'U'
    
    if nose_y + 3 < art.height:
        if nose_x - 2 >= 0:
            art.canvas[nose_y + 3][nose_x - 2] = '('
        if nose_x + 2 < art.width:
            art.canvas[nose_y + 3][nose_x + 2] = ')'
    
    mouth_x, mouth_y = head_center_x, head_center_y + 12
    
    art.draw_ellipse(mouth_x, mouth_y - 1, 7, 2, char='-', thickness=0.6)
    
    art.draw_ellipse(mouth_x, mouth_y + 2, 8, 3, char='=', thickness=0.9)
    
    if mouth_y < art.height and mouth_x - 7 >= 0 and mouth_x + 7 < art.width:
        art.canvas[mouth_y][mouth_x - 7] = '('
        art.canvas[mouth_y][mouth_x + 7] = ')'
    
    for offset in range(-6, 7):
        x = mouth_x + offset
        if 0 <= x < art.width and mouth_y + 1 < art.height:
            if art.canvas[mouth_y + 1][x] == ' ':
                art.canvas[mouth_y + 1][x] = '_'
    
    art.draw_circle(head_center_x - 15, head_center_y + 6, 3.5, char=':', thickness=1.2)
    art.shade_region(head_center_x - 15, head_center_y + 6, 0, 2.5, char='.')
    
    art.draw_circle(head_center_x + 15, head_center_y + 6, 3.5, char=':', thickness=1.2)
    art.shade_region(head_center_x + 15, head_center_y + 6, 0, 2.5, char='.')
    
    body_x, body_y = head_center_x, head_center_y + head_radius + 20
    art.draw_ellipse(body_x, body_y, 26, 24, char='#', thickness=1.8)
    art.draw_ellipse(body_x, body_y, 25, 23, char='=', thickness=1.2)
    art.draw_ellipse(body_x, body_y, 24, 22, char='-', thickness=0.8)
    art.shade_region(body_x, body_y, 0, 22, char='.')
    art.shade_region(body_x, body_y, 0, 18, char=':')
    art.shade_region(body_x, body_y, 0, 14, char='-')
    
    art.draw_line(body_x - 22, body_y - 8, body_x - 32, body_y + 6, char='=', thickness=1.8)
    art.draw_line(body_x + 22, body_y - 8, body_x + 32, body_y + 6, char='=', thickness=1.8)
    
    return art


def main():
    print("Generating ASCII art using distance formulas and geometric shapes...\n")
    
    character = create_character_art()
    
    result = character.render()
    print(result)
    
    output_file = "ascii_character_output.txt"
    character.save_to_file(output_file)
    print(f"\n\nASCII art saved to: {output_file}")
    
  


if __name__ == "__main__":
    main()
