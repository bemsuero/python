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
            "You take the big sleep.",
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
                        You keep your short sword ready at your side as you start walking toward
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
                    Should you cast 'magic missile'? Should you 'run' away?
                    """))
                action = input("> ").lower()

                if action == "yell":
                    print(dedent("""
                        'STOP FIEND', you yell out. The zombie doesn't seem to have any manners.
                        It lurches forward and grabs on to you. Maybe yelling at a zombie wasn't
                        such a good idea.
                        """))
                    return "death"

                elif action == "magic missile":
                    print(dedent("""
                        Your 3 missiles all hit the creature. The first stuns him, the second stops
                        him completely, and the last cracks the creatures skull open. The body falls
                        limp and it seems to have died for the final time. You breathe a sigh of relief.
                        """))
                    return 'mimic_room'

                elif action == "run":
                    print(dedent("""
                        'No treasure is worth my life', you think. You turn around to high-tail it
                        out of the dungeon. You take the first left, then another left. You feel
                        like you may have went the wrong way. As you stand contemplating why you
                        didn't draw a map, you feel a cold hand on your shoulder.
                        """))
                    return "death"

                else:
                    print("Your indecision has cost you your life.")
                    return "death"

            elif character == "fighter":
                print(dedent("""
                    You expected horrors so you are not surprised. Your warrior spirit urges you
                    forward. The only option is attack. You bring the short sword up to take down
                    the abomination. Should you cut off it's 'arms' to stop it's attack? Go for the
                    'legs' and hinder it's mobility? Or should you go straight for the 'head', and
                    end it's misery?
                    """))
                action = input("> ").lower()

                if action == "arms":
                    print(dedent("""
                        You swing wildly at the creature's arm. It comes clean off. As you swing
                        down onto the other arm you lose momentum. The blade gets caught halfway
                        through the shoulder. As you struggle to get it off the zombie rears forward
                        and sinks his teeth into your neck.
                        """))
                    return "death"

                elif action == "legs":
                    print(dedent("""
                        'It can not eat me if it can not catch me', you chuckle to yourself.
                        You lunge forward, and do a horizontal attack towards the creature's
                        left leg. The blade sinks into it's hip and gets stuck. As you try to yank
                        it out, the creature grabs a hold of you. The last thing you see is a dirty
                        grin.
                        """))
                    return "death"

                elif action == "head":
                    print(dedent("""
                        A classic villain deserves a classic approach. You run forward and leap
                        into the air. Screaming, you plunge your sword into the zombie's skull. It
                        gasps like it needs air and collapses. Foolish creature thought that it could
                        get through you.
                        """))
                    return "mimic_room"

            elif character == "rogue":
                print(dedent("""
                    'Well, this is a sticky situation.', you think to yourself. 'I am not exactly the
                    fighting type.' Your options are not limited, however. You consider 'running' and getting
                    a better position. You think that maybe you could 'slice' up this particular foe, as
                    he seems slow. A last resort is to somehow 'sneak' by it. How good could the senses of
                    an undead be?
                    """))
                action = input("> ").lower()

                if action == "running":
                    print(dedent("""
                        You turn back and run around the corner. You hear the shambling of the creature as
                        it gets closer and closer. It seems like it can either hear your breathing, or smell
                        the metal hidden in your cloak. The waiting seems eternal. You take one deep breath
                        and as it turns the corner you plunge your dagger into it's face. That seems to be enough
                        to take it down. Good thing you're not a fighter.
                        """))
                    return "mimic_room"

                if action == "slice":
                    print(dedent("""
                        Confident that you are quicker than this fiend, you run up and start hacking at it
                        with your hidden dagger. You slice up and down his body, not missing one vital point.
                        You are sure that after this barrage of blows not a single living creature would be
                        standing. Unfortunately for you this creature is not living. It grabs you with it's bloody
                        limbs.
                        """))
                    return "death"

                if action == "sneak":
                    print(dedent("""
                        'It turning around was probably a coincidence', you think. You slowly duck down and
                        start making your way towards the creature. It doesn't break it's gaze on you, but
                        you figure that it is not smart enough to do anything. As you slowly sneak past it you
                        breath a sigh of relief that it hasn't moved. You pat yourself on the back for a job well
                        done. Then you feel another, colder, hand on your back.
                        """))
                    return "death"

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
