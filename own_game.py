from sys import exit
from random import randint
from textwrap import dedent

    # if character == 'wizard':
    # elif character == 'fighter':
    # elif character == 'rogue':
    # else:

def main():
    character = "Human"
    print("Choose your class! Wizard, Fighter, or Rogue.")
    character = input(">").lower()

    if character != "wizard" and character != "fighter" and character != "rogue":
        print("This dungeon is too dangerous without a class.")
        main()

    print(f"You have chosen a {character}")

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
                Do you dare go inside? 'Enter' or 'Leave', the choice is yours.
                """))

            if character == 'wizard':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You saunter in, your robes flowing in the wind. Your spellbook
                        is clutched in your hand, as you anticipate the adventure that
                        is ready to begin.
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

            elif character == 'fighter':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You keep your sword ready at your side as you start walking toward
                        the entrance. You are wary of the monsters and ghouls who are said
                        to live in these walls. You are brave above all.
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

            elif character == 'rogue':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You walk along the shadows, dagger hidden. You are aware of the traps
                        that might be around every corner. Tricks and treats were always your
                        forte.
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

    class FirstEncounter(Scene):

        def enter(self):
            print(dedent("""
                You enter the hallowed halls of the dungeon. The air is thick with the stench
                of old wood and rottng flesh. You glance around. Nothing seems to have been
                touched for a long time. If other adventurers came through here, there is no
                longer a trace of them. As you walk into the northern hall, you come across an
                opening with a thirty foot ceiling. In the middle of the room you see a shambling
                body. As soon as you see it, it turns around. A zombie approaches!
                """))

            if character == "wizard":
                print(dedent("""
                    You shudder in fear. The school prepared you for this, but you have never seen
                    a zombie up close. You consider what you can do. Should you 'yell' for it to stop?
                    Should you cast 'magic missle'? Should you 'run' away?
                    """))
                action = input("> ").lower()

                if action == "yell":
                    print(dedent("""
                        'STOP FIEND', you yell out. The zombie doesn't seem to have any manners.
                        It lurches forward and grabs on to you. Maybe yelling at a zombie wasn't
                        such a good idea.
                        """))
                    return "death"


            # elif character == "figher":

            # elif character == "rogue":


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

main()
