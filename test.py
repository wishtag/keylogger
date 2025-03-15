import hashlib

def generate_color_from_name(name):
  """Generates an RGB color tuple from a string name.

  Args:
    name: The string name to generate a color from.

  Returns:
    A tuple of three integers representing the RGB color
    (e.g., (255, 0, 0) for red).
  """
  hashed_name = hashlib.md5(name.encode('utf-8')).hexdigest()
  r = int(hashed_name[0:2], 16)
  g = int(hashed_name[2:4], 16)
  b = int(hashed_name[4:6], 16)
  return (r, g, b)

# Example usage:
name = "example name"
color = generate_color_from_name(name)
print(f"The color for '{name}' is: {color}")

name2 = "acryl"
color2 = generate_color_from_name(name2)
print(f"The color for '{name2}' is: {color2}")