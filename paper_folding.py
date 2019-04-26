thickness = 0.05

for i in range(103):
    thickness = thickness * 2
    print(f"folded {i+1} time(s): {thickness/1000}m thick")