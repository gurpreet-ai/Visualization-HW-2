
import svgutils.transform as sg

fig1 = sg.fromfile('figure_2.svg')
fig2 = sg.fromfile('figure_5.svg')

plot1 = fig1.getroot()
plot2 = fig2.getroot()

fig = sg.SVGFigure("32cm", "43cm")

plot1.moveto(0,0)
plot2.moveto(0, 700)

txt1 = sg.TextElement(225,20, "Figure A: Carapace Width V. Carapace Length and Carapace Width V. Frontal Lobe Size.", size=12, weight="bold")
txt2 = sg.TextElement(225,700, "Figure B: CL and FL V. CW (without sorting)", size=12, weight="bold")

fig.append([plot1, plot2])
fig.append([txt1, txt2])

fig.save('final_figure1.svg')
