from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below


class Class:
    def __init__(self, year, season, departments, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, res_open, waitlist):
        self.year = year
        self.season = season
        self.departments = departments
        self.number = number
        self.section = section
        self.title = title
        self.units = units
        self.instructors = instructors
        self.meetings = meetings
        self.core = core
        self.seats = seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.res__open = res_open
        self.waitlist = waitlist


def get_data():
    classes = []
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            year, season, departments, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, res_open, waitlist = line.split('\t')
            current = Class(year, season, departments, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, res_open, waitlist)
            classes.append(current)
    return classes


@app.route('/')
def view_root():
    classes = get_data()
    return render_template('base.html', classes=classes)


# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)
