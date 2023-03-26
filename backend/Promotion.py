class Promotion():
    def __init__(self, percent, start_date, end_date, net):
        self.__percent = percent
        self.__start_date = start_date
        self.__end_date = end_date
        self.__net = net
    @property
    def percent(self):
        return self.__percent
    @property
    def start_date(self):
        return self.__start_date
    @property
    def end_date(self):
        return self.__end_date
    @property
    def net(self):
        return self.__net
promotion1 = Promotion(
    percent = '10',
    start_date = '21/01/66',
    end_date = '30/01/66',
    net = ' '
)

promotion2 = Promotion(
    percent = '20',
    start_date = '02/02/66',
    end_date = '30/02/66',
    net = ' '
)
