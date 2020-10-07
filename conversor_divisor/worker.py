from PySide2.QtCore import QThread, QObject, Signal, Slot


class SignalsToWorker(QObject):

    progress_signal = Signal(object)
    process_signal = Signal(object)
    done_signal = Signal(object)
    error_signal = Signal(object)


class Worker(QThread):

    def __init__(self, _class=None, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = _class
        self.args = args
        self.kwargs = kwargs
        self.signal = SignalsToWorker()

        self.kwargs['progress_signal'] =  self.signal.progress_signal
        self.kwargs['process_signal'] = self.signal.process_signal
        self.kwargs['done_signal'] = self.signal.done_signal
        self.kwargs['error_signal'] = self.signal.error_signal

    @Slot()
    def stop(self):
        self.terminate()
        
    @Slot()
    def run(self):
        c = self._class(*self.args, **self.kwargs)
        c.convert_or_split()
        