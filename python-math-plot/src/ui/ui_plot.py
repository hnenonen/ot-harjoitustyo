from sympy import plot

class UIPlot:

    def plotting(self, func, t):
        graph = plot(t, func, title="Taylor polynomial approximation",
                     legend=True, show=False, xlabel='x')
        graph[0].line_color = 'b'
        graph[1].line_color = 'r'
        graph.show()
