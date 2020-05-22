"""Run a round-robin league between a number of historical or all-time teams.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec aliquam diam. Quisque nec elit tellus. Mauris
mollis fringilla erat, ut sagittis ligula varius vitae. Vestibulum eget neque neque. Etiam volutpat viverra dolor, eget
volutpat orci blandit sit amet. Aliquam massa lorem, blandit nec dignissim vel, fermentum eu mi. Vivamus eleifend enim
non pellentesque egestas. Phasellus pretium lectus a justo consequat, ut facilisis dui tempor. Donec pulvinar nisl sit
amet libero rhoncus, non dignissim diam consequat. Aliquam erat volutpat. Integer eu condimentum velit.

  Typical usage example:


"""
from customleague import teamnumber, gamenumber, league
from historical import HistoricalYearsSelect, CountrySelect, histplayers
from callcricketnew import team

def setup (x):
	t = team ()
	t.active = histplayers(x, a, b)
	if x == 'all': 
		x = 'World'
		for i in t.active: i.team = x
	t.name = x
	return t

if __name__ == '__main__':
	print ('Historical league')

	x = teamnumber ()
	t = []
	a, b = 2020, 2020
	for i in range (x):
		[a,b] = HistoricalYearsSelect(a, b)
		z = CountrySelect(a,b)
		c = setup(z)

		for j in t:
			if c.name == j.name:
				c.name = '{} {}'.format(c.name, a)
				for k in c.active:
					k.team = c.name

		t.append(c)
		y = a

	n = gamenumber ()

	league (t, n)