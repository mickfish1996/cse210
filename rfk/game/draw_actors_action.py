from game.action import Action

# TODO: Add your DrawActorsAction class here
class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.clear_screen()

        self._output_service.draw_actors(cast["artifact"])
        self._output_service.draw_actors(cast["robot"])
        self._output_service.draw_actors(cast["marquee"])

        self._output_service.flush_buffer()