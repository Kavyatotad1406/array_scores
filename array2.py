import sys

# Check if user gave arguments
if len(sys.argv) > 1:
    scores = sys.argv[1:]
    print("User provided scores:")
else:
    print("No input given - using default scores:")
    scores = ["80", "90", "75", "88"]

# Convert scores to numbers
scores = [float(x) for x in scores]

# Calculate values (main branch features)
total = sum(scores)
average = total / len(scores)

# Print results
print("Scores =", scores)
print("Sum =", total)
print("Average =", average)
