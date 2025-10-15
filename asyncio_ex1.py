import asyncio
async def perform_task(name, delay):
#""" Simulates a task that takes some time to complete. """
    print(f"Task {name} started, will take {delay} seconds.")
    await asyncio.sleep(delay) # Simulates a non-blocking delay
    print(f"Task {name} completed after {delay} seconds.")
    return f"Result from Task {name}"
async def main():
# Create individual coroutines
    task1 = perform_task("A", 3)
    task2 = perform_task("B", 2)
    task3 = perform_task("C", 1)
    print("\n--- Using asyncio.gather ---")
    # Use asyncio.gather to run all tasks concurrently
    results = await asyncio.gather(task1, task2, task3)
    print("Results from asyncio.gather:", results)
    print("\n--- Using asyncio.create_task ---")
    # Use asyncio.create_task to schedule tasks and manage them independently
    task4 = asyncio.create_task(perform_task("D", 4))
    task5 = asyncio.create_task(perform_task("E", 2))
    print("Tasks D and E started.")
    # Wait for the tasks to complete
    await task4
    await task5
# Run the asyncio event loop
asyncio.run(main())