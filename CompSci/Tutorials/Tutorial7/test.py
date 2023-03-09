height = float(input("Enter Height in meters: "))
foot = height / 0.3048
foot_whole = int(foot)
inches = int((foot - foot_whole) * 12)
print(f"{height:.2f} meters is equal to {foot_whole} feet and {inches} inches.")
