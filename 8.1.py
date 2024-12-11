from collections import defaultdict

def calculate_antinodes(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return [(x1 + 2 * dx, y1 + 2 * dy), (x2 + 2 * (-dx), y2 + 2 * (-dy))]
    
def in_bounds(max_x, max_y, coord):
    return coord[0] <= max_x and coord[0] >= 0 and coord[1] <= max_y and coord[1] >= 0
  
with open("inputs/8.txt", 'r') as file:
    lines = file.readlines()
    max_x = len(lines[0]) - 2
    max_y = len(lines) - 1
    freq_locations = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '\n' and char != '.':
                freq_locations[char].append((x, y))
    
    all_antinodes_by_freq = defaultdict(set)
    for freq in freq_locations:
        coords = freq_locations[freq]
        for idx1 in range(len(coords)):
            for idx2 in range(idx1 + 1, len(coords)):
                coord1 = coords[idx1]
                coord2 = coords[idx2]
                freq_antinodes = calculate_antinodes(coord1[0], coord1[1], coord2[0], coord2[1])
                all_antinodes_by_freq.add(freq_antinodes[0])
                all_antinodes_by_freq.add(freq_antinodes[1])
    
    valid_antinodes = set(filter(lambda coord: in_bounds(max_x, max_y, coord), all_antinodes_by_freq))
    print(len(valid_antinodes))