prep_times = [24, 31, 18, 40, 26, 22, 35]

print("=== Restaurant Performance Dashboard ===")

print("Fastest order :", min(prep_times), "minutes")
print("Slowest order :", max(prep_times), "minutes")
print("Total time    :", sum(prep_times), "minutes")
print("Orders today  :", len(prep_times))

average = sum(prep_times) / len(prep_times)

print("Average time  :", round(average, 2), "minutes")
print("Sorted times  :", sorted(prep_times))