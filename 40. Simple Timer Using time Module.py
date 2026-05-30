import time

print("Starting timer...")
start_time = time.time()
time.sleep(2) # Pauses program for 2 seconds
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")