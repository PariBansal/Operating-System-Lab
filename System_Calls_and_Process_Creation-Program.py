import os

print("SYSTEM CALLS AND PROCESS CREATION")
print("----------------------------------")

# 1. Create a child process
pid = os.fork()

if pid == 0:
    # CHILD PROCESS

    # 2. Display Process ID and Parent Process ID
    print("\n--- CHILD PROCESS ---")
    print("Child PID:", os.getpid())
    print("Parent PID:", os.getppid())

    # 4. Execute a harmless Linux command
    print("\n--- LINUX COMMAND ---")
    print("Executing harmless Linux command:")
    os.system("echo Hello from child process")

    # 5. Create, write, read and close a test file
    print("\n--- FILE OPERATION ---")

    filename = "test_file.txt"

    # Create and write
    file = open(filename, "w")
    file.write("This is a controlled test file.")
    file.close()

    print("File created and written.")

    # Read
    file = open(filename, "r")
    data = file.read()

    print("File contents:", data)

    # Close
    file.close()
    print("File closed.")

    # 6. Inspect /dev/null
    print("\n--- DEVICE INTERFACE ---")

    device = open("/dev/null", "w")
    print("/dev/null opened successfully.")

    device.write("Test data")

    device.close()
    print("/dev/null closed.")

    # 7. Handle an invalid path
    print("\n--- ERROR HANDLING ---")

    try:
        file = open("/invalid/path/test.txt", "r")
        file.close()

    except FileNotFoundError:
        print("Error handled: Invalid file path.")

    # End child process
    os._exit(0)

else:
    # PARENT PROCESS

    # 2. Display Parent PID and Child PID
    print("\n--- PARENT PROCESS ---")
    print("Parent PID:", os.getpid())
    print("Child PID:", pid)

    # 3. Wait for child process to complete
    print("\nWaiting for child process to complete...")

    child_pid, status = os.waitpid(pid, 0)

    print("Child process completed.")
    print("Returned Child PID:", child_pid)
    print("Exit Status:", status)

    # 8. Evidence summary
    print("\n--- PROGRAM COMPLETE ---")
    print("Process creation: DONE")
    print("PID and PPID: DONE")
    print("Child waiting: DONE")
    print("Linux command: DONE")
    print("File create/write/read/close: DONE")
    print("Device interface: DONE")
    print("Error handling: DONE")