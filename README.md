# ASCII Art Generator - Winter PEP Class Project

## 🎓 Project Overview

This project was developed as part of my **Winter PEP (Python Enhancement Program)** class, focusing on mastering **conditional statements** and **loops** in Python. The project demonstrates how fundamental programming concepts can be used to create complex visual outputs through ASCII art generation.

---

## 📚 Learning Objectives: Conditional Statements & Loops

### **Conditional Statements (if-elif-else)**

Conditional statements allow programs to make decisions based on specific conditions. They control the flow of execution by evaluating boolean expressions.

**Syntax:**
```python
if condition1:
    # Execute if condition1 is True
elif condition2:
    # Execute if condition1 is False and condition2 is True
else:
    # Execute if all conditions are False
```

**Key Concepts:**
- **Boolean Expressions**: Expressions that evaluate to `True` or `False`
- **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical Operators**: `and`, `or`, `not`
- **Nested Conditionals**: Conditionals inside other conditionals for complex decision-making

**Real-world Applications:**
- Form validation
- Game logic
- User authentication
- Data filtering

---

### **Loops (for & while)**

Loops enable repetitive execution of code blocks, essential for processing collections and automating tasks.

#### **For Loops**
Used when the number of iterations is known or when iterating over a sequence.

**Syntax:**
```python
for variable in sequence:
    # Execute this block for each item
```

**Common Patterns:**
```python
# Range-based iteration
for i in range(10):
    print(i)

# List iteration
for item in my_list:
    process(item)

# Nested loops for 2D structures
for row in range(height):
    for col in range(width):
        process(row, col)
```

#### **While Loops**
Used when the number of iterations is unknown and depends on a condition.

**Syntax:**
```python
while condition:
    # Execute while condition is True
```

**Key Concepts:**
- **Loop Control**: `break` (exit loop), `continue` (skip iteration)
- **Nested Loops**: Loops within loops for multi-dimensional processing
- **Loop Optimization**: Minimizing iterations for better performance

**Real-world Applications:**
- Image processing
- Game development
- Data analysis
- Pattern generation

---

## 🎨 Project Components

### 1. **ascii_output.py** - Position-Based ASCII Art

This file demonstrates **coordinate-based character placement** using conditional statements and loops.

**How It Works:**
- Uses a 2D coordinate system where each character is placed at specific `(row, col)` positions
- The `get_char(row, col)` function returns the appropriate character for each position
- Characters are positioned using **conditional statements** that check row and column ranges

**Example Logic:**
```python
def get_char(row, col):
    if row == 6:
        if 50 <= col <= 52: 
            return '.'
        return ' '
    elif row == 7:
        if 39 <= col <= 41: 
            return '.'
        if 42 <= col <= 58: 
            return ':'
        if 59 <= col <= 62: 
            return '.'
        return ' '
    # ... more conditions
```

**Key Features:**
- **1573 lines** of precise position-based logic
- Each row is handled by a separate conditional block
- Column ranges determine which character to display
- Creates complex ASCII art through careful coordinate mapping

**Technical Highlights:**
- Demonstrates extensive use of `if-elif-else` chains
- Shows how to map 2D coordinates to visual output
- Illustrates the power of systematic conditional logic

---

### 2. **ascii_art_rock.py** - Mathematical Formula-Based Generation

This file uses **mathematical formulas and distance calculations** to generate ASCII art programmatically.

**How It Works:**
- Uses the `generate_char(row, col)` function with mathematical conditions
- Employs distance formulas, geometric shapes, and mathematical relationships
- Creates art through algorithmic pattern generation rather than hardcoded positions

**Example Approach:**
```python
def generate_char(row, col):
    # Calculate distance from center
    center_x, center_y = 50, 30
    distance = sqrt((col - center_x)**2 + (row - center_y)**2)
    
    # Use mathematical conditions
    if distance < 10:
        return '@'
    elif distance < 20:
        return '#'
    # ... more formula-based conditions
```

**Key Features:**
- **2961 lines** of formula-driven logic
- Uses mathematical relationships to determine character placement
- More flexible and scalable than hardcoded positions
- Demonstrates advanced conditional logic with calculations

