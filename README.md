# HIIT Timer

I made a basic HIIT timer so I wouldn't have to rely on online pages and 
really terrible HIIT phone apps that do too much for me anyway. It's the
bare minimum:

* Say (with TTS) and display the current state of the routine (exercise name, rest, upcoming exercise)
* Make your routine on the fly
* Load up created plaintext routines

It doesn't do anything else and there is no reason I can find for it to 
do anything more.


### Preset Routines

There are four fields necessary for a successful routine file:

* `exercises:` - A list of exercises which will comprise one rep. This 
list is comprised of an `exercises:` line, followed by an exercise on
each subsequent line.
* `exercise_time:` - How long to spend on one exercise in seconds. This 
and all the following fields are to be comprised of the key and value on
the same line.
* `rest_time:` - How long to spend resting between exercises in seconds.
* `reps:` - How many cycles of the list of exercises to do in total.

The parser overlooks blank lines and lines that begin with `#`. 

A sample routine looks like this:

```
# Sample Exercise Routine 1

exercises:
	Pushups
	Squats
	Plank
	Jumping Jacks

exercise_time: 30

rest_time: 10

reps: 4
```