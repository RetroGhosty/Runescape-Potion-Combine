import pyautogui
import keyboard
import time
import random

# semi button location
x = 105
y = 530


# example random_algorithm(50, 0.5, 0.3)
def random_algorithm(value, chance, furtherIncreaseChance):
    chance = random.random()  # Generates a random value between 0 and 1

    if chance < 0.5:  # 50% chance of increasing
        increase = random.uniform(4, 8)
        value += increase
    else:
        decrease = random.uniform(4, 8)
        value -= decrease

    further_increase_chance = random.random()
    if (
        further_increase_chance < furtherIncreaseChance
    ):  # 20% chance of increasing further
        further_increase = random.uniform(6, 10)
        value += further_increase
    return value


def random_tick(value, chance, furtherIncreaseChance):
    chance = random.random()  # Generates a random value between 0 and 1

    if chance < 0.5:  # 50% chance of increasing
        increase = random.uniform(0.1, 0.2)
        value += increase
    else:
        decrease = random.uniform(0.1, 0.2)
        value -= decrease

    further_increase_chance = random.random()
    if (
        further_increase_chance < furtherIncreaseChance
    ):  # 20% chance of increasing further
        further_increase = random.uniform(0.1, 0.3)
        value += further_increase
    return value


def click(x, y):
    randomX = random_algorithm(x, 0.5, 0.3)
    randomY = random_algorithm(y, 0.5, 0.3)
    pyautogui.moveTo(randomX, randomY, random_tick(0.3, 0.5, 0.2))
    time.sleep(random_tick(0.2, 0.5, 0.2))
    pyautogui.click(randomX, randomY)


def finderclick(image):
    while True:
        try:
            if pyautogui.locateCenterOnScreen(image, confidence=0.7) != None:
                x, y = pyautogui.locateCenterOnScreen(image, confidence=0.7)
                pyautogui.moveTo(x, y, random_tick(0.2, 0.5, 0.6))
                time.sleep(0.2)
                click(x, y)
                return True

        except TypeError:
            return False


def findThis(image):
    while True:
        try:
            if pyautogui.locateCenterOnScreen(image, confidence=0.7) != None:
                x, y = pyautogui.locateCenterOnScreen(image, confidence=0.7)
                pyautogui.moveTo(x, y)
                return True
            else:
                return False
        except TypeError:
            return False


def smith_iron_ore():
    isDoneSmith = True
    time_delay = 0.4
    isMenuFound = False

    # 2. click ore
    pyautogui.moveTo(355, 167)
    time.sleep(time_delay)
    click(355, 167)
    time.sleep(time_delay)

    # 3. click bank exit
    pyautogui.moveTo(961, 49)
    time.sleep(time_delay)
    click(961, 49)
    time.sleep(time_delay)

    finderclick("magic_book.png")
    time.sleep(time_delay)

    while isDoneSmith == True:
        finderclick("fire.png")  # 4. click fire
        time.sleep(time_delay + 0.5)
        try:
            oreX, oreY = pyautogui.locateCenterOnScreen("iron_ore.png", confidence=0.8)
            click(1517, 763)
        except:
            isDoneSmith = False

    while isMenuFound == False:
        try:
            tryx, tryy = pyautogui.locateCenterOnScreen(
                "example_menu.png", confidence=0.7
            )
            print("Menu found")
            isMenuFound = True
        except:
            print("No menu found")
            isMenuFound = False
            click(478, 375)

    time.sleep(2)
    click(1517, 763)  # 6. click bottom
    time.sleep(time_delay)


def unicorn_dust():
    isDoneSmith = True
    time_delay = 0.2
    isMenuFound = False

    # 2. click ore
    pyautogui.moveTo(355, 167)
    time.sleep(time_delay)
    click(355, 167)
    time.sleep(time_delay)

    # 3. click bank exit
    pyautogui.moveTo(961, 49)
    time.sleep(time_delay)
    click(961, 49)
    time.sleep(time_delay)
    while isDoneSmith == True:
        try:
            oreX, oreY = pyautogui.locateCenterOnScreen("raw_item.png", confidence=0.8)
            click(1517, 763)
            time.sleep(0)
            click(1443, 760)
        except:
            isDoneSmith = False

    while isMenuFound == False:
        try:
            time.sleep(0.4)
            tryx, tryy = pyautogui.locateCenterOnScreen(
                "example_menu.png", confidence=0.7
            )
            print("Menu found")
            isMenuFound = True
        except:
            print("No menu found")
            isMenuFound = False
            click(770, 371)

    time.sleep(time_delay)
    click(1443, 760)  # 6. click bottom
    time.sleep(time_delay)


# 60% stretched mode
def potion_making():
    isDoneSmith = True
    time_delay = 0.3
    isMenuFound = False
    runescapeTick = 0.7

    click(303, 172)
    click(385, 176)
    click(943, 53)

    # step 3: combine
    click(1333, 593)
    click(1401, 593)
    finderclick("combine_button.png")
    while True:
        try:
            oreX, oreY = pyautogui.locateCenterOnScreen("raw_item.png", confidence=0.8)
        except:
            break
    while isMenuFound == False:
        try:
            time.sleep(0.4)
            tryx, tryy = pyautogui.locateCenterOnScreen(
                "example_menu.png", confidence=0.7
            )
            print("Menu found")
            break
        except:
            print("No menu found")
            click(770, 371)

    click(1268, 426)  # 6. click bottom
    time.sleep(runescapeTick)


def high_alch():
    finderclick("high_alch.png")
    if findThis("findThis.png") == True:
        finderclick("findThis.png")
    else:
        finderclick("raw_alch.png")


while True:
    potion_making()