**Technical Highlights:**
- Combines loops with mathematical formulas
- Shows how geometry can be represented in ASCII
- Illustrates algorithmic thinking in art generation

---

### 3. **dynamic_ascii_art.py** - Object-Oriented Dynamic Generation

This file showcases **advanced programming techniques** using classes and methods to create dynamic ASCII art.

**Architecture:**

#### **AsciiArtGenerator Class**
A comprehensive class that provides tools for creating ASCII art programmatically.

**Core Methods:**

1. **`__init__(width, height)`**
   - Initializes a 2D canvas (list of lists)
   - Sets up the drawing area dimensions
   - Creates empty space filled with spaces

2. **`distance(x1, y1, x2, y2)`**
   - Calculates Euclidean distance between two points
   - Formula: `√[(x2-x1)² + (y2-y1)²]`
   - Used for circle and shape detection

3. **`draw_circle(center_x, center_y, radius, char, thickness, fill)`**
   - Draws circles using distance calculations
   - **Loop Logic**: Iterates through every canvas position
   - **Conditional Logic**: Checks if point is on circle perimeter or inside
   ```python
   for y in range(self.height):
       for x in range(self.width):
           dist = self.distance(x, y, center_x, center_y)
           if abs(dist - radius) <= thickness:
               self.canvas[y][x] = char
   ```

4. **`draw_ellipse(center_x, center_y, radius_x, radius_y, char, thickness, fill)`**
   - Creates elliptical shapes using normalized distance
   - Formula: `(x-cx)²/rx² + (y-cy)²/ry² = 1`
   - Demonstrates mathematical shape generation

5. **`draw_filled_circle(center_x, center_y, radius, char)`**
   - Fills entire circular area with character
   - Uses `fill=True` parameter in draw_circle

6. **`shade_region(center_x, center_y, inner_radius, outer_radius, char)`**
   - Creates gradient effects between two radii
   - **Conditional Logic**: `if inner_radius <= dist <= outer_radius`
   - Only fills empty spaces to preserve existing art

7. **`draw_gradient_circle(center_x, center_y, radius, chars)`**
   - Creates depth effect using character gradients
   - **Loop Logic**: Calculates distance ratio for each point
   - **Conditional Selection**: Chooses character based on distance
   ```python
   ratio = dist / radius
   char_index = int(ratio * (len(chars) - 1))
   ```

8. **`clear_circle(center_x, center_y, radius)`**
   - Erases circular areas
   - Useful for creating negative space

9. **`draw_line(x1, y1, x2, y2, char, thickness)`**
   - Draws lines using point-to-line distance formula
   - Handles vertical and diagonal lines
   - Uses bounding box optimization

10. **`render()`**
    - Converts 2D canvas array to string output
    - **Nested Loops**: Joins each row, then joins all rows
    ```python
    return '\n'.join([''.join(row) for row in self.canvas])
    ```

11. **`save_to_file(filename)`**
    - Exports ASCII art to text file
    - Preserves formatting with UTF-8 encoding

#### **create_character_art() Function**
Demonstrates how to use the class to create a complete character face.

**Features Created:**
- **Head**: Gradient circle with multiple border layers
- **Hair**: Overlapping circles for texture
- **Eyes**: Nested circles with highlights and pupils
- **Eyebrows**: Elliptical shapes
- **Nose**: Small circle with custom character
- **Mouth**: Elliptical smile with underline
- **Cheeks**: Shaded circular regions
- **Body**: Large ellipse with gradient shading
- **Arms**: Lines extending from body

**Loop & Conditional Usage:**
```python
# Example: Creating gradient head
art.draw_gradient_circle(head_center_x, head_center_y, head_radius, 
                        chars=[' ', ' ', '.', '.', ':', ':', '-', '-', '='])

# Example: Drawing multiple border layers
art.draw_circle(head_center_x, head_center_y, head_radius, char='@', thickness=1.5)
art.draw_circle(head_center_x, head_center_y, head_radius - 1, char='#', thickness=1)
art.draw_circle(head_center_x, head_center_y, head_radius - 2, char='=', thickness=0.5)

# Example: Conditional boundary checking
if mouth_y < art.height and mouth_x - 7 >= 0 and mouth_x + 7 < art.width:
    art.canvas[mouth_y][mouth_x - 7] = '('
    art.canvas[mouth_y][mouth_x + 7] = ')'
```

