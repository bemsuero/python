from sys import exit
from random import randint
from textwrap import dedent

    # if character == 'wizard':
    # elif character == 'fighter':
    # elif character == 'rogue':


character = "Human"
print("Choose your class! Wizard, Fighter, or Rogue.")
character = input(">").lower()
print(f"You have chosen a {character}")

# if character != "wizard" or character != "fighter" or character != "rogue"

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.",
        "You didn't live.",
        "Dead for the first time, again.",
        "Red Dead Redemption.",
        "You fell through life into death."


    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class EnterDungeon(Scene):

    def enter(self):
        print(dedent("""
            You see a dungeon before you and know that your destiny nears.
            Do you dare go inside? Enter or Leave, your choice.
                """))

        if character == 'wizard':
            action = input("> ").lower()

            if action == "enter":
                print(dedent("""
                You saunter in, your robes flowing in the wind
                    """))
                return "first_encounter"

            elif action == "leave":
                print(dedent("""
                You turn back, unprepared for the horrors that are right behind you.
                    """))
                return "death"

            else:
                print("Your indecision has cost you your life.")
                return "death"

        # elif character == 'fighter'
        # elif character == 'rogue'
        # else
        action = input("> ")

class FirstEncounter(Scene):
    print("done")


class MimicRoom(Scene):
    print("done")

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return "finished"

class Map(object):

    scenes = {
        'enter_dungeon': EnterDungeon(),
        'first_encounter': FirstEncounter(),
        'mimic_room': MimicRoom(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('enter_dungeon')
a_game = Engine(a_map)
a_game.play()
