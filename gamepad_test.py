import pygame
import sys

pygame.init()
pygame.joystick.init()

# Check controller
count = pygame.joystick.get_count()

if count == 0:
    print("❌ No game controller found!")
    print("Please connect your Bluetooth controller first.")
    sys.exit()

print(f"✅ Found {count} controller(s)")

for i in range(count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

    print("\n==============================")
    print("Controller:", joystick.get_name())
    print("Axes:     ", joystick.get_numaxes())
    print("Buttons:  ", joystick.get_numbuttons())
    print("Hats:     ", joystick.get_numhats())
    print("==============================")

joystick = pygame.joystick.Joystick(0)
joystick.init()

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # Controller connected
        if event.type == pygame.JOYDEVICEADDED:
            print("🎮 Controller connected")

        # Controller disconnected
        elif event.type == pygame.JOYDEVICEREMOVED:
            print("❌ Controller disconnected")

        # Button
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"🔘 BUTTON {event.button} DOWN")

        elif event.type == pygame.JOYBUTTONUP:
            print(f"⚪ BUTTON {event.button} UP")

        # Analog stick / trigger
        elif event.type == pygame.JOYAXISMOTION:
            value = event.value

            # Ignore tiny joystick noise
            if abs(value) > 0.05:
                print(
                    f"🕹️ AXIS {event.axis}: "
                    f"{value:+.3f}"
                )

        # D-Pad
        elif event.type == pygame.JOYHATMOTION:
            print(
                f"🎯 HAT {event.hat}: "
                f"{event.value}"
            )

        # Quit
        elif event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