**Technical Highlights:**
- **Object-Oriented Programming**: Encapsulates functionality in a class
- **Method Chaining**: Multiple drawing operations on same canvas
- **Layering**: Builds complex images from simple shapes
- **Mathematical Precision**: Uses formulas for accurate shape rendering
- **Boundary Checking**: Prevents array index errors with conditionals

---

## 🔧 How Loops & Conditionals Power This Project

### **Nested Loops for 2D Canvas Processing**
Every drawing method uses nested loops to iterate through the entire canvas:
```python
for y in range(self.height):      # Outer loop: rows
    for x in range(self.width):   # Inner loop: columns
        # Process each pixel position
```

### **Conditional Logic for Shape Detection**
Mathematical conditions determine what character to place:
```python
if distance <= radius:                    # Inside circle
    canvas[y][x] = char
elif abs(distance - radius) <= thickness: # On circle edge
    canvas[y][x] = char
```

### **Range-Based Conditionals**
Position-based files use range checks extensively:
```python
if 50 <= col <= 52:  # Column range check
    return '.'
```

### **Logical Operators**
Combine multiple conditions for complex shapes:
```python
if inner_radius <= dist <= outer_radius and canvas[y][x] == ' ':
    canvas[y][x] = char
```

---

## 🚀 Running the Programs

### **ascii_output.py**
```bash
python ascii_output.py
```
Generates a static ASCII art image using position-based logic.

### **ascii_art_rock.py**
```bash
python ascii_art_rock.py
```
Creates ASCII art using mathematical formulas and geometric patterns.

### **dynamic_ascii_art.py**
```bash
python dynamic_ascii_art.py
```
Generates a dynamic character face and saves it to `ascii_character_output.txt`.

---

## 📊 Project Statistics

| File | Lines of Code | Primary Technique | Complexity |
|------|---------------|-------------------|------------|
| `ascii_output.py` | 1,573 | Position-based conditionals | High |
| `ascii_art_rock.py` | 2,961 | Formula-based generation | Very High |
| `dynamic_ascii_art.py` | 208 | OOP with geometric methods | Advanced |

---

## 🎯 Key Learning Outcomes

Through this project, I have demonstrated mastery of:

1. **Conditional Statements**
   - Complex if-elif-else chains
   - Nested conditionals
   - Range-based conditions
   - Logical operator combinations

2. **Loops**
   - Nested for loops for 2D iteration
   - Range-based iteration
   - Loop optimization techniques
   - Iterating over data structures

3. **Advanced Concepts**
   - 2D coordinate systems
   - Mathematical formula application
   - Object-oriented programming
   - Algorithm design
   - Code organization and modularity

4. **Problem-Solving Skills**
   - Breaking complex problems into smaller parts
   - Systematic approach to pattern generation
   - Debugging multi-layered logic
   - Optimizing performance

---

## 🎨 Visual Output Examples

The programs generate various ASCII art outputs including:
- Complex character faces with detailed features
- Geometric patterns and shapes
- Gradient effects using character density
- Layered compositions with depth

---

## 🔮 Future Enhancements

Potential improvements for this project:
- Animation support with frame-by-frame generation
- Color support using ANSI escape codes
- Interactive drawing tools
- Image-to-ASCII conversion
- Real-time preview GUI
- Export to different formats (HTML, SVG)

---

## 📝 Conclusion

This project demonstrates how fundamental programming concepts—**conditional statements** and **loops**—can be combined to create sophisticated visual outputs. By exploring three different approaches (position-based, formula-based, and object-oriented), I've gained a comprehensive understanding of how these core concepts apply to real-world programming challenges.

The progression from simple position-based logic to advanced mathematical generation showcases the power and flexibility of Python's control structures, proving that even basic programming concepts can produce remarkable results when applied creatively.

---

## 👨‍💻 Author

**Suman**  
Winter PEP Class Project - 2026  
Topic: Conditional Statements and Loops in Python

---

## 📄 License

This project is created for educational purposes as part of the Winter PEP class curriculum.
