from sympy import plot

class UIPlot:
    """Class that plots the user input function and its approximated Taylor polynomial.
    """

    def plotting(self, func, taylor):
        """Takes user input function and Taylor polynomial and graphs them using sympy plot method.

        Args:
            func: Sympified user input function
            taylor: approximated Taylor polynomial
        """
        graph = plot(taylor, func, title="Taylor polynomial approximation",
                     legend=True, show=False, xlabel='x')
        graph[0].line_color = 'b'
        graph[1].line_color = 'r'
        graph.show()
