#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime

class Timer(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Timer, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--time", help="The timer length, %M:%S or %S, 0:0-59:59", type=str, default="0:30")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/10x20.bdf")
        textColor = graphics.Color(255, 255, 255)
        time_format = "%M:%S"
        try:
            try:
                timer_counter = datetime.datetime.strptime(self.args.time, time_format)
            except:
                time_format = "%S"
                timer_counter = datetime.datetime.strptime(self.args.time, time_format)
        except:
            print("Illegal time argument!")
            return False
        x = self.args.led_cols / 8
        y = self.args.led_rows / 2
        seconds = timer_counter.minute * 60 + timer_counter.second + 1
        for s in range(seconds):
            offscreen_canvas.Clear()
            time_str = datetime.datetime.strftime(timer_counter, time_format)
            graphics.DrawText(offscreen_canvas, font, x, y, textColor, time_str)
            time.sleep(1)
            timer_counter -= datetime.timedelta(seconds=1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == "__main__":
    timer = Timer()
    if (not timer.process()):
        timer.print_help()

