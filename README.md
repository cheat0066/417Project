# 417Project

# Piecewise Linear Interpolation of temperature readings

# Sample input
# 61.0 63.0 50.0 58.0
# 80.0 81.0 68.0 77.0
# 62.0 63.0 52.0 60.0
# 83.0 82.0 70.0 79.0
# 68.0 69.0 58.0 65.0

# Input for core 00
# 0   61.0
# 30  80.0
# 60  62.0
# 90  83.0
# 120 68.0

# Output for core 00
# 0 <= x <=        30 ; y =      61.0000 +       0.6333 x ; interpolation
# 30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
# 60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
# 90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation

# Input for core 01
# 0   63.0
# 30  81.0
# 60  63.0
# 90  82.0
# 120 69.0

# Output for core 01
# 0 <= x <=        30 ; y =      63.0000 +       0.6000 x ; interpolation
# 30 <= x <=       60 ; y =      99.0000 +      -0.6000 x ; interpolation
# 60 <= x <=       90 ; y =      25.0000 +       0.6333 x ; interpolation
# 90 <= x <=      120 ; y =     121.0000 +      -0.4333 x ; interpolation

# Input for core 02
# 0   50.0
# 30  68.0
# 60  52.0
# 90  70.0
# 120 58.0

# Output for core 02
# 0 <= x <=        30 ; y =      50.0000 +       0.6000 x ; interpolation
# 30 <= x <=       60 ; y =      84.0000 +      -0.5333 x ; interpolation
# 60 <= x <=       90 ; y =      16.0000 +       0.6000 x ; interpolation
# 90 <= x <=      120 ; y =     106.0000 +      -0.4000 x ; interpolation

# Input for core 03
# 0   58.0
# 30  77.0
# 60  60.0
# 90  79.0
# 120 65.0

# Output for core 03
# 0 <= x <=        30 ; y =      58.0000 +       0.6333 x ; interpolation
# 30 <= x <=       60 ; y =      94.0000 +      -0.5667 x ; interpolation
# 60 <= x <=       90 ; y =      22.0000 +       0.6333 x ; interpolation
# 90 <= x <=      120 ; y =     121.0000 +      -0.4667 x ; interpolation
