

class Vector(object):
    def __init__(self, coordinates):    #init will be run when class is instantiated, self is required, coordinates are the parameter passed in
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)      #fist try statement is executed if there is an error it jumps to the except
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):   #built-in method to print
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v): #built-in method to test for equality
        return self.coordinates == v.coordinates


