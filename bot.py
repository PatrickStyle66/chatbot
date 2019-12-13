import aiml

kernel = aiml.Kernel()
kernel.learn("brain.xml")
while True: print("bot> " + kernel.respond(input("user> ")))