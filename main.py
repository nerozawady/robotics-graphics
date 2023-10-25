import matplotlib.pyplot as matplot
import numpy
from adjustText import adjust_text

humans = {
    'Nero': {
        'talkative': 50,
        'distractive': 50,
        'distractable': 90,
        'off-topic': 20
    },
    'Jaren': {
        'talkative': 100,
        'distractive': 100,
        'distractable': 50,
        'off-topic': 40,
    },
    'Mya': {
        'talkative': 20,
        'distractive': 20,
        'distractable': 70,
        'off-topic': 5,
    },
    'Mari': {
        'talkative': 80,
        'distractive': 20,
        'distractable': 90,
        'off-topic': 60,
    },
    'Micah': {
        'talkative': 5,
        'distractive': 5,
        'distractable': 100,
        'off-topic': 10,
    },
    'Mr. Handsome': {
        'talkative': 100,
        'distractive': 100,
        'distractable': 80,
        'off-topic': 100,
    },
    'RJ': {
        'talkative': 20,
        'distractive': 50,
        'distractable': 100,
        'off-topic': 20,
    },
    'Max': {
        'talkative': 20,
        'distractive': 30,
        'distractable': 70,
        'off-topic': 30,
    },
    'Jakeonora': {
        'talkative': 70,
        'distractive': 70,
        'distractable': 70,
        'off-topic': 50,
    },
    # 'x': {
    #     'talkative': 80,
    # 'distractive': 20,
    #     'distractable': 90,
    #     'off-topic': 60,
    # }
}

# x_points = numpy.array([])
# y_points = numpy.array([])
x_points = []
y_points = []
texts = []
# fig, ax = matplot.subplots()

for human in humans:
    # texts.append(human)
    # x_points = numpy.append(
    #     x_points, humans[human]['talkative'])
    x_points.append(humans[human]['talkative'])

for human in humans:
    # y_points = numpy.append(
    # y_points, humans[human]['distractive'])
    y_points.append(humans[human]['distractive'])

# matplot.plot(x_points, y_points)
matplot.scatter(x_points, y_points)

for human in humans:
    # matplot.annotate(human, (humans[human]['talkative'] + 1,
    #                          humans[human]['distractive'] + 1))
    texts.append(matplot.text(humans[human]['talkative'],
                 humans[human]['distractive'],
                 human,
                 ha='center',
                 va='center'
                 ))

matplot.xlabel('Talkative')
matplot.ylabel('Distractive')
matplot.title('Talkative-Distractive Scale')
matplot.xlim((0, 110))
matplot.ylim((0, 110))
# print(texts)
# print(texts[0])
# , force_text=(2, 2)
# adjust_text(texts, force_points=(2, 2), force_text=(2, 2))
adjust_text(texts, force_points=(2, 2))
# adjust_text(texts, only_move={'points': 'y', 'texts': 'y'},
# arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
matplot.show()
