from graph import run_pipeline, Agentstate
from utils.print_helpers import pretty_print

if __name__ == "__main__":
    print("==="*3 + " Smart Workplace Assistant — interactive mode " + "==="*3)
    while True:
        user = input("You >>")
        if user.lower() in ["exit", "quit", "q"]:
            print("Exiting the assistant. Goodbye!")
            break

        state = run_pipeline(Agentstate(user_inputs=user))

        pretty_print(state)
        print("\n" + "==="*20 + "\n")