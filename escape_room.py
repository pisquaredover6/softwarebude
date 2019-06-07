from room import Room
from task import Task
from countdown import Countdown
import helper, threading


class EscapeRoom(Room):
    def __init__(self, name, description,  task):
        super().__init__(name, description)
        self.task = task

    def escape_room_intro(self):
        self.task = Task('Was ist 2+2', '4')  #TODO: Question and answer! Better place?
        print('Oh. Hallo. Gut das du da bist. Ich brauche deine Hilfe!')
        helper.wait(2)
        print('Ich komme bei diesem Problem nicht weiter. Kannst du es für mich lösen?')
        helper.wait(2)
        print('Eigentlich hast du keine anderer möglichkeit. Dafür bezahle ich dich schließlich')
        helper.wait(2)
        count = Countdown(20)               #Here you can change the countdown!
        count.start()
        self.task.show_question()
        self.start_task()
        count.stop_countdown()
        print('Du hast die Aufgabe erfüllt!!!')

    def start_task(self):
        while True:
            answer = input('Wie lautet die Lösung? ')
            print(self.task.is_answer_correct(answer))
            if self.task.is_answer_correct(answer):
                return
