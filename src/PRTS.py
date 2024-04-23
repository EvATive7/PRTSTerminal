import subprocess

def execute_command(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout

def main():
    while True:
        user_input = input("RHODES ISLAND Terminal >> ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        commands = user_input.split("|")

        previous_output = None
        for cmd in commands:
            cmd_parts = cmd.strip().split()
            if previous_output:
                cmd_parts[0] = previous_output
            output = execute_command(" ".join(cmd_parts))
            print(output.strip())
            previous_output = output

if __name__ == "__main__":
    main()
