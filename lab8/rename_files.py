import re

''' TASK
	A list of file names is given. Rename each file following next pattern:
		Python-NN__yyyy_mm_dd.mp4

		where:
			yyyy - year, like 2020
			mm   - month, like 07
			dd   - day, like 21
			NN   - lecture number, like 38
	'''


file_names = [
	"Python_21.07.2020_Lekcia_38.mp4",
	"Python_22.08.2020_39.mp4",
	"Pthon_23.08.2020_Lekjk_40.mp4",
	"24.08.2020_Python_41.mp4",
	"25.08.2020_Python_42_Lekcia.mp4"
]

reanamed_filenames = []

rx = re.compile(r'(?P<dd>\d{2})\.(?P<mm>\d{2})\.(?P<yyyy>\d{4}).+(?P<NN>\d{2})')

for fn in file_names:
	m = rx.search(fn)
	g = m.groupdict()
	# print(f"{g['yyyy']}_{g['mm']}_{g['dd']}-{g['NN']}.mp4")
	# print(m[1],m[2],m[3],m[4])
	reanamed_filenames.append(f"Python-{g['NN']}__{g['yyyy']}_{g['mm']}_{g['dd']}.mp4")

for fn in reanamed_filenames:
	print(fn)

# EXPECTED OUTPUT
# Python-38__2020_07_21.mp4
# Python-39__2020_08_22.mp4
# Python-40__2020_08_23.mp4
# Python-41__2020_08_24.mp4
# Python-42__2020_08_25.mp4


