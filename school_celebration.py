# Author Sajad
"""
This pattern is called Facade which used to decrease coupling among
objects all required actions will perform by the EventManager class
The EventManager class it self knows all parts and client doesnt
"""


# The Facade
class EventManager:

    def __init__(self):
        print('Will speak to all units')

    def arrange(self):
        self.presenter = Presenter()
        self.presenter.set_presentation()

        self.theater_group = TheaterGroup()
        self.theater_group.set_theater()

        self.caterer = Caterer()
        self.caterer.set_catering()

        self.lecture = Lecture()
        self.lecture.set_lecture()

        self.music_group = MusicGroup()
        self.music_group.set_music()


class Presenter:
    def __init__(self):
        print('setting meeting date')

    def set_presentation(self):
        print('tell the details of the celebration')


class TheaterGroup:
    def __init__(self):
        print('setting the date')

    def set_theater(self):
        print('what kind of theater and the time')


class Caterer:
    def __init__(self):
        print('setting meeting date')

    def set_catering(self):
        print('how many guests and the time')


class Lecture:
    def __init__(self):
        print('setting meeting date')

    def set_lecture(self):
        print('The subject and the time')


class MusicGroup:

    def __init__(self):
        print('set meeting date')

    def set_music(self):
        print('choose the music')


# Client Section
class HeadMaster:

    def tell_manager(self):
        em = EventManager()
        em.arrange()


you = HeadMaster()
you.tell_manager()
